import spacy

nlp = spacy.load("pt_core_news_sm")

def preprocess_nlp(text: str) -> dict:
    doc = nlp(text.lower())

    lemmas = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return {
        "processed_text": " ".join(lemmas),
        "lemmas": lemmas
    }
