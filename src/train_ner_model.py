import random

import spacy

from spacy.training.example import Example

from prepare_training_data import training_data


class NERTrainer:
    def __init__(self):
        self.nlp = spacy.blank("en")

        if "ner" not in self.nlp.pipe_names:
            self.ner = self.nlp.add_pipe("ner")

        else:
            self.ner = self.nlp.get_pipe("ner")

    def add_labels(self):
        for _, annotations in training_data:
            for start, end, label in annotations["entities"]:
                self.ner.add_label(label)

    def train_model(self, iterations=20):
        self.add_labels()

        optimizer = self.nlp.begin_training()

        for _ in range(iterations):
            random.shuffle(training_data)

            losses = {}

            for text, annotations in training_data:
                doc = self.nlp.make_doc(text)

                example = Example.from_dict(
                    doc,
                    annotations
                )

                self.nlp.update(
                    [example],
                    drop=0.3,
                    losses=losses,
                    sgd=optimizer
                )

        self.nlp.to_disk(
            "models/spacy_ner_model"
        )

        print("Model training completed")


if __name__ == "__main__":
    trainer = NERTrainer()

    trainer.train_model()