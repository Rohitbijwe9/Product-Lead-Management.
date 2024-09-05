from rest_framework.permissions import BasePermission

class IsAuthenticatedForMethodsExceptGet(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET': #only get method auth no requred
            return True
        
        return request.user and request.user.is_authenticated #authentication required
