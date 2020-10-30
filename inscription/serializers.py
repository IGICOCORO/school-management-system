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