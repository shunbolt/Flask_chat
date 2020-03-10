import spacy
import pandas as pd
from difflib import SequenceMatcher
import re


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

def retreive_name(message):
    nlp = spacy.load('fr_core_news_sm')
    doc = nlp(message)
    name = ''
    for token in doc.ents:
        if token.label_ == "PER" or token.label_ == 'MISC':
            name += token.text
    return name.title()


# ----------------------------fonction de validation -------------------------------------------------------------------

def validate(message):
    message = message.lower()
    no_pattern = re.compile(r"non|pas|n'|ne")
    if re.search(no_pattern, message):
        print("false")
        return False
    else :
        return True
