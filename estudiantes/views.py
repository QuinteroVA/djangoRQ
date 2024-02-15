from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Estudiante

def estudiantes (request):
  estudiantes = Estudiante.objects.all()
  return render(request, "estudiantes/estudiantes.html", {'estudiantes': estudiantes})

def editarE (request, cedula):
  estudiantes = Estudiante.objects.get(cedula=cedula)
  return render(request, "estudiantes/editarE.html", {'estudiantes': estudiantes})

def registrarE (request):
  cedula = request.POST['txtCedula']
  nombre = request.POST['txtNombre']
  materiaE = request.POST['txtMateriaE']
  nota1 = request.POST['txtNota1']
  nota2 = request.POST['txtNota2']
  nota3 = request.POST['txtNota3']
  estudiantes = Estudiante.objects.create(cedula=cedula, nombre=nombre, materiaE=materiaE, nota1=nota1, nota2=nota2, nota3=nota3)
  messages.success(request, '¡Estudiante registrado!')
  return redirect("estudiantes")

def actualizarE (request):
  cedula = request.POST['txtCedula']
  nombre = request.POST['txtNombre']
  materiaE = request.POST['txtMateriaE']
  nota1 = request.POST['txtNota1']
  nota2 = request.POST['txtNota2']
  nota3 = request.POST['txtNota3']
  estudiantes = Estudiante.objects.get(cedula=cedula)
  estudiantes.nombre = nombre
  estudiantes.materiaE = materiaE
  estudiantes.nota1 = nota1
  estudiantes.nota2 = nota2
  estudiantes.nota3 = nota3
  estudiantes.save()
  messages.success(request, '¡Estudiante actualizado!')
  return redirect("estudiantes")

def eliminarE (request, cedula):
  estudiantes = Estudiante.objects.get(cedula=cedula)
  estudiantes.delete()
  messages.success(request, '¡Curso eliminado!')
  return redirect("estudiantes")