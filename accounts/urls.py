from django.urls import path, include
from .views import *
urlpatterns = [
    # path('', index, name='index' ),
    path('login/', custom_login, name='login' ),
    path('register', signup , name='register' ),
]
