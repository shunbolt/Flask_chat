var messages = document.getElementById("messages");
var bouton = document.getElementById("send");
var textArea = document.getElementById("messageToBeSent")

var messageStringLia =
'<div class="d-flex justify-content-start mb-4">'+
'<div class="img_cont_msg">'+
'<img src = "static/images/logoLIA.png" class="rounded-circle user_img_msg">'+
'</div>'+
'<div class="msg_cotainer">'+
'XXXXX'+
'</div>'+
'</div>';

var messageStringUser =
'<div class="d-flex justify-content-end mb-4">'+
'<div class="msg_cotainer_send">'+
'XXXXX'+
'</div>'+
'<div class="img_cont_msg">'+
'<img src="https://upload.wikimedia.org/wikipedia/commons/f/f4/User_Avatar_2.png" class="rounded-circle user_img_msg">'+
'</div>'+
'</div>';

var loadingStringLia =
'<div class="d-flex justify-content-start mb-4" id = "loading">'+
'<div class="img_cont_msg">'+
'<img src = "static/images/logoLIA.png" class="rounded-circle user_img_msg">'+
'</div>'+
'<div class="msg_cotainer">'+
 'XXXXX '+
'</div>'+
'</div>';

/* bouton.addEventListener("click", add_message);

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
*/
function add_message_user(msg_user){
    var message = document.createElement("div");
    finalString = messageStringUser.replace("XXXXX", msg_user)
    message.innerHTML = finalString


    
    messages.appendChild(message)
    updateScroll()
}


function add_message_bot(msg_bot){
    var message = document.createElement("div");
    finalString = messageStringLia.replace("XXXXX", msg_bot)
    message.innerHTML = finalString

    
    messages.appendChild(message)
    updateScroll()
}

function add_message_bot_list(json){
    var message = document.createElement("div");

    console.log(JSON.stringify(json));

    // parsed_JSON = JSON.parse(JSON.stringify(json))

    msg_bot = "<ol>" +
    "<li>" + json.school1.name + ' - ' + json.school1.street +  ' - ' + json.school1.code + ' - ' + json.school1.city + "</li>" +
    "<li>" + json.school2.name + ' - ' + json.school2.street +  ' - ' + json.school2.code + ' - ' + json.school2.city + "</li>" +
    "<li>" + json.school3.name + ' - ' + json.school3.street +  ' - ' + json.school3.code + ' - ' + json.school3.city + "</li>" +
    "</ol>";
    finalString = messageStringLia.replace("XXXXX",msg_bot)
    message.innerHTML = finalString


    messages.appendChild(message)
    updateScroll()


}

function display_loading_bot(){
    var message = document.createElement("div");
    finalString = loadingStringLia.replace("XXXXX", '<img src = "static/images/loadingV2.png" >' )
    message.innerHTML = finalString

    messages.appendChild(message)
    updateScroll()
}

function remove_loading_bot(){
    var load_elem = document.getElementById('loading')
    if(load_elem != null){
        load_elem.parentNode.removeChild(load_elem)
    }
}

function updateScroll(){
    messages.scrollTop = messages.scrollHeight;
}

/*
function onTestChange() {
    var key = window.event.keyCode;

    // If the user has pressed enter
    if (key === 13) {
        add_message();
        window.event.preventDefault();
        return false;
    }
}
*/
      