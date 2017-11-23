
var DOMAIN = "http://127.0.0.1:8000/"; // Must be change if will be new.

var url_config = {
    "comment_app:edit_comment":"comments/edit/",
    "rating_app:add_like":"rating/add/"
};


// Message class --- START ---
function Message(innerHTML){
    this.innerHTML = innerHTML;
    this.outer_class_name = "alert_message_outer"
}

Message.prototype.alert = function () {
    message = document.createElement("div");
    message.className = this.outer_class_name;
    message.innerHTML = this.innerHTML;
    document.body.appendChild(message)
};
Message.prototype.close = function () {
    document.body.removeChild(document.querySelector(this.outer_class_name))
};
// Message class --- END ---




/*

    message_body =

        "    <form class=\"alert_message_inner\" method=\"post\" action=\"" + url_config["comment_app:edit_comment"] + "\">\n" +
        "        <input type=\"text\" required maxlength=\"80\" placeholder=\"content\" value=\"" + + "\">\n" +
        "        <input type=\"submit\">\n" +
        "    </form>\n" +

    // Да, это пиздец.

 */


/* Some shit

--------------#1----------

class Animal {
  constructor(name){
    this.name = name;
  }
  walk(){
    alert(this.username);
  }
}

class Human extends Animal{
  constructor(name,surname){
    super(...arguments);
    this.username = name;
    this.surname = surname;
  }
  get fullname(){
    return `${this.username} ${this.surname}`
  }
  set fullname(newValue){
    [this.name, this.surname] = newValue.split(" ");
  }
}

wolf1 = new Human("haHAA","hahaHA");

alert(wolf1.fullname);
wolf1.username = "I am ";
wolf1.surname = "Batman";
alert(wolf1.fullname);
alert(wolf1.name);


-------------#2------------

var ms = prompt("Give a time.");

var promise = new Promise(promise_function);

    function promise_function(resolve,reject) {
        setTimeout(function(){resolve("Fuck you. ")},ms);
    }

promise.then(promise_result,promise_error);

    function promise_result(result) {
        alert(result + "No, wrong answer, fuck you, kozhewnik")
    }

    function promise_error(error) {
        alert(error)
    }

*/