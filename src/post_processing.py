class PostProcessor:
    def __init__(self):
        pass

    def clean_entities(self, entities):
        cleaned_entities = {}

        for label, values in entities.items():
            cleaned_values = []

            for value in values:
                text = value["text"].strip()

                if len(text) < 3:
                    continue

                if len(text) > 200:
                    continue

                entity = {
                    "text": text,
                    "start": value["start"],
                    "end": value["end"]
                }

                if entity not in cleaned_values:
                    cleaned_values.append(
                        entity
                    )

            cleaned_entities[label] = (
                cleaned_values
            )

        return cleaned_entities