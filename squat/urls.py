from django.urls import path
from squat import views

urlpatterns = [
    path('squat/', views.squat)
]
