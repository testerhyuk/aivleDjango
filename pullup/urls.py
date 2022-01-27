from django.urls import path
from . import views

urlpatterns = [
    path('pullup/', views.pullup),
    path('update_count/', views.update_count),
]
