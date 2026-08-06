from django.urls import path
from .views import *


urlpatterns = [
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile-view'),
    path('profiles_list/', ProfileListView.as_view(), name='profile-list'),
]