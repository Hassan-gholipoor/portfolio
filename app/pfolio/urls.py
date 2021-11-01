from . import views
from django.urls import path

app_name = 'pfolio'

urlpatterns = [
    path('', views.Home.as_view(), name='home')
]