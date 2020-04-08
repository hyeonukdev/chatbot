from django.urls import path
from . import views

urlpatterns = [
    path('foodmenu/', views.food_menu, name='foodmenu'),
]