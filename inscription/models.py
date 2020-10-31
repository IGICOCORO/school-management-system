from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time

# Create your models here.
class Etudiant(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	matricule = models.CharField(max_length=100)
	année_academique = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"


class Classe(models.Model):
	nom = models.CharField(max_length=50)
	etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.nom}"


class Categorie(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.nom}"


class Cour(models.Model):
	nom = models.CharField(max_length=50)
	credit = models.PositiveIntegerField( default= 0)
	classe = models.OneToOneField(Classe,on_delete=models.CASCADE)
	categorie = models.OneToOneField(Categorie,on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.nom}"


class Examen(models.Model):
	nom = models.CharField(max_length=50)
	notes = models.PositiveIntegerField(default=0)
	cours = models.OneToOneField(Cours,on_delete=models.CASCADE)
	categorie = models.OneToOneField(Categorie,on_delete=models.CASCADE)


	def __str__(self):
		return f"{self.nom} {self.notes}"


