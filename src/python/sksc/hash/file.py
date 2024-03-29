"""
See: https://nitratine.net/blog/post/how-to-hash-files-in-python/
"""


import hashlib
import sys

BLOCK_SIZE = 65536  # The size of each read from the file


def hashfile(filename: str):
    file_hash = (
        hashlib.sha256()
    )  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(filename, "rb") as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    return file_hash.hexdigest()  # Get the hexadecimal digest of the hash


if __name__ == "__main__":
    filename = sys.argv[1]
    hash = hashfile(filename)
    print(f"{filename}: {hash}")
