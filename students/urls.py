from django.urls import path

from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('students', StudentsViewSet)
router.register('cursos', CursoViewSet)
router.register('diario', DiarioViewSet)

urlpatterns = router.urls