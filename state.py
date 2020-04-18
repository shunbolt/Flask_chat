import Text_analysis

captions = {
    "S1": "Salut, moi c'est Lia, je suis un robot qui a été conçu dans le but de venir en aide aux élèves victimes de "
          "harcèlement à l'école. Je tiens tout d'abord à te féliciter de venir me parler !",
    "S2": "Avant de commencer, peux-tu me donner le nom de la personne qui subit le harcèlement ? Si c'est toi, "
          "tu peux me donner ton nom",
    "S3": "Oh, je vois, tu t'appelles FULL_NAME, c'est bien ça ?",
    "S4": "Ok, FIRST_NAME, j'ai besoin de savoir où se passent les faits. J'aurai besoin du nom de "
          "l'établissement et de la ville dans laquelle tu es situé.",
    "S5": "Ok, tu peux m'écrire ton prénom à nouveau ?",
    "S6": "Ton établissement est SCHOOL c'est ça ?",
    "S7": "Peux tu me dire dans quelle classe tu es ?",
    "S8": "Donc résumons, tu es à SCHOOL dans la classe CLASS. C'est bien ça FIRST_NAME ?",
    "S9": "Es-tu prêt à répondre à des questions plus précises ?",
    "S10": "Ok FIRST_NAME, quand est-ce que tes ennuis ont commencés ?",
    "S11": "C'est noté. On va te poser une petite série de questions: "
           "je t'invite à répondre librement à chacune d'entre"
           "elles. N'hésites pas à donner plus de détails si possible. Cela me permettra de mieux "
           "comprendre ta situation. Est-ce que ça va pour l'instant?",
    "S12": "Ok FIRST_NAME, est-ce que quelqu'un t'as frappé ? Si c'est le cas tu peux développer...",
    "S13": "Est-ce que tu te fais insulter ? N'hésites pas à développer si c'est le cas...",
    "S14": "Est-ce que que tu te fais harceler sur internet ou par sms ? "
           "Si oui peux-tu m'expliquer comment ils s'y prennent ?",
    "S15": "Est-ce qu'on te fait du chantage ?",
    "S16": "As-tu déjà parlé de ça autour de toi ?",
    "S17": "Est-ce que tu te sens mal dans ta classe ?",
    "S18": "Est-ce qu'un adulte s'en prend à toi à l'école ?",
    "S19": "Est-ce que tu veux me donner l'identité des harceleurs ?",
    "S20": "Acceptes-tu que nous envoyons le contenu de cette conversation aux personnes compétentes afin qu'elles "
           "soient prévenues de ce qu'il t'arrive ?",
    "S21": "Dans tous les cas, je te félicites pour ta conversation FIRST_NAME. Tu as eu raison de venir me parler et"
           "personne ne dira le contraire !"
           "C'est un grand pas en avant. Tu peux contacter le 3020 par téléphone si tu souhaites discuter de ce "
           "genre de problèmes avec un adulte qualifié qui sera tout aussi discret. "
           "Tu peux également te rapporcher de l'association Hugo"
           "qui saura t'accompagner et te guider pour ton problème. Bon courage ! ",
    "S22": "Peux-tu sélectionner ton école dans la liste au dessus s'il te plait"
}

name = ''
school = ''
classe = ''
school_list = []

def set_classe(tmp):
    global classe
    classe = tmp


def set_name(tmp):
    global name
    name = tmp

def set_school(tmp):
    global school
    school = tmp

def set_list(tmp):
    global school_list
    school_list = tmp


