# Libraries imports
from flask import Flask, render_template, url_for
from flask_socketio import SocketIO
from chat import chatbot

# Author of the code
auth = "Tran Raphaël"

# Define flast application
app = Flask(__name__)

# Secret key to secure transactions
app.config['SECRET_KEY'] = 'a7849f59f9eb4d40cd48e3c4c4e6f2f1'
#Define Socket object
socketio = SocketIO(app)

# Default route
@app.route('/')
def chat():
    return render_template('chat.html')

# function that triggers on callback when an event is received
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

# Event handler with socket.on decorator
@socketio.on('event_chat_input')
def handler_event(json, methods=['GET', 'POST']):
	response = chatbot(json.get('user_message'))
	# print('received the event: '+ str(json))
	json['bot_message'] = response
	socketio.emit('event_chat_output', json, callback=messageReceived)

# Helps easy debug by running python from command line
if(__name__ == '__main__'):
	app.run(debug=True)