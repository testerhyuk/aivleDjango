from django.urls import path
from . import views

app_name='history'
urlpatterns = [
    path('history/', views.history),
    path('member_del/', views.member_del, name='member_del'),
]
