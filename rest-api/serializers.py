from rest_framework import serializers
from django.conf import settings
from core.models import Topic
from django.contrib.auth.models import User
from comment_app.models import Comment
from rating_app.models import Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username")


class TopicSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")
    number_of_comments = serializers.ReadOnlyField(source="comments.count")
    number_of_likes = serializers.ReadOnlyField(source="likes.count")

    class Meta:
        model = Topic
        fields = ("title", "description", "pub_date", "update_date", "id","author","number_of_comments","number_of_likes")

    def create(self, validated_data):
        topic = super(TopicSerializer, self).create(validated_data)
        topic.author = self.author
