from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Curso

def cursos (request):
  cursos = Curso.objects.all()
  return render(request, "cursos/cursos.html", {'cursos': cursos})

def editar (request, codigo):
  cursos = Curso.objects.get(codigo=codigo)
  return render(request, "cursos/editar.html", {'cursos': cursos})

def registrar (request):
  codigo = request.POST['txtCodigo']
  profesor = request.POST['txtProfesor']
  materia = request.POST['txtMateria']
  horario = request.POST['txtHorario']

  cursos = Curso.objects.create(codigo=codigo, profesor=profesor, materia=materia, horario=horario)
  messages.success(request, '¡Curso registrado!')
  return redirect("cursos")

def actualizar (request):
  codigo = request.POST['txtCodigo']
  profesor = request.POST['txtProfesor']
  materia = request.POST['txtMateria']
  horario = request.POST['txtHorario']
  cursos = Curso.objects.get(codigo=codigo)
  cursos.profesor = profesor
  cursos.materia = materia
  cursos.horario = horario
  cursos.save()
  messages.success(request, '¡Curso actualizado!')
  return redirect("cursos")

def eliminar (request, codigo):
  cursos = Curso.objects.get(codigo=codigo)
  cursos.delete()
  messages.success(request, '¡Curso eliminado!')
  return redirect("cursos")