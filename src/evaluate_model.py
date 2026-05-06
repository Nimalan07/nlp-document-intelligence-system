import spacy

from sklearn.metrics import classification_report


TEST_DATA = [
    (
        "Invoice Number INV-2026-104 dated 12/04/2026",
        ["INVOICE_ID", "DATE"]
    ),
    (
        "Total amount is $12500",
        ["AMOUNT"]
    ),
    (
        "Organization ABC Technologies",
        ["ORG"]
    )
]


class ModelEvaluator:
    def __init__(self, model_path="models/spacy_ner_model"):
        self.nlp = spacy.load(model_path)

    def evaluate(self):
        y_true = []
        y_pred = []

        for text, labels in TEST_DATA:
            doc = self.nlp(text)

            predicted_labels = [ent.label_ for ent in doc.ents]

            y_true.extend(labels)
            y_pred.extend(predicted_labels)

        report = classification_report(
            y_true,
            y_pred,
            zero_division=0
        )

        return report


if __name__ == "__main__":
    evaluator = ModelEvaluator()

    result = evaluator.evaluate()

    print(result)