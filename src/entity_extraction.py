import spacy


class EntityExtractor:
    def __init__(self, model_path="models/spacy_ner_model"):
        self.nlp = spacy.load(model_path)

    def extract_entities(self, text):
        doc = self.nlp(text)

        entities = {}

        for ent in doc.ents:
            entities[ent.label_] = ent.text

        return entities