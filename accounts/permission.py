from rest_framework.permissions import BasePermission
from .models import *



class IsControllerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role == 'controller' or user.role == 'admin'
    

class IsStudentOrAdminOrControllerOrManager(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role in ['student', 'admin', 'controller', 'manager']
    
    
    
class IsController(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role == "controller"
    
    
    
class IsManager(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role == "manager"
    
    
    
    
class IsControllerOrAssistantController(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.role in ["controller", "assistant_controller"]