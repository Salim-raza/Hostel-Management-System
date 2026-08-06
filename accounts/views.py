from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserCreateSerializer, SigninSerializer
from rest_framework.authentication import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .utils import get_tokens_for_user
from rest_framework import status
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


