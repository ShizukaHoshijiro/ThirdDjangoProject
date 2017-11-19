
var DOMAIN = "http://127.0.0.1:8000/"; // Must be change if will be new.

var rating_request_body = {
  "model_name":"topic",
  "object_id":null,
  "app_label":"core"
};

function like_event(event){
    event.stopImmediatePropagation();
    var target = event.target;

    if (!target.matches(".like_form .btn")){
        return
    }

    else {
        var obj_id = target.parentNode.querySelector("[name=object_id]").value;
        var csrf_token = target.parentNode.querySelector("[name=csrfmiddlewaretoken]").value;

        var rating_request_body_upd = rating_request_body;

        rating_request_body_upd.object_id = obj_id;
        var rating_request_body_json = JSON.stringify(rating_request_body_upd)
        // rating_request_body_upd["X-CSRFToken"] = csrf_token;
        var adress = DOMAIN + "rating/add/";

        var rating_xhr = new XMLHttpRequest();
        rating_xhr.open("POST",adress);
        rating_xhr.setRequestHeader("X-CSRFToken", csrf_token);
        rating_xhr.send(rating_request_body_json);

    }
}

document.addEventListener("click",like_event);

