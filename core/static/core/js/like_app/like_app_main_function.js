
/*

    Documentations/Документация
    like_app_main_function.js - объявляет функциюю добавляющую обработчик для кнопок лайков.
    Параметры:
        target_selecter - CSS селектор кнопки для определённого класса объектов(комментарии, темы).
        request_body - Тело POST запроса, рендерится в JSON, содержит имя модели, имя приложения, id объекта.
    Использование:
        В начале добавляем в документ like_app_main_function.js(тем самым объявляем addEventListenTo()),
        после, добавляем другие скрипы вызывающие addEventListenTo() с нужными параметрами.
        В данном проекте это скрипты лежащие в calls/...

 */


(function(){ // Обёртка в анонимную функцию чтобы не захламлять глобальное окружение.

function addEventListenTo(target_selecter,request_body) {

    function like_event(event){
        var target = event.target;

        if (!target.matches(target_selecter)){
          // Если глобальный обработчик зафиксировал клик не по нужной кнопке(элементу подходящему под target_selecter).
          // Тогда возвращаем return, событие не обрабатывается и всплывает дальше
            return
        }

        else {
            // event.stopPropagation(); // Останавливаем всплытие если нужно.
            var obj_id = target.parentNode.querySelector("[name=object_id]").value;
            var csrf_token = target.parentNode.querySelector("[name=csrfmiddlewaretoken]").value;

            request_body.object_id = obj_id; // Добаляем object_id к request_body_upd.
            var request_body_json = JSON.stringify(request_body); // Преобразуем в JSON

            var adress = DOMAIN + "rating/add/";

            var rating_xhr = new XMLHttpRequest();
            rating_xhr.open("POST", adress);
            rating_xhr.setRequestHeader("X-CSRFToken", csrf_token);
            rating_xhr.setRequestHeader("Content-Type", "application/json");
            rating_xhr.send(request_body_json);

            // Обработка успеха и ошибок.
            rating_xhr.onload = function () {
                if (this.status === 200) {
                    var response_data = JSON.parse(this.responseText);
                    target.value = response_data.likes;
                }
                else {
                   alert("Status not a 200, it is "+this.status)
                }
            };

            rating_xhr.onerror = function () {
               alert("Error: "+this.status);
            }
        }
    }

    document.addEventListener("click",like_event);
}

window.addEventListenTo = addEventListenTo; // export "addEventListenTo" in global environment

}());
