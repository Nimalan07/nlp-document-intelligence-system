import random

import spacy

from spacy.training.example import Example


TRAIN_DATA = [
    (
        "Invoice Number INV-2026-104 dated 12/04/2026",
        {
            "entities": [
                (15, 27, "INVOICE_ID"),
                (34, 44, "DATE")
            ]
        }
    ),
    (
        "Total amount is $12500",
        {
            "entities": [
                (16, 22, "AMOUNT")
            ]
        }
    ),
    (
        "Organization ABC Technologies",
        {
            "entities": [
                (13, 29, "ORG")
            ]
        }
    )
]


class NERTrainer:
    def __init__(self):
        self.nlp = spacy.blank("en")

        if "ner" not in self.nlp.pipe_names:
            self.ner = self.nlp.add_pipe("ner")

        else:
            self.ner = self.nlp.get_pipe("ner")

    def add_labels(self):
        for _, annotations in TRAIN_DATA:
            for start, end, label in annotations["entities"]:
                self.ner.add_label(label)

    def train_model(self, iterations=30):
        self.add_labels()

        optimizer = self.nlp.begin_training()

        for _ in range(iterations):
            random.shuffle(TRAIN_DATA)

            losses = {}

            for text, annotations in TRAIN_DATA:
                doc = self.nlp.make_doc(text)

                example = Example.from_dict(doc, annotations)

                self.nlp.update(
                    [example],
                    drop=0.3,
                    losses=losses,
                    sgd=optimizer
                )

        self.nlp.to_disk("models/spacy_ner_model")


if __name__ == "__main__":
    trainer = NERTrainer()
    trainer.train_model()