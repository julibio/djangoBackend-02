from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=140)
  course = models.CharField(max_length=140)
  rating = models.IntegerField()

  def __str__(self):
      return self.name

  class Meta:
    ordering = ['name']

class Curso(models.Model):
  nome_curso = models.CharField(max_length=140)
  ch_curso = models.IntegerField()

  def __str__(self):
    return self.nome_curso

  class Meta:
    ordering = ['nome_curso']

class Diario(models.Model):
  nome_turma=models.CharField(max_length=140)
  nota_aluno=models.FloatField()
  student = models.ForeignKey(Student, related_name='matricula', on_delete=models.CASCADE)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

  def __str__(self):
        return self.nome_turma
