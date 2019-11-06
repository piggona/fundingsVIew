import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("this research also has implications for battery and energy technologies")
for ent in doc.ents:
    print(ent.text, ent.label)