from rest_framework.permissions import BasePermission
from .models import *


class IsController(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role == 'controller'

