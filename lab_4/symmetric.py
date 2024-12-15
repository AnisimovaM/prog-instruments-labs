import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from work_with_files import *


def generation_key(size_key: int) -> bytes:

    if size_key not in [128, 192, 256]:
        raise ValueError("Invalid key length. Please choose 128, 192, or 256 bits.")
    key = os.urandom(size_key // 8)
    return key


def key_serialization(key: bytes, path: str) -> None:

    try:
        with open(path, 'wb') as key_file:
            key_file.write(key)

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def key_deserialization(path: str) -> bytes:

    try:
        with open(path, "rb") as file:
            key = file.read()
        return key
    
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def encrypt(key: bytes, path: str, encrypted_path: str) -> None:

    text = read_binary_from_file(path)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv), backend=default_backend())

    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    padded_text = padder.update(text) + padder.finalize()
    cipher_text = iv + encryptor.update(padded_text) + encryptor.finalize()

    write_binary_to_file(encrypted_path, cipher_text)


def decrypt(key: bytes, encrypted_path: str, decrypted_path: str) -> None:

    encrypted_text = read_binary_from_file(encrypted_path)
    iv = encrypted_text[:16]
    cipher_text = encrypted_text[16:]
    cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv), backend=default_backend())

    decryptor = cipher.decryptor()
    decrypt_text = decryptor.update(cipher_text) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_dc_text = unpadder.update(decrypt_text) + unpadder.finalize()
    decrypt_text = unpadded_dc_text.decode('utf-8')

    write_text_to_file(decrypted_path, decrypt_text)


def save_generated_key(key: str, path: str) -> None:

        try:
            with open(path, 'wb') as key_file:
                key_file.write(key)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")