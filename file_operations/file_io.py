from os import sep
import json


class FileIO:
    '''
    Class to handle file IO
    '''

    @staticmethod
    def read_file(dir, file_name, ext):
        '''
        Function to read a file except .json.
        '''
        try:
            with open(f"{dir}{sep}{file_name}.{ext}", "rt", encoding="utf-8") as file:
                return file.read()
        except Exception as ex:
            print(f"Error: {ex}")

    @staticmethod
    def write_file(dir, file_name, ext, data):
        '''
        Function to write to a file.
        '''
        try:
            file_name, ext = file_name.lower(), ext.lower()
        except Exception as ex:
            print(f"Error: {ex}")


        if ext is "json":
            data = json.dumps(data)
            try:
                with open(f"{dir}{sep}{file_name}.{ext}", "w+t", encoding="utf-8") as file:
                    file.write(data)
            except Exception as ex:
                print(f"Error: {ex}")
        elif ext is "txt":
            try:
                with open(f"{dir}{sep}{file_name}.{ext}", "w+t", encoding="utf-8") as file:
                    file.write(data)
            except Exception as ex:
                print(f"Error: {ex}")
        elif ext is "csv":
            try:
                with open(f"{dir}{sep}{file_name}.{ext}", "a+t", encoding="utf-8") as file:
                    file.write(data)
            except Exception as ex:
                print(f"Error: {ex}")
        elif ext is "xlsx":
            try:
                with open(f"{dir}{sep}{file_name}.{ext}", "a+t", encoding="utf-8") as file:
                    file.write(data)
            except Exception as ex:
                print(f"Error: {ex}")

    @staticmethod
    def read_json(dir, file_name):
        '''
        Function to read a json file.
        '''
        try:
            with open(f"{dir}{sep}{file_name}.json", "rt", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as ex:
            print(f"Error: {ex}")

        return data


    