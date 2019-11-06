import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("this research also has implications for battery and energy technologies")
doc1 = nlp("Recently, these operators have found application in big data analysis")
doc2 = nlp("One possible application of such low regularity theory is that by the action of Calderon-Zygmund operators on a set in a space of a very high dimension")
doc3 = nlp("Our other recent observation is that well-studied problems for such an operator can be dualized to provide new information for analysis on the hypercube")
doc4 = nlp("Other challenges for mobile VR/AR are limited battery life and increased heat dissipation")
doc5 = nlp("The main focus of this project is the study of the effects of disorder on quantum systems.")

for token in doc:
    if token.dep_ == "ROOT" or token.dep_ == "nsubj" or token.dep_ == "dobj" or token.dep_ == "prep":
        print(token.text, token.dep_)
print("-------------------------")
for token in doc1:
    if token.dep_ == "ROOT" or token.dep_ == "nsubj" or token.dep_ == "dobj" or token.dep_ == "prep":
        print(token.text, token.dep_)
print("-------------------------")
for token in doc2:
    if token.dep_ == "ROOT" or token.dep_ == "nsubj" or token.dep_ == "dobj" or token.dep_ == "prep":
        print(token.text, token.dep_)
print("-------------------------")
for token in doc3:
    if token.dep_ == "ROOT" or token.dep_ == "nsubj" or token.dep_ == "dobj" or token.dep_ == "prep":
        print(token.text, token.dep_)
print("-------------------------")
for token in doc4:
    # if token.dep_ == "ROOT" or token.dep_ == "nsubj" or token.dep_ == "dobj" or token.dep_ == "prep":
    print(token.text, token.dep_)
print("-------------------------")
for token in doc5:
    if token.dep_ == "ROOT" or token.dep_ == "nsubj" or token.dep_ == "dobj" or token.dep_ == "prep":
        print(token.text, token.dep_)