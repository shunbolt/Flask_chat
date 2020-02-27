import Text_analysis

captions = {
    "M1": "Salut, moi c'est Lia, je suis un robot qui a été conçu dans le but de venir en aide aux élèves victimes de harcèlement à l'école. Je tiens tout d'abord à te féliciter de venir me parler !",
    "M2": "Avant de commencer, peux-tu me donner le nom de la personne qui subit le harcèlement ? Si c'est toi, tu peux me donner ton nom. ",
    "M3": "Oh, je vois tu t'appelles ***, c'est bien ça ?",
    "M4": "Ok, ***, dans quel établissement scolaire se passent les faits ? Jaurai besoin du nom de l'établissement et de la ville dans laquelle il se situe",
    "M4bis":"ok, tu peux m'écrire ton prénom à nouveau ?",
    "M5": "Peux-tu me confirmer l'établissement ?",
    "M6": "Maintenant, j'aimerais que tu m'expliques la situation, est-ce que tu peux me donner un peu plus de détails s'il te plait ?"
}

state = "M1"
name = ''
texte = ''
school = ''

def next_state():
    global state, texte, school
    send_message()

    #print(state)

    if state == "M1":
        state = "M2"

    elif state == "M2":
        in_ = input(">>> ")
        set_name(Text_analysis.retreive_name(in_))
        state = "M3"

    elif state == "M3":
        in_ = input(">>> ")
        if Text_analysis.validate(in_):
            state = "M4"
        else :
            state = "M4bis"

    elif state == "M4":
        in_ = input(">>> ")
        school = Text_analysis.find_school(in_)
        print(school)
        state = "M5"

    elif state == "M4bis":
        in_ = input(">>> ")
        set_name(Text_analysis.retreive_name(in_))
        state = "M3"

    elif state == "M5":
        in_ = input(">>> ")
        if Text_analysis.validate(in_):
            state = "M6"
        else:
            state = "M6bis"

    elif state == "M6":
        texte = input(">>> ")
        print("nom = ", name)
        print("établissement = ", school)
        print("déclaration = ", texte)
        return

    next_state()



def set_name(tmp):
    global name
    name = tmp

def send_message():
    message = states[state]
    if "***" in message:
        message = message.replace("***", name.split()[0])
    print(message)

def print_states():
    print(state)
    next_state()
    print(state)
