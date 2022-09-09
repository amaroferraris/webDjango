
from django.contrib import admin
from django.urls import path
from webDjango.view import home, homePage, cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<name>', home),
    path('homePage/', homePage),
    path('cursos/', cursos),
]
