import spacy

nlp = spacy.load("en_core_web_md")
apple = nlp.vocab['apple']
orange = nlp.vocab['orange']

print(nlp.vocab.strings["apple"])
