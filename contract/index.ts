import { bip341, address, networks, CreatorInput, CreatorOutput, Creator, script, Updater, Transaction, Finalizer, Pset, TapLeafScript, witnessStackToScriptWitness, Extractor } from 'liquidjs-lib';
import secp256k1 from '@vulpemventures/secp256k1-zkp';
import fetch from 'node-fetch';

const { BIP341Factory } = bip341;
const { OPS } = script;

const internalPubkey = Buffer.from('021dae61a4a8f841952be3a511502d4f56e889ffa0685aa0098773ea2d4309f624', 'hex');

const scriptHex = '52796b53796b54796b6b6b6b748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea868748c92636c76519976766b9394647c687ea8686c756c6c766ba87b7c7e2012daa779c128ffd161ecdbdf233cad20bca1ee79df09819fbbbb412240679047c26c6c6c6c537a7c528b7ea886a887916900d14f88016aa88800ce7520499a818545f6bae39fc03b637f2a4e1e64e590cac1bc3a6f6d71aa4443654c148800cf750850c3000000000000887551';

const prevoutTxID = '8d6c3396b1e7671ddc42488775512532ab2bbab328618b6ea3af7cbd7cc9a472';
const prevoutIndex = 1;

const prevoutValue = 100000;
const burnValue = 50000;


const unlockingScript = [
    // Merkle inclusion proof
    '192ba599bc8f5e5b35b3ff04d1bda57dac2d726e6fd15181ade9105784097dfc',
    '348b8269fda663fe19ce47ccbb26a9d512ab759ad103b64655a146b9832216ea',
    'e0596898ccd511c7b7986951a601734ea5fd15474fa23fe70c5a3c93af8f5520',
    'ce1d84ab102ad318097de2d4e66848fef3c7a68b787f727d763460a4a01d854c',
    'e8fa1978a1075f52bb4de461f5df5cff9e8f7da8c2d51f95ce5a6362e5683d7a',
    '77b6caa0ca9f146a30c2170509c1a7a489bf67d20713752d62dafbd09b5440c8',
    '69b1fb99f443e066169af26f965121eddff39d721a469928c39838713868fa6e',
    '136b9de4d311458be68ef8840718874617f01a6cfc6c405577d6f2d1fa58a55a',
    '08a2c6c19859a5a2b4a75359207823aeae2763a8bd03049a11965945376ce10e',
    '51c3a10768ff893ae71b5bc97fdc7cd8d4a5420db390e92f1f6eb30a8a5e7088',
    '385af78b2646a7a184613bec4a770f4d081c7fb4961af5bbcd3dbbc1b5f29274',
    'b7da7cdd9daa6334983d473454cc1104cc18a20d1ef7e42cba42d972170473b5',
    '6e3862fcd79bf67a9d64710e6bd27815e79106cb5933f6435af1644c6a91b153',
    '3be8ab029e9d9a24adda121967593a4f926fcb5d75382feee53a59eb9e14b29a',

    // Encrypted chunk
    'd9a2c7ad0ec6d5e47a95465466b8e223720ea9365c0a8745f184a357feed626c',

    // Index 
    '0a',

    // Signature 
    'de6e8a2a1c8a698a16cd84eb0442acd3bc408ba355cc41308996f4b4fb0ca124b6e86bb2456b8697b39a6540ab634bb5151e6340eeacda97a658d247756f347c',

    // Preimage 
    '12d1e0adcc952d39c32399874c5c18f895212e47c63d36a052dcb95fc6aa1169'

].map(e => Buffer.from(e, 'hex'));


(async () => {
    // get prevout 

    const res = await fetch(`https://blockstream.info/liquidtestnet/api/tx/${prevoutTxID}/hex`);
    const prevoutTxHex = await res.text();
    const prevoutTx = Transaction.fromHex(prevoutTxHex);
    const prevoutTxOut = prevoutTx.outs[prevoutIndex];

    const { ecc: ecclib } = await secp256k1();
    const leaves: bip341.TaprootLeaf[] = [{ scriptHex }];
    const hashTree = bip341.toHashTree(leaves);
    const output = BIP341Factory(ecclib).taprootOutputScript(
        internalPubkey,
        hashTree,
    );
    const taprootAddress = address.fromOutputScript(output, networks.testnet); // UNCONFIDENTIAL
    console.log(taprootAddress);


    /// let's try to spend it
    const inputs = [new CreatorInput(prevoutTxID, prevoutIndex)];

    const outputs = [
        new CreatorOutput(
            networks.testnet.assetHash,
            burnValue,
            Buffer.of(OPS.OP_RETURN),
        ),
        new CreatorOutput(networks.testnet.assetHash, prevoutValue - burnValue),
    ];

    const pset = Creator.newPset({
        inputs,
        outputs,
    });

    const updater = new Updater(pset);
    updater.addInWitnessUtxo(0, prevoutTxOut);
    updater.addInSighashType(0, Transaction.SIGHASH_ALL);

    const leafHash = bip341.tapLeafHash(leaves[0]);
    const pathToLeaf = bip341.findScriptPath(hashTree, leafHash);
    const [script, controlBlock] = BIP341Factory(ecclib).taprootSignScriptStack(
        internalPubkey,
        leaves[0],
        hashTree.hash,
        pathToLeaf,
    );

    updater.addInTapLeafScript(0, {
        controlBlock,
        leafVersion: bip341.LEAF_VERSION_TAPSCRIPT,
        script,
    });

    const finalizer = new Finalizer(pset);

    finalizer.finalizeInput(0, (index, pset: Pset) => {
        const tapLeafScript = pset.inputs[index]
            .tapLeafScript![0] as TapLeafScript;
        return {
            finalScriptSig: undefined,
            finalScriptWitness: witnessStackToScriptWitness([
                ...unlockingScript,
                tapLeafScript.script,
                tapLeafScript.controlBlock,
            ]),
        };
    });

    const tx = Extractor.extract(pset);
    const hex = tx.toHex();
    console.log(hex);
})();