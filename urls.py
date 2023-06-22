"""
URL configuration for prova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Alunos.views import AlunosViews
from Curso.views import CursoViews
from Disciplina.views import DisciplinaViews
from Turma.views import TurmaView
from Professor.views import ProfessorView
from DetalheCurso.views import DetalhecursoViews
from DetalheTurma.views import DetalheTurmaViews
from DetalheDisciplina.views import DetalheDisciplinaViews




rotas = routers.DefaultRouter()
rotas.register(r'alunos', AlunosViews, basename='alunos'),
rotas.register(r'curso', CursoViews, basename='curso'),
rotas.register(r'disciplina', DisciplinaViews, basename='disciplina'),
rotas.register(r'professor', ProfessorView, basename='professor'),
rotas.register(r'turma', TurmaView, basename='turma'),
rotas.register(r'detalhecurso', TurmaView, basename='detalhecurso'),
rotas.register(r'detalhedisciplina', TurmaView, basename='detalhedisciplina'),
rotas.register(r'detalheturma', TurmaView, basename='detalheturma'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas.urls)),
]
