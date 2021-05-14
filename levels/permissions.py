from rest_framework.exceptions import APIException
from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_superuser:
            raise OnlyAdminCanCreateLevel

        return True


class OnlyAdminCanCreateLevel(APIException):
    status_code = 401
    default_detail = "Only Admin can create levels"
