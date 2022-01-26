from django.urls import path
from shoulder import views

urlpatterns = [
    path('shoulder/', views.shoulder),
    path('update_count/', views.update_count),
]
