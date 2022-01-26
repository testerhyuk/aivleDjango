from django.urls import path
from member import views

app_name = 'member'

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout, name='logout'),
]