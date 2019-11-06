import spacy

nlp = spacy.load("en_core_web_sm")
doc  = nlp("Calderon-Zygmund operators are objects that are largely responsible for our understanding of a number of physical phenomena, from heat transfer to turbulence")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_,token.is_alpha, token.is_stop)