from django.urls import path
from squat import views

urlpatterns = [
    path('squat/', views.squat),
    path('update_count/', views.update_count),
]
