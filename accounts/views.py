from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework.response import Response
from src.accounts.serializers import UserSerializer
from rest_framework import status
# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=201)
        return Response(serializer.errors, status=400)