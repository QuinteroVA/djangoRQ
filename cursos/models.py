from django.db import models

class Curso(models.Model):
  codigo = models.CharField(primary_key=True,max_length=3)
  profesor = models.CharField(max_length=50)
  materia = models.CharField(max_length=50)
  horario = models.CharField(max_length=50)

  class Meta:
    verbose_name = "curso"
    verbose_name_plural = "cursos"

  def __str__(self):
    texto = "{0} ({1})"
    return texto.format(self.profesor, self.materia)