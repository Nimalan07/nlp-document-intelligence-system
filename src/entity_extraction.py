import spacy


class EntityExtractor:
    def __init__(
        self,
        model_path="models/spacy_ner_model"
    ):
        self.nlp = spacy.load(model_path)

    def extract_entities(self, text):
        doc = self.nlp(text)

        entities = {}

        for ent in doc.ents:
            if ent.label_ not in entities:
                entities[ent.label_] = []

            entities[ent.label_].append(
                {
                    "text": ent.text,
                    "start": ent.start_char,
                    "end": ent.end_char
                }
            )

        return entities