from utils import merkle_tree, compute_hashes, split_file_into_chunks, encrypt_chunk, hash_data
import sys
import os

# This has to get checked in Liquid
PUBLIC_KEY_SERVER = bytes.fromhex("0212daa779c128ffd161ecdbdf233cad20bca1ee79df09819fbbbb412240679047")


if len(sys.argv) != 2:
    raise Exception("File name must be provided as an argument.")
file_path = sys.argv[1]

chunks = list(split_file_into_chunks(file_path))
signature = chunks[0] + chunks[1]
payment_hash = chunks[2]
chunks = chunks[3:]

# Every second chunk
chunk_hashes = chunks[1::2]
file_id = merkle_tree(chunk_hashes)

encrypted_root = merkle_tree(chunks)


message = encrypted_root + payment_hash

from secp256k1 import PublicKey

# Create a PublicKey object from the serialized public key
pubkey = PublicKey(PUBLIC_KEY_SERVER, raw=True)

# Verify the Schnorr signature
if not pubkey.schnorr_verify(message, signature, raw=True, bip340tag=''):
    raise "Signature is invalid"

print(f"FileId: \n{file_id.hex()}\n")
print(f"Encrypted FileId: \n{encrypted_root.hex()}\n")
print(f"Payment hash: \n{payment_hash.hex()}\n")