import re


class TextPreprocessor:
    def __init__(self):
        pass

    def clean_text(self, text):
        text = text.lower()

        text = re.sub(r"\n", " ", text)

        text = re.sub(r"\t", " ", text)

        text = re.sub(
            r"[^a-zA-Z0-9:/.$%\-\s]",
            "",
            text
        )

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def tokenize_text(self, text):
        tokens = text.split()

        return tokens