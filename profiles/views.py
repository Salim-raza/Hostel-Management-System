from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from profiles.models import Profile
from .serializers import ProfileUpdateSerializers
from django.shortcuts import get_object_or_404
from rest_framework import status


# Create your views here.
class ProfileUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        profile = request.user.profile
        serializer = ProfileUpdateSerializers(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Profile updated successfully.", "profile": serializer.data}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileUpdateSerializers(profile)
        return Response({"profile": serializer.data}, status=status.HTTP_200_OK)
    
class ProfileListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileUpdateSerializers(profiles, many=True)
        return Response({"profiles": serializer.data}, status=status.HTTP_200_OK)
    
class DeleteProfile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def delete(self, request):
        user = request.user
        if user is None:
            return Response({
                "message": "user delete successful"
            }, status=status.HTTP_200_OK)
        user.delete()
        return Response(
            {"message": "profile delete successful"},
            status=status.HTTP_200_OK
            )
    
