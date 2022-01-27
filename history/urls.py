from django.urls import path
from . import views

app_name='history'
urlpatterns = [
    path('history/', views.history),
    path('change_image/', views.change_image, name='change_image'),
    path('member_del/', views.member_del, name='member_del'),
    path('upload/', views.upload, name='upload'),
    path('img_show/', views.img_show, name='img_show'),
]
