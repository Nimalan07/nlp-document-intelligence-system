import json
from pathlib import Path


annotations_path = Path(
    "data/annotations/training_annotations/annotations"
)

training_data = []


for file_path in annotations_path.glob("*.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    text = ""

    entities = []

    cursor = 0

    for item in data["form"]:
        item_text = item["text"]

        label = item["label"]

        start = cursor

        end = start + len(item_text)

        text += item_text + " "

        if label != "other":
            entities.append(
                (
                    start,
                    end,
                    label.upper()
                )
            )

        cursor = len(text)

    training_data.append(
        (
            text,
            {
                "entities": entities
            }
        )
    )

print(training_data[:2])