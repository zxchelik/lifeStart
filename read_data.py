import json


def read_data():
    file_path = "data.json"
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data
