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

class Home(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_initial = request.user.username[0].upper()
            contacts = Contact.objects.all()
            return render(request, self.template_name, locals())
        else:
            return redirect("login")

def disconnect(request):
    show_hidden = "hidden"
    logout(request)
    return redirect("login")


class Connexion(View):
    template_name = "login.html"
    next_p = "inscription"

    def get(self, request, *args, **kwargs):
        form = ConnexionForm()
        try:
            self.next_p = request.GET["next"]
        except:
            print
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)
                messages.success(request, "You're now connected!")
                return redirect(self.next_p)
            else:
                messages.error(request, "logins incorrect!")
        return render(request, self.template_name, locals())



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
