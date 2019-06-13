from django.urls import path
from . import views


app_name = 'fish'

urlpatterns = [
    path('', views.FishList.as_view(), name='all'),
]