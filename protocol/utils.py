from hashlib import sha256

def split_file_into_chunks(file_path):
    with open(file_path, 'rb') as file:
        while chunk := file.read(32):
            yield chunk.ljust(32, b'\0')
            
def hash_data(data):
    if isinstance(data, str):
        data = data.encode()
    return sha256(data).digest()

def compute_hashes(elements):
    return [hash_data(e) for e in elements]

def merkle_tree(leaves):
    while len(leaves) > 1:
        if len(leaves) % 2 != 0:
            leaves.append(leaves[-1])

        new_leaves = [hash_data(leaves[i] + leaves[i+1]) for i in range(0, len(leaves), 2)]
        leaves = new_leaves

    return leaves[0]


def merkle_path(leaves, index, path=None):
    if path is None:
        path = []

    if len(leaves) == 1:
        return leaves[0].hex(), path
    
    if len(leaves) % 2 != 0:
        leaves.append(leaves[-1])
    
    new_leaves = []
    for i in range(0, len(leaves), 2):
        new_leaves.append(hash_data(leaves[i] + leaves[i+1]))
        if i <= index < i + 2:
            if index % 2 == 0:
                path.append(leaves[i+1].hex())
            else:
                path.append(leaves[i].hex())
            index = i // 2
    
    return merkle_path(new_leaves, index, path)


def encrypt_chunk(chunk, secret, index):
    hasher = sha256()
    hasher.update(secret)
    hasher.update(to_bytes(index + 1)) # We add +1 to avoid the case 0 == 0x encoded as zero bytes
    hash_ = hasher.digest()
    return bytes([a ^ b for a, b in zip(chunk, hash_)])

def to_bytes(n):
    if n == 0:
        return b''
    result = bytearray()
    neg = n < 0
    abs_n = abs(n)
    while abs_n:
        byte = abs_n & 0xff
        abs_n >>= 8
        result.append(byte)
    if result[-1] & 0x80:
        result.append(0x80 if neg else 0)
    elif neg:
        result[-1] |= 0x80
    return bytes(result)

