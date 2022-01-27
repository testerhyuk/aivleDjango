from django.urls import path
from . import views

app_name='history'
urlpatterns = [
    path('history/', views.history),
<<<<<<< HEAD
    path('change_image/', views.change_image),
=======
    path('member_del/', views.member_del, name='member_del'),
>>>>>>> e40ea7e62e6d403b5f73db4cb4f95641809f618e
]
