from rest_framework import permissions
from rest_framework.views import View


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.profile == "Admin" or request.user.profile == "Manager"


class IsStaffOrRetrieve(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.user.profile == "Admin"
            or request.user.profile == "Manager"
            or request.method == "GET"
        )
