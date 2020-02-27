import spacy

nlp = spacy.load("en_core_web_lg")
doc1 = nlp("king")
doc2 = nlp("man")

doc3 = nlp("queen")
doc4 = nlp("woman")

tl = []

sim1 = doc1.similarity(doc2)
sim2 = doc2.similarity(doc3)

print(sim1, sim2)
