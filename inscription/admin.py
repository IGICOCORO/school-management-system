from django.contrib import admin
from .models import *

class EtudiantAdmin(admin.ModelAdmin):
	list_display = "user", "matricule","classe","faculte","niveau"
	list_filter =  "user", "matricule","classe","faculte","niveau"
	ordering =  "user", "matricule", "classe","faculte","niveau"

class ClasseAdmin(admin.ModelAdmin):
	list_display = "niveau","faculte","a_a","fin_inscription","cloturee"
	list_filter = "niveau","faculte","a_a","fin_inscription","cloturee"
	ordering =  "niveau","faculte","a_a","fin_inscription","cloturee"

class CoursAdmin(admin.ModelAdmin):
	list_display = "nom", "v_h","classe"
	list_filter = "nom", "v_h","classe"
	ordering = "nom", "v_h","classe"

class ExamenAdmin(admin.ModelAdmin):
	list_display = "nom", "notes", "cours","categorie","date","faculte"
	list_filter = "nom", "notes", "cours","categorie","date","faculte"
	ordering = "nom", "notes", "cours","categorie","date","faculte"

class NiveauAdmin(admin.ModelAdmin):
	list_display = "nom", "niveau"
	list_filter = "nom", "niveau"
	ordering = "nom", "niveau"

class FaculteAdmin(admin.ModelAdmin):
	list_display = "nom", "niveau","a_a"
	list_filter = "nom", "niveau","a_a"
	ordering = "nom", "niveau","a_a"

class  CampusAdmin(admin.ModelAdmin):
	list_display = "nom", "faculte"
	list_filter = "nom", "faculte"
	ordering = "nom", "faculte"


admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Examen, ExamenAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(Categorie)
admin.site.register(AnneAcademique)
admin.site.register(Faculte,FaculteAdmin)
admin.site.register(Niveau,NiveauAdmin)
admin.site.register(Campus,CampusAdmin)