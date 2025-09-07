from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserRole(BasePermission):
    """
    Allows access only to users with role 'admin'.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')

class IsCustomerOrAdminReadOnly(BasePermission):
    """
    Safe methods allowed for everyone. POST for customers & admins. Admin only for writes to some endpoints.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        # allow POST for authenticated customers and admins
        return bool(request.user and request.user.is_authenticated and request.user.role in ['customer', 'admin'])
