from django.contrib import admin
from .models import *

class EtudiantAdmin(admin.ModelAdmin):
	list_display = "user", "matricule","année_academique"
	list_filter =  "user", "matricule", "année_academique"
	ordering =  "user", "matricule", "année_academique"

class ClasseAdmin(admin.ModelAdmin):
	list_display = "nom","etudiant","cours"
	list_filter = "nom", "etudiant","cours"
	ordering =  "etudiant","cours"

class CoursAdmin(admin.ModelAdmin):
	list_display = "nom", "categorie"
	list_filter = "nom", "categorie"
	ordering = "nom", "categorie"

class ExamenAdmin(admin.ModelAdmin):
	list_display = "nom", "notes", "cours"
	list_filter = "nom", "notes", "cours"
	ordering = "nom", "notes", "cours"



admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Examen, ExamenAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(Categorie)
