(function(){ // Обёртка в анонимную функцию чтобы не захламлять глобальное окружение.

var general_info = {};
general_info.username = "{{user}}";
general_info.is_authenticated = new Boolean("{%if user.is_authenticated %}some{%else%}{%endif%}");
// Костыли, ибо IDE не нравится синтаксис шаблонов в js файле. ¯\_(ツ)_/¯

window.general_info = general_info

}()); // Конец обёртки.
