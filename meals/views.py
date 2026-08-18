from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from accounts.permission import IsManager
from rest_framework import status
from .serializers import MealAddSerializer

# Create your views here.

class MealAdd(APIView):
    permission_classes = [IsManager]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request, format=None):
        serializer = MealAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "meal add successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
