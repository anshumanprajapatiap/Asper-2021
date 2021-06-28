from django.urls import path
from .views import *

app_name = "Codeadept"

urlpatterns = [
    path('', Index, name='Index'),
]