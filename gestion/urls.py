from django.contrib import admin
from django.urls import path
from core import views as core_views
from cursos import views as cursos_views
from docentes import views as doc_views
from estudiantes import views as est_views

urlpatterns = [
  path('', core_views.home, name="home"),
  path('cursos/', cursos_views.cursos, name="cursos"),
  path('docentes/', doc_views.docentes, name="docentes"),
  path('estudiantes/', est_views.estudiantes, name="estudiantes"),
  path('login/', core_views.login, name="login"),
  path('registrar/', cursos_views.registrar),
  path('editar/<codigo>', cursos_views.editar),
  path('actualizar/', cursos_views.actualizar),
  path('eliminar/<codigo>', cursos_views.eliminar),
  path('registrarD/', doc_views.registrarD),
  path('editarD/<cedula>', doc_views.editarD),
  path('actualizarD/', doc_views.actualizarD),
  path('eliminarD/<cedula>', doc_views.eliminarD),
  path('registrarE/', est_views.registrarE),
  path('editarE/<cedula>', est_views.editarE),
  path('actualizarE/', est_views.actualizarE),
  path('eliminarE/<cedula>', est_views.eliminarE),
  path('admin/', admin.site.urls),
]
