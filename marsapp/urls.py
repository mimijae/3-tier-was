from django.urls import path
from . import views

urlpatterns = [
    path('fruits/', views.fruit_list, name='fruit_list'),
    
]