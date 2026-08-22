from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MealAddSerializer, MealUpdateSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from accounts.permission import IsManager
from rest_framework import status
from .models import Meal

# Create your views here.
class MealAdd(APIView):
    permission_classes = [IsManager]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request, format=None):
        serializer = MealAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "meal add successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)


class MealUpdate(APIView):
    permission_classes = [IsManager]
    authentication_classes = [JWTAuthentication]
    
    def patch(self, request, id, format=None):
        meal = get_object_or_404(Meal, id=id)
        serializer = MealUpdateSerializer(meal, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "meal update successful", "data": serializer.data}, status=status.HTTP_200_OK)


class DeleteMeal(APIView):
    permission_classes = [IsManager]
    authentication_classes = [JWTAuthentication]
    
    def delete(self, request, id, format=None):
        meal = get_object_or_404(Meal, id=id)
        meal.delete()
        return Response({"message": "meal delete successful"}, status=status.HTTP_200_OK)
        
        