from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permission import IsStudentOrAdminOrControllerOrManager
from rest_framework.response import Response
from .serializers import ProfileUpdateSerializers
from rest_framework import status


# Create your views here.
class ProfileUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStudentOrAdminOrControllerOrManager]
    
    def put(self, request):
        profile = request.user.profile
        serializer = ProfileUpdateSerializers(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Profile updated successfully.", "profile": serializer.data}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)