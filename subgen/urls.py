from django.contrib import admin
from django.urls import path, include

from GbéMiton import settings
from .views import *
urlpatterns = [
    path('', home , name="subgen" ),
    # path('<int:v_id>/', video , name="vid" ),
    path('gen/', generate , name="gen" ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)