"""AlohaCorps URL Configuration"""
#AlohaCorps/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("aloha_app_pro/", include("aloha_app_pro.urls")),
    path("blog/", include("blog.urls")),
]
