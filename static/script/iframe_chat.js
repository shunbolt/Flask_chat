var messages = document.getElementById("messages");
var bouton = document.getElementById("send");
var textArea = document.getElementById("messageToBeSent")

var messageStringLia =
'<div class="d-flex justify-content-start mb-4">'+
'<div class="img_cont_msg">'+
'<img src="images/logoLIA.png" class="rounded-circle user_img_msg">'+
'</div>'+
'<div class="msg_container">'+
'I am looking for your next templates'+
'</div>'+
'</div>';

var messageStringUser =
'<div class="d-flex justify-content-end mb-4">'+
'<div class="msg_container_send">'+
'XXXXX'+
'</div>'+
'<div class="img_cont_msg">'+
'<img src="images/user_avatar.png" class="rounded-circle user_img_msg">'+
'</div>'+
'</div>';


bouton.addEventListener("click", add_message);

function add_message() {

	if (textArea.value == '') return;


	var messageContent = textArea.value;

    var message = document.createElement("div");
    finalString = messageStringUser.replace("XXXXX", messageContent)
    message.innerHTML = finalString


    messages.appendChild(message)
    textArea.value='';
    updateScroll()
}

function updateScroll(){
    messages.scrollTop = messages.scrollHeight;
}

function onTestChange() {
    var key = window.event.keyCode;

    // If the user has pressed enter
    if (key === 13) {
        add_message();
        window.event.preventDefault();
        return false;
    }
}
