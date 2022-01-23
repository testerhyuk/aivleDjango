from django.urls import path
from triceps import views

urlpatterns = [
    path('triceps/', views.triceps)
]
