from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *

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
