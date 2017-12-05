
var request_body_for_topic = {
  "model_name":"topic",
  "object_id":null,
  "app_label":"core"
};

target_selector_for_topic = ".like_form_for_topic .btn";

addLikeEventListenTo(target_selector_for_topic,request_body_for_topic);