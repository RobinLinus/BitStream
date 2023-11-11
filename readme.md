# BitStream (Early Prototype)

BitStream -- a decentralized file-hosting network based on Bitcoin.

## Installation
```
pip install secp256k1
```

## Protocol
First, enter the `protocol` directory: `cd protocol`. 

### Publish
Compute the file_id of a file.

```
python publish.py examples/bitcoin.pdf
```

### Encrypt
Encrypt a file, save it to disk, and display the secret preimage used for encryption.

```
python encrypt.py examples/bitcoin.pdf
```

### Verify
Verify that an encrypted file claims to be the file named file_id and display its payment hash.

```
python verify.py examples/my_file.txt.encrypted
```

### Decrypt
Tries to decrypt and save the file. If that fails, it returns the fraud proof.

```
python3 decrypt.py examples/bitcoin.pdf.encrypted <your_preimage_here>
```