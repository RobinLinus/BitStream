from utils import merkle_tree, compute_hashes, split_file_into_chunks
import sys

if len(sys.argv) != 2:
    raise Exception("File name must be provided as an argument.")
file_path = sys.argv[1]

chunks = split_file_into_chunks(file_path)
leaves = compute_hashes(chunks)
root = merkle_tree(leaves)

print(f"FileId: \n{root.hex()}\n")