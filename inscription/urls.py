from django.urls import path, include
from rest_framework import routers
from .views import *
from . import views


router = routers.DefaultRouter()
router.register("Etudiant", EtudiantViewset)
router.register("classe", ClasseViewset)
router.register("categorie", CategorieViewset)
router.register("cours", CoursViewset)
router.register("examen", ExamenViewset)
router.register("Annee-Academique", AnneAcademiqueViewset)
router.register("campus", CampusViewset)
router.register("faculte", FaculteViewset)
router.register("niveau", NiveauViewset)


urlpatterns = [
	path("", include(router.urls)),
]
