from constants.file_paths import FilePath
from datetime import datetime

class FileIO:

    @classmethod
    def write_token_to_file(cls, username:str, token:str):
        file_data = f"{datetime.now()}, {username}, {str(token[0])}\n"
        with open(FilePath.token_file, "a+t", encoding="utf-8")as token_csv:
            token_csv.write(file_data)