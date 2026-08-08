from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('signup/', SignupView.as_view(), name="signup"),
    path("change_password/", ChangePassword.as_view(), name="change_password"),
    path("send_otp/", SendOtp.as_view(), name="send_otp"),
    path('reset_password/', ResetPassword.as_view(), name="reset_password")
]