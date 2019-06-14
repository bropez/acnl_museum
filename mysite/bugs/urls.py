from django.urls import path
from . import views


app_name = 'bugs'

urlpatterns = [
    path('', views.BugList.as_view(), name='all'),

]