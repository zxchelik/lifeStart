import json


class my_data:
    def __init__(self, data):
        self.message = self.Message(data['message'])
        self.question = self.Question(data['question'])

    class Message:
        def __init__(self, message):
            self.menu = message['menu']
            self.digest = message['digest']
            self.result = self.Result(message['result'])
            self.build = self.Build(message['build'])

        class Result:
            def __init__(self, result):
                self.result1 = result['result1']
                self.result2 = result['result2']

        class Build:
            def __init__(self, build):
                self.build1 = build['build1']
                self.build2 = build['build2']

    class Question:
        def __init__(self, question):
            self.start = question['start']
            self.question1 = question['question1']
            self.question2 = question['question2']


def read_data():
    print("СЧИТЫВАНИЕ")
    file_path = "data.json"
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


DATA = my_data(read_data())