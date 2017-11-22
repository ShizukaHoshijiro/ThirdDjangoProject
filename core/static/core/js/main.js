
var DOMAIN = "http://127.0.0.1:8000/"; // Must be change if will be new.




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