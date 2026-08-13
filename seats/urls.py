from django.urls import path
from .views import *


urlpatterns = [
    path("SeatAdd/", SeatAdd.as_view, name="seat_add"),
    path("SeatUpdate/", SeatUpdate.as_view, name="seat_update"),
    path("SeatDelete/", Delete.as_view, name="seat_delete")
]
