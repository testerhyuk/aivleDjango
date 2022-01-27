from django.urls import path
from . import views

app_name='history'
urlpatterns = [
    path('history/', views.history),
    path('change_image/', views.change_image),
]
