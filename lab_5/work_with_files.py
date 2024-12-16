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
        with open(file_path, 'a+', encoding='utf-8') as file:
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