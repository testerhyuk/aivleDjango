from django.urls import path
from . import views

app_name='vrksasana'
urlpatterns = [
    path('vrksasana/', views.vrksasana),
    path('update_count/', views.update_count),
]
