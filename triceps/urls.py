from django.urls import path
from triceps import views

urlpatterns = [
    path('triceps/', views.triceps),
    path('update_count/', views.update_count),
]
