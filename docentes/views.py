from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Docente

def docentes (request):
  docentes = Docente.objects.all()
  return render(request, "docentes/docentes.html", {'docentes': docentes})

def editarD (request, cedula):
  docentes = Docente.objects.get(cedula=cedula)
  return render(request, "docentes/editarD.html", {'docentes': docentes})

def registrarD (request):
  cedula = request.POST['txtCedula']
  nombre = request.POST['txtNombre']
  materiaD = request.POST['txtMateriaD']
  docentes = Docente.objects.create(cedula=cedula, nombre=nombre, materiaD=materiaD)
  messages.success(request, '¡Docente registrado!')
  return redirect("docentes")

def actualizarD (request):
  cedula = request.POST['txtCedula']
  nombre = request.POST['txtNombre']
  materiaD = request.POST['txtMateriaD']
  docentes = Docente.objects.get(cedula=cedula)
  docentes.nombre = nombre
  docentes.materiaD = materiaD
  docentes.save()
  messages.success(request, '¡Docente actualizado!')
  return redirect("docentes")

def eliminarD (request, cedula):
  docentes = Docente.objects.get(cedula=cedula)
  docentes.delete()
  messages.success(request, '¡Docente eliminado!')
  return redirect("docentes")