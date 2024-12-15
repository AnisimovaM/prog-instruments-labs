
import json


def read_text_from_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error has occurred: {e}")


def write_text_to_file(file_path: str, text: str) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print("The information is successfully saved to the file.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def read_json_from_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Error while decoding JSON: {e}")
    except Exception as e:
        print(f"An error has occurred: {e}")


def write_json_to_file(file_path: str, data: dict, indent: int = 4) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=indent)
        print("Data was successfully written to a file in JSON.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def read_binary_from_file(file_path: str) -> bytes:
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        print(f"\033[97;41mFile not found: {e}\033[0m")
    except Exception as e:
        print(f"\033[97;41mAn error occurred while reading the file: {e}\033[0m")


def write_binary_to_file(file_path: str, bytes_text: bytes) -> None:
    try:
        with open(file_path, 'wb') as file:
            file.write(bytes_text)
        print("\033[91;107mThe binary data has been successfully saved to the file.\033[0m")
    except FileNotFoundError as e:
        print(f"\033[97;41mFile not found: {e}\033[0m")
    except Exception as e:
        print(f"\033[97;41mAn error occurred while writing the binary data to the file: {e}\033[0m")