import spacy

nlp = spacy.load("en_core_web_md")
tokens = nlp("Calderon-Zygmund operators are objects that are largely responsible for our understanding of a number of physical phenomena, from heat transfer to turbulence")

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)