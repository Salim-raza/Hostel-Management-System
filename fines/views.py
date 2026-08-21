from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import FineAddSerializer
from rest_framework.authentication import JWTAuthentication
from rest_framework import status
from .models import Fine

# Create your views here.
class FineAddView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    def post(self, request):
        serializer = FineAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Fine added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
