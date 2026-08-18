from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from accounts.permission import IsManager
from rest_framework import status

# Create your views here.

class MealAdd(APIView):
    permission_classes = [IsManager]
    authentication_classes = [JWTAuthentication]
    
    def post
