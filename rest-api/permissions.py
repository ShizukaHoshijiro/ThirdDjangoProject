from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ThisUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user