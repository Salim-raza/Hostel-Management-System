from django.urls import path
from .views import *


urlpatterns = [
    path('add/', FineAddView.as_view(), name='fine-add'),
    path('update/<int:fine_id>/', FineUpdateview.as_view(), name='fine-update'),
    path('delete/<int:fine_id>/', FineDeleteView.as_view(), name='fine-delete'),
    path('list/', FineListView.as_view(), name='fine-list')
]