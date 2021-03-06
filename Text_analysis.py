import spacy
import pandas as pd
from difflib import SequenceMatcher
import re
import unidecode


# ----------------------------boîte à outils ---------------------------------------------------------------------------

def similar(a, b):
    a = a.lower()
    b = b.lower()
    return SequenceMatcher(None, a, b).ratio()

# ----------------------------fonctions servant à localiser l'établissement scolaire------------------------------------

def find_school(message):
    schools = pd.read_csv('Logic/schools1.csv')
    from_location = find_city(schools, message)
    suspects = find_school_in_city(from_location, message)
    return suspects


def find_city(schools, message):
    df = schools.loc[schools["Nom_commune"] == 'x']
    schools = schools.dropna(subset=["Nom_commune"])
    for tokens in message.split():
        if len(tokens) > 2:
            token = tokens.capitalize()
            df = pd.concat([df, schools.loc[schools["Nom_commune"].str.contains(token)]])
    return df


def find_school_in_city(schools, message):
    top_match = []
    for iter, school in schools.iterrows():
        top_match.append((similar(school[1], message), school[1], school[4], school[7], school[9]))
    top_match = sorted(top_match, key=lambda x: x[0], reverse=True)[:3]
    return top_match

# ----------------------------fonctions servant à récupérer le nom de l'élève ------------------------------------------

"""def retreive_name(message):
    nlp = spacy.load('fr_core_news_sm')
    doc = nlp(message)
    name = ''
    for token in doc.ents:
        if token.label_ == "PER" or token.label_ == 'MISC':
            name += token.text
    return name.title()"""

def retreive_name(message):
    df = pd.read_csv("Logic/Prenoms.csv", usecols=[0])
    splitted = message.split(' ')
    if len(splitted)<3:
        return message.title()
    nlp = spacy.load('fr_core_news_sm')
    doc = nlp(message)
    name = ''
    if "m'appelle" in splitted:
        i = splitted.index("m'appelle")
        return ' '.join(splitted[i+1:]).title()
    if "suis" in splitted:
        i = splitted.index("suis")
        return ' '.join(splitted[i+1:]).title()
    if "est" in splitted:
        i = splitted.index("est")
        return ' '.join(splitted[i+1:]).title()
    if len(doc.ents) > 0:
        for token in doc.ents:
            if token.label_ == "PER" or token.label_ == 'MISC':
                name += token.text
        return name.title()
    for x in doc:
        if x.text.lower() in list(df.prenom):
            return x.text.title()
    else:
        return message.title()
# ----------------------------fonction servant à trouver la classe de l'élève ------------------------------------------

def find_class_name(message):
    message = unidecode.unidecode(message)
    a=0 
    
    for w in message.split(' '):
        for cl in ["sixieme", "cinquieme", "quatrieme", "troisieme", "seconde", "premiere", "terminale"]:
            if w.lower() == cl:
                return ' '.join(message.split(' ')[message.split(' ').index(w):])
            
    for c in message:
        if c.isnumeric():
            return message[a:]
        a += 1

# ----------------------------fonction de validation -------------------------------------------------------------------

def validate(message):
    message = message.lower()
    no_pattern = re.compile(r"non|pas|n'|ne")
    if re.search(no_pattern, message):
        print("false")
        return False
    else :
        return True
