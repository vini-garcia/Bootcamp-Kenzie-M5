from rest_framework.views import Request, View
from rest_framework import permissions
from users.models import User


class IsEmployeeOrOwnerReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if (
            (obj.id == request.user.id)
            or request.user.is_authenticated
            and request.user.is_employee
        ):
            return True

        return False
