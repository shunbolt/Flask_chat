# Libraries imports
from flask import Flask, render_template
from flask_socketio import SocketIO
# from chat import chatbot
import Text_analysis
import time

# Author of the code
auth = "Tran Raphaël"

# Define flask application
app = Flask(__name__)

# Secret key to secure transactions
app.config['SECRET_KEY'] = 'a7849f59f9eb4d40cd48e3c4c4e6f2f1'
# Define Socket object
socketio = SocketIO(app)


# Default route
@app.route('/')
def chat():
    return render_template('chat.html')

flag = True
json_input = ''

def HTMLBot_response(answer):
    time.sleep(3)
    socketio.emit('event_chat_output', {
        "bot_message": answer,
        "user_message": ""
    })


def HTMLUser_input():
    global flag
    global json_input

    flag = True
    json_input = ''

    while (flag):
        @socketio.on('event_chat_input')
        def read_input(json):
            global flag
            global json_input


            json_input = json['user_message']
            flag = False



    return json_input


# Event handler with socket.on decorator
# @socketio.on('event_chat_input')
# def handler_event(json, methods=['GET', 'POST']):
#    response = chatbot(json.get('user_message'))
# print('received the event: '+ str(json))
#    json['bot_message'] = response
#    time.sleep(3)
#    socketio.emit('event_chat_output', json)


# Partie Code State.py de Paul

name = 'name surname'
school = ''
classe = ''


def set_classe(tmp):
    global classe
    classe = tmp


def set_name(tmp):
    global name
    name = tmp


def set_school(tmp):
    global school
    school = tmp


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

    def get_ans(self):
        # self.ans = input(">>> ")
        self.ans = HTMLUser_input()

    def profiling(self):
        tmp = Text_analysis.validate(self.ans)
        if tmp:
            tmp = input("Peux-tu me raconter plus en détail ?\n >>> ")
        else:
            print("ok")

    def analyse(self):
        if self.f == "none":
            return
        elif self.f == "name":
            set_name(Text_analysis.retreive_name(self.ans))
        elif self.f == "school":
            schools = Text_analysis.find_school(self.ans)
            print(schools)
            tmp = input("entre le numéro de ton école dans cette liste s'il te plaît ")
            set_school(schools[int(tmp)][1])
        elif self.f == "classe":
            set_classe(self.ans)
        elif self.f == "profiling":
            self.profiling()

    def execute(self):
        tmp = self.get_caption().replace("SCHOOL", school)
        tmp = tmp.replace("FULL_NAME", name)
        tmp = tmp.replace("FIRST_NAME", name.split()[0])
        tmp = tmp.replace("CLASS", classe)

        HTMLBot_response(tmp)
        # print(tmp)

        if self.next != "END":
            if self.input:
                self.get_ans()
            self.analyse()
            self.get_next_state()
            state_table[self.next - 1].execute()


# S1 = State(statenb, caption, possible_next_states, TA_function)

captions = {
    "S1": "Salut, moi c'est Lia, je suis un robot qui a été conçu dans le but de venir en aide aux élèves victimes de "
          "harcèlement à l'école. Je tiens tout d'abord à te féliciter de venir me parler !",
    "S2": "Avant de commencer, peux-tu me donner le nom de la personne qui subit le harcèlement ? Si c'est toi, "
          "tu peux me donner ton nom. ",
    "S3": "Oh, je vois, tu t'appelles FULL_NAME, c'est bien ça ?",
    "S4": "Ok, FIRST_NAME, dans quel établissement scolaire se passent les faits ? J'aurai besoin du nom de "
          "l'établissement et de la ville dans laquelle il se situe",
    "S5": "ok, tu peux m'écrire ton prénom à nouveau ?",
    "S6": "Peux-tu me confirmer que ton établissement est SCHOOL ?",
    "S7": "Peux tu me dire dans quelle classe tu es ?",
    "S8": "donc résumons, tu es à SCHOOL dans la classe CLASS. C'est cela FIRST_NAME ?",
    "S9": "Es-tu prêt à répondre à des questions plus précises ?",
    "S10": "ok FIRST_NAME, quand es-ce que tes ennuis ont commencés ?",
    "S11": "on va te poser une petite série de questions, je t'invite à répondre par oui ou non à chacune d'entre "
           "elles. On pourra aussi te demander plus de détails.",
    "S12": "Est-ce que quelqu'un t'a frappé ?",
    "S13": "Est-ce que tu te fais insulter ?",
    "S14": "Est-ce que que tu te fais harceler sur internet ou par sms ?",
    "S15": "Est-ce qu'on te fait chanter ?",
    "S16": "En as-tu déjà parlé autour de toi ?",
    "S17": "Est-ce que tu te sens mal dans ta classe ?",
    "S18": "Est-ce qu'un adulte s'en prend à toi à l'école ?",
    "S19": "Est-ce que tu veux me donner l'identité des harceleurs ?",
    "S20": "Acceptes-tu que nous envoyons le contenu de cette conversation aux personnes compétentes afin qu'elles "
           "soient prévenues de ce qu'il t'arrive ?",
    "S21": "Dans tous les cas, je te remercie pour cette conversation FIRST_NAME. Tu as eu raison de venir me parler, "
           "c'est déjà un grand pas en avant. Tu peux contacter le 3020 par téléphone si tu souhaites discuter de ce "
           "genre de problèmes avec un humain qualifié et discret. Bonne continuation ! "

}

S1 = State(1, captions.get("S1"), 2, "none", input=False)
S2 = State(2, captions.get("S2"), 3, "name")
S3 = State(3, captions.get("S3"), [4, 5], "none")
S4 = State(4, captions.get("S4"), 6, "school")
S5 = State(5, captions.get("S5"), 3, "name")
S6 = State(6, captions.get("S6"), 7, "none")
S7 = State(7, captions.get("S7"), 8, "classe")
S8 = State(8, captions.get("S8"), [9, 7], "none")
S9 = State(9, captions.get("S9"), [10, 1], "none")
S10 = State(10, captions.get("S10"), 11, "none")
S11 = State(11, captions.get("S11"), 12, "none", input=False)
S12 = State(12, captions.get("S12"), 13, "profiling")
S13 = State(13, captions.get("S13"), 14, "profiling")
S14 = State(14, captions.get("S14"), 15, "profiling")
S15 = State(15, captions.get("S15"), 16, "profiling")
S16 = State(16, captions.get("S16"), 17, "profiling")
S17 = State(17, captions.get("S17"), 18, "profiling")
S18 = State(18, captions.get("S18"), 19, "profiling")
S19 = State(19, captions.get("S19"), 20, "profiling")
S20 = State(20, captions.get("S20"), 21, "none")
S21 = State(21, captions.get("S21"), "END", "none", input=False)

state_table = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21]


@socketio.on('event_chat_connect')
def state_start(methods=['GET', 'POST']):
    S1.execute()


######## End of Paul's code ######

# Helps easy debug by running python from command line
if (__name__ == '__main__'):
    app.run(debug=True)
