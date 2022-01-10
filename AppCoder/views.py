from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(self):

    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")
def cursos(request):

    lista = Curso.objects.all()

    return render(request, "AppCoder/cursos.html", {"lista": lista})

def profesores(request):
    return render(request, "AppCoder/profesores.html")
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
def entregables(request):
    return render(request, "AppCoder/entregables.html")
