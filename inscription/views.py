from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views import View
from django.shortcuts import render

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *


def login(request):
    return render(request,'login.html')


class EtudiantViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Etudiant.objects.all()
	serializer_class = EtudiantSerializer

class ClasseViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Classe.objects.all()
	serializer_class = ClasseSerializer


class CategorieViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset =Categorie.objects.all()
	serializer_class = CategorieSerializer


class CoursViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset =Cours.objects.all()
	serializer_class = CoursSerializer

class ExamenViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, JWTAuthentication]
	permission_classes = [IsAuthenticated]
	queryset =Examen.objects.all()
	serializer_class = ExamenSerializer

class AnneAcademiqueViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset =AnneAcademique.objects.all()
    serializer_class = AnneAcademiqueSerializer


class CampusViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset =Campus.objects.all()
    serializer_class = CampusSerializer


class FaculteViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset =Faculte.objects.all()
    serializer_class = FaculteSerializer

class NiveauViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset =Niveau.objects.all()
    serializer_class = NiveauSerializer