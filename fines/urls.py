from django.urls import path
from .views import *


urlpatterns = [
    path('add/', FineAddView.as_view(), name='fine-add'),
    path('update/<int:fine_id>/', FineUpdateview.as_view(), name='fine-update'),
]