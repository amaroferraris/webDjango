
from django.contrib import admin
from django.urls import path, include
from webDjango.view import home, homePage, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('home/<name>', home),
    path('homePage/', homePage),
    path('AppCoder/', include("AppCoder.urls")),
]
