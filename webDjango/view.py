from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

def home(self, name):
    return HttpResponse(f'Hola soy {name}')

def inicio(request):
    return HttpResponse(f'Hola soy inicio webDjango')

def homePage(self):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    data = {"nombre":"Amaro", "apellido":"El Pingüinito", "lista":lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    # planilla = loader.get_template('cursos.html')
    curso = Curso(nombre="UX/UI", camada="12345")
    curso.save()

    documento = f'Curso: {curso.nombre} Camada: {curso.camada}'
    return HttpResponse(documento)

