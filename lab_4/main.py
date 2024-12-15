import argparse
from work_with_files import *
import symmetric
import assymetric

def menu():

    parser = argparse.ArgumentParser()
    settings = read_json_from_file("settings.json")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Generate symmetric and asymmetric keys')
    group.add_argument('-enc', '--encryption', help='Encrypt a file using symmetric key')
    group.add_argument('-dec', '--decryption', help='Decrypt a file using symmetric key')
    group.add_argument('-enc_sym', '--encryption_symmetric', help='Encrypt sym key using asym encryption')
    group.add_argument('-dec_sym', '--decryption_symmetric', help='Decrypt sym key using asym decryption')


    args = parser.parse_args()

    match args:
        case args if args.generation:
            key_length = int(input(
                    "Enter the key length in bits, in the range [128, 192, 256]: "
                ))
            print(f"Your key length: {key_length} ")

            assym_keys = assymetric.generate_keys()
            assymetric.serialization_private(assym_keys["private_key"], settings["secret_key_path"])
            assymetric.serialization_public(assym_keys["public_key"], settings["public_key_path"])
            key_serialization= symmetric.generation_key(key_length)
            symmetric.key_serialization(key_serialization, settings["symmetric_key_path"])

        case args if args.encryption:
            symmetric_key = symmetric.key_deserialization(settings["symmetric_key_path"])
            symmetric.encrypt(symmetric_key, settings["initial_file_path"], settings["encrypted_file_path"])

        case args if args.decryption:
            symmetric_key = symmetric.key_deserialization(settings["symmetric_key_path"])
            symmetric.decrypt(symmetric_key, settings["encrypted_file_path"], settings["decrypted_file_path"])

        case args if args.encryption_symmetric:
            symmetric_key = symmetric.key_deserialization(settings["symmetric_key_path"])
            public_key = assymetric.public_key_deserialization(settings["public_key_path"])

            encrypted_symmetric_key = assymetric.encrypt(public_key, symmetric_key)
            write_binary_to_file(settings["encrypted_key_path"], encrypted_symmetric_key)

        case args if args.decryption_symmetric:
            private_key = assymetric.private_key_deserialization(settings["secret_key_path"])
            encrypted_symmetric_key = read_binary_from_file(settings["encrypted_key_path"])

            decrypted_symmetric_key = assymetric.decrypt(private_key, encrypted_symmetric_key)
            write_binary_to_file(settings["decrypted_key_path"], decrypted_symmetric_key)


if __name__ == "__main__":
    menu()