from django.urls import path
from .views import *


urlpatterns = [
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
]