class State:
    def __init__(self, statenb, caption, possible_next_states, TA_function, input=True):
        self.statenb = statenb
        self.caption = caption
        self.possible_next_states = possible_next_states
        self.next = possible_next_states
        self.f = TA_function
        self.ans = None
        self.input = input


    def get_caption(self):
        return self.caption

    def get_next_state(self):
        # print(self.next)
        if not isinstance(self.possible_next_states, int):
            if Text_analysis.validate(self.ans):
                self.next = self.possible_next_states[0]
            else:
                self.next = self.possible_next_states[1]
        # print(self.next)

    # def get_ans(self):
    #    self.ans = input(">>> ")

    # def profiling(self):
    #    tmp = Text_analysis.validate(self.ans)
    #    if tmp:
    #        tmp = input("Peux-tu me raconter plus en détail ?\n >>> ")
    #    else:
    #        print("ok")

    def analyse(self):
        if self.f == "none":
            return
        elif self.f == "name":
            set_name(Text_analysis.retreive_name(self.ans))
        elif self.f == "school_ask":
            set_list(Text_analysis.find_school(self.ans))
            # print(schools)
            # tmp = input("entre le numéro de ton école dans cette liste s'il te plaît ")
            # set_school(schools[int(tmp)][1])
        elif self.f == "classe":
            set_classe(self.ans)
        # elif self.f == "profiling":
        #    self.profiling()

    def schools_to_dict_top3(self):
        dict = {}
        print(school_list)
        if school_list:
            print('Schools detected')
            dict = {
                "school1": {
                    "name": school_list[0][1],
                    "street": school_list[0][2],
                    "code": school_list[0][3],
                    "city": school_list[0][4]
                },
                "school2": {
                    "name": school_list[1][1],
                    "street": school_list[1][2],
                    "code": school_list[1][3],
                    "city": school_list[1][4]
                },
                "school3": {
                    "name": school_list[2][1],
                    "street": school_list[2][2],
                    "code": school_list[2][3],
                    "city": school_list[2][4]
                }
            }
        return dict


    def execute(self, user_json):
        # Process answer from user

        print(user_json.get('response'))
        if self.next != "END":
            if self.input:
                self.ans = user_json.get('response')
            self.analyse()
            self.get_next_state()
            # state_table[self.next - 1].execute()

        print(name)
        response_json = user_json

        # Collect parameters if found during analysis
        if name:
            response_json['name'] = name
        if school:
            response_json['school'] = school
        if classe:
            response_json['classe'] = classe
        response_json['dict_school'] = self.schools_to_dict_top3()

        print(response_json['dict_school'])
        # Prepares question to user
        tmp = state_table[self.next - 1].get_caption().replace("SCHOOL", response_json['school'])
        tmp = tmp.replace("FULL_NAME", response_json['name'])
        tmp = tmp.replace("FIRST_NAME", response_json['name'].split()[0])
        tmp = tmp.replace("CLASS", response_json['classe'])

        response_json['response'] = tmp

        # Update new state
        response_json['state'] = self.next
        return response_json



# S1 = State(statenb, caption, possible_next_states, TA_function)
S1 = State(1, captions.get("S1"), 2, "none", input=False)
S2 = State(2, captions.get("S2"), 3, "name")
S3 = State(3, captions.get("S3"), [4, 5], "none")
S4 = State(4, captions.get("S4"), 22, "school_ask")
S5 = State(5, captions.get("S5"), 3, "name")
S6 = State(6, captions.get("S6"), [7,4], "none")
S7 = State(7, captions.get("S7"), 8, "classe")
S8 = State(8, captions.get("S8"), [9, 7], "none")
S9 = State(9, captions.get("S9"), [10, 21], "none")
S10 = State(10, captions.get("S10"), 11, "none")
S11 = State(11, captions.get("S11"), 12, "none", input=False)
# Bloc de profiling
S12 = State(12, captions.get("S12"), 13, "none")
S13 = State(13, captions.get("S13"), 14, "none")
S14 = State(14, captions.get("S14"), 15, "none")
S15 = State(15, captions.get("S15"), 16, "none")
S16 = State(16, captions.get("S16"), 17, "none")
S17 = State(17, captions.get("S17"), 18, "none")
S18 = State(18, captions.get("S18"), 19, "none")
S19 = State(19, captions.get("S19"), 20, "none")
# Fin de bloc
S20 = State(20, captions.get("S20"), 21, "none")
S21 = State(21, captions.get("S21"), 21, "none", input=False)

S22 = State(22, captions.get("S22"), 6, "none",input=False)

state_table = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22]


def LIA_response(user_json):
    # Json Structure received :
    # {
    #    'response': user_input,
    #    'state': val_state,
    #    'name': name,
    #    'classe': classe,
    #    'school': school,
    # }
    return state_table[int(user_json.get('state')) - 1].execute(user_json)
