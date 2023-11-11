from utils import merkle_path, split_file_into_chunks, encrypt_chunk, hash_data
import sys
import os
from hashlib import sha256

if len(sys.argv) != 3:
    raise Exception("File name and preimage must be provided as arguments.")
file_path = sys.argv[1]
preimage = bytes.fromhex(sys.argv[2])

# Read the File
chunks = list(split_file_into_chunks(file_path))
signature = chunks[0] + chunks[1]
payment_hash = chunks[2]

if payment_hash != sha256(preimage).digest():
    raise Exception("Preimage mismatch\n")

chunks = chunks[3:]
encrypted_chunks = chunks[0::2]
expected_hashes = chunks[1::2]

decrypted_file = []
for index, encrypted_chunk in enumerate(encrypted_chunks):
    decrypted_chunk = encrypt_chunk(encrypted_chunk, preimage, index)
    decrypted_chunk_hash = hash_data(decrypted_chunk)
    expected_hash = expected_hashes[index]

    if decrypted_chunk_hash != expected_hash:
        root, path = merkle_path(chunks, 2*index)

        print("// Merkle inclusion proof\n")
        path.reverse()
        for node in path:
            print(f"<0x{node}>")
            
        print(f"// Encrypted chunk: \n<0x{encrypted_chunk.hex()}>\n")
        
        index = index * 2
        index = f'{index:0{2 * ((len(hex(index)) - 2 + 1) // 2)}x}'
        print(f"// Index \n<0x{(index)}>\n")
        print(f"// Signature \n<0x{signature.hex()}>\n\n")
        print(f"// Preimage \n<0x{preimage.hex()}>\n\n")

        raise ValueError

    decrypted_file.append(decrypted_chunk)

# Saving the encrypted chunks and their hashes to a file
base_name, extension = file_path.replace(".encrypted", "").rsplit('.', 1)
file_path = f"{base_name}_decrypted.{extension}"
with open(file_path, 'wb') as file:
    for item in decrypted_file:
        file.write(item)

print(f'Successfully decrypted {file_path}')
