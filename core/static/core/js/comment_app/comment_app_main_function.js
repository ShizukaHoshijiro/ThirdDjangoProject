/*

function edit_comment_event(event) {
    target = event.target;

    if (!target.matches(".comment_edit_button")) {
        return
    }

    var comment_id = target.parentNode.querySelector(".comment_id").value;
    var get_par_id = "?id=" + comment_id;
    var get_par_app_label = "&app_label=" + "comment_app";
    var get_par_model_name = "&model_name=" + "comment";

    addres = DOMAIN + "comments/edit/" + get_par_id + get_par_model_name + get_par_app_label ;

    var comment_get_form_xhr = new XMLHttpRequest();
    comment_get_form_xhr.open("GET", addres);
    comment_get_form_xhr.setRequestHeader("Content-Type", "application/json");
    comment_get_form_xhr.send();
    comment_get_form_xhr.onload = function () {
        if (this.status === 200) {
            var elem = document.createElement("div");
            elem.className = "alert_comment_form_outer";
            elem.innerHTML = this.responseText;
            document.body.appendChild(elem);
        }
    };

    comment_get_form_xhr.onerror = function () {
        alert("Error: " + this.status);
    };
}

document.addEventListener("click", edit_comment_event);

*/

var comment_button_class = ".comment_edit_button";
var comment_content_class = ".comment_content";
var comment_id_class = ".comment_id";

function comment_event(event) {

    var target = event.target;
    var address = DOMAIN + url_config["comment_app:edit_comment"];

    if(!target.matches(comment_button_class)){
        return
    }
    var comment_content = target.parentNode.querySelector(comment_content_class).textContent;
    var comment_id = target.parentNode.querySelector(comment_id_class).value;

    var csrf_token = jQuery.cookie("csrftoken");

    var message_body =
        "           <form class='alert_message_inner' method='post' action='" + address + "'>" +
        "                <input type='text' name='comment_content' required maxlength='80' placeholder='content' value='" + comment_content + "'>" +
        "                <input type='hidden' name='comment_id' value='" + comment_id + "'> " +
        "                <input class='message_submit_button' type='submit'>" +
        "                <input type='hidden' name='csrfmiddlewaretoken' value='" + csrf_token + "'>" +
        "                <input type='hidden' name='next' value='" + window.location + "'>" +
        "           </form>";
    // NotLikeThis


    var message = new Message(message_body);
    message.alert();

    // Внизу функция для отправки формы средством AJAX, в данный момент не используется, отправка формы обновляет стаинцу.
    /*
    document.addEventListener("click",post_xhr_func);

    function post_xhr_func(event) {
        target = event.target;
        if(!target.matches("message_submit_button")){
            return
        }



        var json_post_info = target.parentNode.serialize();

        var post_xhr = new XMLHttpRequest();
        post_xhr.open("POST",url_config["comment_app:edit_comment"]);
        post_xhr.setRequestHeader("X-CSRFToken", csrf_token);
        post_xhr.setRequestHeader("Content-Type", "application/json");
        post_xhr.send(json_post_info)

    }
    */

}

document.addEventListener("click",comment_event);