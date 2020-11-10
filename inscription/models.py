from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time

# Create your models here.
class Etudiant(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	matricule = models.CharField(max_length=50)
	classe = models.OneToOneField(Classe, on_delete=models.CASCADE)
	faculte = models.ForeignKey(Faculte,on_delete=models.CASCADE)
	niveau = models.OneToOneField(Niveau,on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"


class Classe(models.Model):
    niveau = models.ForeignKey(Niveau,on_delete=models.CASCADE ,null=False, blank=False)
    faculte = models.ForeignKey(Faculte,on_delete=models.CASCADE, null=False, blank=False)
    a_a = models.ForeignKey(AnneAcademique,on_delete=models.CASCADE, null=False, blank=False)
    fin_inscription = models.DateField(null=False, blank=False)
    cloturee = models.BooleanField(null=False, default=False)

    def nom_niveau(self):
    	return f"{self.niveau.nom}"

    def nom_faculte(self):
    	return f"{self.faculte.nom}"

    def nom_a_a(self):
    	return f"{self.a_a.nom}"

    def __str__(self):
        return f"{self.niveau.nom} {self.faculte.nom}"


class Categorie(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.nom}"


class Cours(models.Model):
    nom = models.CharField(max_length=20, unique=True)
    v_h = models.IntegerField(null=True)
    classe = models.ForeignKey(Classe, null=False)
    Enseignant = models.ForeignKey(User, null=False)

    def __str__(self):
    	return f"{self.nom}"

class AnneAcademique(models.Model):
    nom = fields.CharField(max_length=50, null=True)

    def __str__(self):
    	return nom


class Examen(models.Model):
	nom = models.CharField(max_length=50)
	notes = models.PositiveIntegerField(default=0)
	cours = models.OneToOneField(Cours,on_delete=models.CASCADE)
	categorie = models.OneToOneField(Categorie,on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	faculte = models.ForeignKey(Faculte,on_delete=models.CASCADE)


	def __str__(self):
		return f"{self.nom} {self.notes}"

class Niveau(models.Model):
	nom = models.CharField(max_length=20)
	niveau = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.nom} { self.niveau}"


class Faculte(models.Model):
	nom = fields.CharField(max_length=50, null=True)
	niveau = models.OneToOneField(Niveau,on_delete=models.CASCADE)
	a_a = models.ForeignKey(AnneAcademique,on_delete=models.CASCADE)

	def __str__(self):
		return nom

class Campus(models.Model):
	nom = models.CharField(max_length=30)
	faculte = models.ForeignKey(Faculte,on_delete=models.CASCADE)
	
	def __str__(self):
		return nom