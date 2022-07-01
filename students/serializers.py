from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Student,Curso,Diario


class StudentSerializer(ModelSerializer):
  matricula = serializers.StringRelatedField(many=True)
  
  class Meta:
    model = Student
    fields = ['id', 'name', 'course', 'rating', 'matricula']


class CursoSerializer(ModelSerializer):
  class Meta:
    model = Curso
    fields = ['id','nome_curso','ch_curso']

class DiarioSerializer(ModelSerializer):
  url = serializers.HyperlinkedIdentityField(
        view_name='diario-detail',
        lookup_field='pk'
    )    

  student = serializers.SlugRelatedField(queryset=Student.objects.all(),
        slug_field='name')
  curso = serializers.SlugRelatedField(queryset=Curso.objects.all(),
        slug_field='nome_curso')

  class Meta:
    model=Diario
    fields = '__all__'
   # fields = ['id','nome_turma','nota_aluno','student','curso']