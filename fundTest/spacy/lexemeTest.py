import spacy

nlp = spacy.load("en_core_web_md")
doc = nlp("Calderon-Zygmund operators are objects that are largely responsible for our understanding of a number of physical phenomena, from heat transfer to turbulence")
lexeme = doc.vocab["Calderon"]
lexeme2 = doc.vocab["operators"]
print(lexeme.similarity(lexeme2)) 
# -0.10432234