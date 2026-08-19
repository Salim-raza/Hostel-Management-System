from django.urls import path
from .views import MealAdd

urlpatterns = [
    path("meal_add/", MealAdd.as_view(), name="meal_add"),
    path("meal_update/<int:id>/", MealAdd.as_view(), name="meal_update"),
    path("meal_delete/<int:id>/", MealAdd.as_view(), name="meal_delete"),
]
