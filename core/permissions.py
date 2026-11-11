from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # User must be logged in
        if not request.user or not request.user.is_authenticated:
            return False

        # Allow read-only requests
        if request.method in SAFE_METHODS:
            return True

        # Only staff users can modify data
        return request.user.is_staff

from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):

        # Staff can access any application
        if request.user.is_staff:
            return True

        # Students cannot delete applications
        if request.method == "DELETE":
            return False

        # Students can access only their own applications
        return obj.student == request.user