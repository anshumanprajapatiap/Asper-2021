from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "Main"

urlpatterns = [
    path('', Index, name='Index'),


]