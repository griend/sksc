from cryptography.fernet import Fernet


def encode():
    # key is generated
    key = Fernet.generate_key().decode()
    print(f'Key: {key}')

    # value of key is assigned to a variable
    f = Fernet(key)

    # the plaintext is converted to ciphertext
    token = f.encrypt(b'Hello, World!')

    # display the ciphertext
    print(f'Token: {token.decode()}')

    # decrypting the ciphertext
    d = f.decrypt(token).decode()

    # display the plaintext
    print(f'Decrypted: {d}')


if __name__ == '__main__':
    encode()
