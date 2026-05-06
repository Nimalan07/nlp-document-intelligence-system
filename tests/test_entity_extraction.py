from src.entity_extraction import EntityExtractor


def test_entity_extraction():
    extractor = EntityExtractor()

    text = "Invoice Number INV-2026-104 dated 12/04/2026"

    entities = extractor.extract_entities(text)

    assert isinstance(entities, dict)