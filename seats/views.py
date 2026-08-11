from rest_framework.decorators import APIView, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import SeatCreateSerializers
from accounts.permission import IsController
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
# Create your views here.

class SeatAdd(APIView):
    permission_classes = [IsController]
    authentication_classes = [JWTAuthentication]
    @swagger_auto_schema(
        method='post',
        request_body=SeatCreateSerializers,
        responses={200: SeatCreateSerializers(), 400: "bad request"}
        operation_description="seat add"
    )
    def post(self, request, format=None):
        serializer = SeatCreateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "seta add successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
    