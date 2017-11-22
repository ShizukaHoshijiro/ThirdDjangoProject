
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

