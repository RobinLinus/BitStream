# Burn Contract

Burn contract in Liquid Script. It requires mainly `OP_CAT` and `OP_CHECKSIGFROMSTACK`.

Developed and tested in [Script Wizard](https://ide.scriptwiz.app/) (in the top right corner, select `Liquid (v1_p2tr)`). Also, the output of `decrypt.py` is made compatible with this implementation.

```
// Make copy of the index and the two leaves to verify encryption later
<2>
OP_PICK
OP_TOALTSTACK
<3>
OP_PICK
OP_TOALTSTACK
<4>
OP_PICK
OP_TOALTSTACK




// Move preimage and signature to altstack
OP_TOALTSTACK
OP_TOALTSTACK
// Move index to altstack
OP_TOALTSTACK


// Compute Merkle root 

// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF

// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF

// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF

// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF

// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Loop begin
OP_DEPTH 
OP_1SUB
OP_IF

    OP_FROMALTSTACK
    OP_DUP
    <2>
    OP_DIV
    OP_TOALTSTACK
    <2>
    OP_MOD

    OP_NOTIF
        OP_SWAP
    OP_ENDIF

    OP_CAT
    OP_SHA256

OP_ENDIF


// Now the root is on the stack


OP_FROMALTSTACK
OP_DROP

OP_FROMALTSTACK

OP_FROMALTSTACK
OP_DUP
OP_TOALTSTACK
OP_SHA256

OP_ROT
OP_SWAP

OP_CAT

<0x12daa779c128ffd161ecdbdf233cad20bca1ee79df09819fbbbb412240679047>
OP_CHECKSIGFROMSTACK
OP_VERIFY


// Expected hash
OP_FROMALTSTACK

// Encrypted chunk
OP_FROMALTSTACK

// Secret Preimage
OP_FROMALTSTACK

// Index
OP_FROMALTSTACK



<3>
OP_ROLL
OP_SWAP

<2>
OP_DIV
// Add 1 to avoid 0 encoded as zero-byte
OP_1ADD

OP_CAT

OP_SHA256

OP_XOR

OP_SHA256

OP_EQUAL

OP_NOT
OP_VERIFY

```



## Example Inputs

### Valid Fraud Proof

The script succeeds for a path of an incorrectly encrypted file

```
// Merkle inclusion proof

<0x192ba599bc8f5e5b35b3ff04d1bda57dac2d726e6fd15181ade9105784097dfc>
<0x348b8269fda663fe19ce47ccbb26a9d512ab759ad103b64655a146b9832216ea>
<0xe0596898ccd511c7b7986951a601734ea5fd15474fa23fe70c5a3c93af8f5520>
<0xce1d84ab102ad318097de2d4e66848fef3c7a68b787f727d763460a4a01d854c>
<0xe8fa1978a1075f52bb4de461f5df5cff9e8f7da8c2d51f95ce5a6362e5683d7a>
<0x77b6caa0ca9f146a30c2170509c1a7a489bf67d20713752d62dafbd09b5440c8>
<0x69b1fb99f443e066169af26f965121eddff39d721a469928c39838713868fa6e>
<0x136b9de4d311458be68ef8840718874617f01a6cfc6c405577d6f2d1fa58a55a>
<0x08a2c6c19859a5a2b4a75359207823aeae2763a8bd03049a11965945376ce10e>
<0x51c3a10768ff893ae71b5bc97fdc7cd8d4a5420db390e92f1f6eb30a8a5e7088>
<0x385af78b2646a7a184613bec4a770f4d081c7fb4961af5bbcd3dbbc1b5f29274>
<0xb7da7cdd9daa6334983d473454cc1104cc18a20d1ef7e42cba42d972170473b5>
<0x6e3862fcd79bf67a9d64710e6bd27815e79106cb5933f6435af1644c6a91b153>
<0x3be8ab029e9d9a24adda121967593a4f926fcb5d75382feee53a59eb9e14b29a>
// Encrypted chunk: 
<0xd9a2c7ad0ec6d5e47a95465466b8e223720ea9365c0a8745f184a357feed626c>

// Index 
<0x0a>

// Signature 
<0xde6e8a2a1c8a698a16cd84eb0442acd3bc408ba355cc41308996f4b4fb0ca124b6e86bb2456b8697b39a6540ab634bb5151e6340eeacda97a658d247756f347c>


// Preimage 
<0x12d1e0adcc952d39c32399874c5c18f895212e47c63d36a052dcb95fc6aa1169>
```


### Invalid Fraud Proof 

The script fails for any path of a truthfully encrypted file

```
// Merkle inclusion proof

<0xbae6065a2a6fcc8079abe1bc629ebfa46f6c6032c5354362608f3619b02269a4>
<0xbc546a562110df76aac7a18dcb650f181d98e8d552688556fdaf1a415df6238f>
<0x5a817b8d59e59f71dffb2bcf94aa304d581d0d0b63fc95ad152e45e6d9784c26>
<0x352ce998130bfe4abad9ad9f3aa92eac11d1cf39e4eec0fcf5759e27413c440f>
<0xcb0b354e4699a63f2757a81ddea71339f5ef209c29ded9cda78514c1503039ec>
<0x5f5dab13d65d66e2f5f704499c351cb00e0c6419c9e3a858ae779c8f6ede7761>
<0x776b59674471db0e2439b295d0a9de0364eb4eec186b74bdb52ee6071471f414>
<0x4cc71e7bd4b5eea20ed4660254c3586fc8ff3cf4e32402bd200e46c87295bc6d>
<0xeecafa8fcdfdae90c4b2d0e063a74e83b4a8be9aec92000e3f429483b7d6312f>
<0x812f74b4200af037d63911ce37965d12ca979e9d2e95ea1b4eac870c017703a5>
<0x31b8f60bc8f65501b631d7f40839f324be7d764b158445a6ce2cfe195f483edc>
<0xae642d8421b73ef961516e2a880a4103af3f003f4468ef779c0873a53d128555>
<0xbc4b3c83da1dd3fa1d3e6935ace49d44e7a0f6bdf2ad1d6c73802d9678583155>
<0x729573482048167444b6c7ef75e842c77ce3bcfbce820f7aeb4bf32be4136339>
// Encrypted chunk: 
<0x6767a832fb7a6e08141e39b049143acfdd845b1b1555d525af2bf94ee695504f>

// Index 
<0x4a>

// Signature 
<0x1ee5c03f47eb4e1261c7d54d8d06c9d70e00fe94f90591d3879e5b16758d4890cbb8fb893176065f1aec3355e2f9589ad0191dd6b64fb88ad656359023891404>


// Preimage 
<0x0ea90c90b3dfef79887d81e920fda009c2e20bc84bb15fec4dc7c7baba2c28a3>
```
