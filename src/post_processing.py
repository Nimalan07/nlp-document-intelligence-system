import re


class PostProcessor:
    def __init__(self):
        pass

    def validate_date(self, value):
        pattern = r"\b\d{2}[/-]\d{2}[/-]\d{4}\b"

        if re.match(pattern, value):
            return value

        return None

    def validate_currency(self, value):
        pattern = r"[\$₹€]\s?\d+(?:,\d{3})*(?:\.\d{2})?"

        if re.match(pattern, value):
            return value

        return None

    def process_entities(self, entities):
        processed_entities = {}

        for key, value in entities.items():
            if "date" in key.lower():
                processed_entities[key] = self.validate_date(value)

            elif "amount" in key.lower():
                processed_entities[key] = self.validate_currency(value)

            else:
                processed_entities[key] = value

        return processed_entities