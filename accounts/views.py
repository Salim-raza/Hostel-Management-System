from rest_framework.decorators import APIView, permission_classes, authentication_classes
from .serializers import UserCreateSerializer, SigninSerializer, ChangePasswordSerializer, OtpCreateSerializer, ResetPasswordSerializer
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
from drf_yasg.utils import swagger_auto_schema
import random
# Create your views here.


class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        responses={201: "User registered successfully", 400: "Invalid data"},
        operation_description="User registration"
    )
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
    
    @swagger_auto_schema(
        request_body=OtpCreateSerializer,
        responses={201: "otp create successful", 400: "email dosenot exists"},
        operation_description="send otp"
    )
    
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
        

class ResetPassword(APIView):
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        request_body=ResetPasswordSerializer,
        responses={200: "password reset successful", 400: "wrong otp or email dosenot exists"},
        operation_description="reset password"
    )
    
    def post(self, request, format=None):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data["email"]
        otp = serializer.validated_data["otp"]
        new_password = serializer.validated_data["new_password"]
        
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email__iexact=email)
            db_otp = OTP.objects.filter(user=user).last()
            
            if db_otp and str(otp) == str(db_otp.otp):
                if db_otp.is_expire:
                    return Response({
                        "status": "error",
                        "message": "otp time is expired"
                    }, status=status.HTTP_400_BAD_REQUEST)
                user.set_password(new_password)
                user.save()
                
                return Response({
                    "status": "success",
                    "message": "password reset successful"
                }, status=status.HTTP_200_OK)
                
            return Response({
                "status": "failed",
                "message": "wrong otp"
            }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
            "status": "failed",
            "message": "email dosenot exists"
        },status=status.HTTP_400_BAD_REQUEST)