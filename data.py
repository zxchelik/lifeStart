import json


class MyData:
    _instance = None

    def __init__(self):
        data = read_json()
        self.message = self.Message(data['message'])
        self.question = [
            (q["message"], [(ans[0], ans[1]) for ans in q["answers"]])
            for q in data["questions"]]


    class Message:
        def __init__(self, message):
            self.menu = message['menu']
            self.digest = message['digest']
            self.faq = message['faq']
            self.sections = message['sections']
            self.call_menu_test = message["call_menu_test"]
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

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


def read_json():
    file_path = "data.json"
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


DATA = MyData.instance()
