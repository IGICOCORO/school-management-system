from .models import *
from rest_framework import serializers

class EtudiantSerializer(serializers.ModelSerializer):
	fullname = serializers.SerializerMethodField()

	def get_fullname(self, obj):
		return f"{obj.user.first_name} {obj.user.last_name}"

	class Meta:
		model = Etudiant
		fields = "__all__"

class ClasseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classe
		fields = "__all__"

class CategorieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categorie
		fields = "__all__"

class CoursSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cours
		fields = "__all__"


class ExamenSerializer(serializers.ModelSerializer):

	class Meta:
		model = Examen
		fields = "__all__"

class AnneAcademiqueSerializer(serializers.ModelSerializer):

	class Meta:
		model = AnneAcademique
		fields = "__all__"

class CampusSerializer(serializers.ModelSerializer):

	class Meta:
		model = Campus
		fields = "__all__"

class FaculteSerializer(serializers.ModelSerializer):
	class Meta:
		model= Faculte
		fields = "__all__"


class NiveauSerializer(serializers.ModelSerializer):
	class Meta:
		model= Niveau
		fields = "__all__"
