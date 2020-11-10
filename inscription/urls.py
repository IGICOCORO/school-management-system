from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views


router = routers.DefaultRouter()
router.register("Etudiant", EtudiantViewset)
router.register("classe", ClasseViewset)
router.register("categorie", CategorieViewset)
router.register("Examen", ExamenViewset)
router.register("cours", CoursViewset)

urlpatterns = [
	path("", include(router.urls)),
]
