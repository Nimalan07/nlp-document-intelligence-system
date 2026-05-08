class KeyValueExtractor:
    def __init__(self):
        pass

    def extract_pairs(self, entities):
        questions = entities.get("QUESTION",[])
        answers = entities.get(  "ANSWER", [])
        structured_data = {}
        for question, answer in zip( questions,answers):
            key = question["text"]
            value = answer["text"]
            structured_data[key] = value
        return structured_data