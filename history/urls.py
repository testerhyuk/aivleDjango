from django.urls import path
from . import views

app_name='history'
urlpatterns = [
    path('history/', views.history),
<<<<<<< HEAD
<<<<<<< HEAD
    path('change_image/', views.change_image),
=======
    path('member_del/', views.member_del, name='member_del'),
>>>>>>> e40ea7e62e6d403b5f73db4cb4f95641809f618e
=======
    path('member_del/', views.member_del, name='member_del'),
>>>>>>> 8cf250dc2fbd4b0693550179268fe7e473b01641
]
