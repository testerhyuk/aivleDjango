from django.urls import path
from member import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
]