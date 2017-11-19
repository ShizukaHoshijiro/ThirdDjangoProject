
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
        var rating_request_body_json = JSON.stringify(rating_request_body_upd);

        var adress = DOMAIN + "rating/add/";

        var rating_xhr = new XMLHttpRequest();
        rating_xhr.open("POST",adress);
        rating_xhr.setRequestHeader("X-CSRFToken", csrf_token);
        rating_xhr.setRequestHeader("Content-Type", "application/json");
        rating_xhr.send(rating_request_body_json);

        rating_xhr.onload = rating_xhr.onerror = function () {
            if (this.status === 200) {
                var response_data = JSON.parse(this.responseText);
                // this.responseText сырой текст ответа
                target.value = response_data.likes;

            }
            else {
                alert("Error: "+this.status)
            }
        };

    }
}

document.addEventListener("click",like_event);

