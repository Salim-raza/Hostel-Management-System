from django.urls import path
from .views import *


urlpatterns = [
    path("SeatAdd/", SeatAdd.as_view, name="seat_add")
]
