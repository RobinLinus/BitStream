from utils import merkle_tree, split_file_into_chunks, encrypt_chunk, hash_data
import sys
import os
from hashlib import sha256
from secp256k1 import PrivateKey

if len(sys.argv) != 2:
    raise Exception("File name and preimage must be provided as an argument.")
file_path = sys.argv[1]

# Generate a random seed
preimage = os.urandom(32)

# preimage = bytes.fromhex(sys.argv[2])

payment_hash = sha256(preimage).digest()
print(f"Secret Preimage: \n{preimage.hex()}\n")
print(f"Payment Hash: \n{payment_hash.hex()}\n")

chunks = list(split_file_into_chunks(file_path))
encrypted_file = []
for index, chunk in enumerate(chunks):
    enc_chunk = encrypt_chunk(chunk, preimage, index)
    hash_chunk = hash_data(chunk)
    encrypted_file.append(enc_chunk)
    encrypted_file.append(hash_chunk)

### PRODUCE SOME RANDOM ERROR ### 
# tmp = encrypted_file[11]
# encrypted_file[11] = encrypted_file[10]
# encrypted_file[10] = tmp
### PRODUCE SOME RANDOM ERROR ### 

encrypted_root = merkle_tree(encrypted_file)
print(f"Encrypted FileId: \n{encrypted_root.hex()}\n")



# Compute the message
message = encrypted_root + payment_hash

# Example private key in hex
privkey_bytes = bytes.fromhex('3a1076bf45ab87712ad64ccb3b10217737f7faacbf2872e88fdd9a537d8fe267')
privkey = PrivateKey(privkey_bytes, raw=True)

# Get the public key
pubkey_serialized = privkey.pubkey.serialize(compressed=True)
x_only_pubkey = pubkey_serialized[1:]
print(f"Public Key: \n{x_only_pubkey.hex()}\n")

# Sign with Schnorr the encrypted root and the Payment hash
signature = privkey.schnorr_sign(message, '', raw=True)
print(f"Schnorr Signature: \n{signature.hex()}\n")

# Saving the encrypted chunks and their hashes to a file
with open(file_path + '.encrypted', 'wb') as file:
    file.write(signature)
    file.write(payment_hash)
    for item in encrypted_file:
        file.write(item)
