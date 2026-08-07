from rest_framework.decorators import APIView, permission_classes, authentication_classes
from .serializers import UserCreateSerializer, SigninSerializer, ChangePasswordSerializer, OtpCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import authenticate
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .utils import get_tokens_for_user
from rest_framework import status
from .models import CustomUser, OTP
from django.utils import timezone
import random
# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"message": "User registered successfully.", "user": UserCreateSerializer(user).data, "token": token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        request_body=SigninSerializer,
        responses={200: "Login Successful", 401: "Invalid credentials"},
        operation_description="User Signin"
    )
    
    def post(self, request, formate=None):
        serializer = SigninSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            email = serializer.validated_data["email"], 
            password = serializer.validated_data["password"]
        )
    
        
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({"message": "Login Successful .", "access_token" : token["access"], "refresh_token": token["refresh"]}, status=status.HTTP_200_OK)
        return Response({"message": "invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)


class ChangePassword(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        request_body=ChangePasswordSerializer,
        responses={200: "password change Successful", 401: "Invalid credentials"},
        operation_description="password change"
    )
    
    def post(self, request, formate=None):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(CustomUser, id=request.user.id)
        if user.check_password(serializer.validated_data["old_password"]):
            user.set_password(serializer.validated_data["new_password"])
            user.save()
            return Response({"message": "password change successful"}, status=status.HTTP_200_OK)
        return Response({"message": "invalid old password"}, status=status.HTTP_400_BAD_REQUEST)
    
    
class SendOtp(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, format=None):
        serializer = OtpCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data["email"]
        
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            otp = random.randint(1111, 9999)
            
            OTP.objects.update_or_create(user=user, defaults={"otp": otp, "create_at": timezone.now()})
            
            return Response({
                "status": "success",
                "message": "otp create successful"
            }, status=status.HTTP_201_CREATED)
            
        return Response({
            "status": "failed",
            "message": "email dosenot exists"
        }, status=status.HTTP_400_BAD_REQUEST)