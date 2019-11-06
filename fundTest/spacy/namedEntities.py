import spacy

nlp = spacy.load("en_core_web_md")
# doc = nlp("Calderon-Zygmund operators are objects that are largely responsible for our understanding of a number of physical phenomena, from heat transfer to turbulence")
doc = nlp("With this award, the Chemical Structure, Dynamics and Mechanisms (CSDM-A) Program of the Division of Chemistry is funding Professor Istvan Z. Kiss and his research group at Saint Louis University to study pattern formation of electrochemical reactions")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)