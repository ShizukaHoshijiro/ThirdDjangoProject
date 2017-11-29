from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import TopicSerializer, UserSerializer
from core.models import Topic
from rest_framework import permissions
from .permissions import AuthorOrReadOnly


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.order_by("-pub_date")
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )
