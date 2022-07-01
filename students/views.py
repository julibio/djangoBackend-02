
from rest_framework.viewsets import ModelViewSet

from .models import Student,Curso,Diario
from .serializers import CursoSerializer, StudentSerializer, DiarioSerializer

class StudentsViewSet(ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class CursoViewSet(ModelViewSet):
      queryset = Curso.objects.all()
      serializer_class = CursoSerializer


class DiarioViewSet(ModelViewSet):
      queryset = Diario.objects.all()
      serializer_class = DiarioSerializer




