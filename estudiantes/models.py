from django.db import models

class Estudiante(models.Model):
  cedula = models.CharField(primary_key=True,max_length=10)
  nombre = models.CharField(max_length=50)
  materiaE = models.CharField(max_length=50)
  nota1 = models.CharField(max_length=2)
  nota2 = models.CharField(max_length=2)
  nota3 = models.CharField(max_length=2)

  def __str__(self):
    texto = "{0} ({1})"
    return texto.format(self.nombre, self.materiaE)