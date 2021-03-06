import json
from spacy.matcher import Matcher
from spacy.lang.de import German

with open("exercises/de/iphone.json") as f:
    TEXTS = json.loads(f.read())

nlp = German()
matcher = Matcher(nlp.vocab)
pattern1 = [{"LOWER": "iphone"}, {"LOWER": "x"}]
pattern2 = [{"LOWER": "iphone"}, {"IS_DIGIT": True}]
matcher.add("GADGET", None, pattern1, pattern2)

TRAINING_DATA = []

# Erstelle ein Doc-Objekt für jeden Text aus TEXTS
for ____ in ____:
    # Wende den Matcher an und erstelle eine Liste der gefundenen Spans
    spans = [____[____:____] for match_id, start, end in matcher(doc)]
    # Erstelle (Start-Buchstabe, End-Buchstabe, Label) Tuples für die gefundenen Spans
    entities = [(span.start_char, span.end_char, "GADGET") for span in spans]
    # Formatiere die Resultate als (doc.text, entities) Tuple
    training_example = (____, {"entities": ____})
    # Füge das Beispiel zur Liste TRAINING_DATA hinzu
    ____.____(____)

print(*TRAINING_DATA, sep="\n")
