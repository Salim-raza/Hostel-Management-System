from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permission import IsControllerOrAssistantController
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import FineAddSerializer
from rest_framework import status
from .models import Fine

# Create your views here.
class FineAddView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsControllerOrAssistantController]

    def post(self, request):
        serializer = FineAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Fine added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FineUpdateview(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsControllerOrAssistantController]

    def patch(self, request, fine_id):
        fine = get_object_or_404(Fine, id=fine_id)
        serializer = FineAddSerializer(fine, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Fine updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        