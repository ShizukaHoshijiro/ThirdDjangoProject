
var request_body_for_comment = {
  "model_name":"comment",
  "object_id":null,
  "app_label":"comment_app"
};

target_selector_for_comment = ".like_form_for_comment .btn";

addLikeEventListenTo(target_selector_for_comment,request_body_for_comment);