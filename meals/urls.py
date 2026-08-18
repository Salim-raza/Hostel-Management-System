from django.urls import path
from .views import MealAdd

urlpatterns = [
    path("meal_add/", MealAdd.as_view(), name="meal_add")
]
