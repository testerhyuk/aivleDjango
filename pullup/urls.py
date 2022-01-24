from django.urls import path
from . import views

urlpatterns = [
    path('pullup/', views.pullup)
]
