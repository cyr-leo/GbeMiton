
# # Create your views here.
from django.contrib.auth.models import User
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, UserLoginForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Enregistrer le nouvel utilisateur
            # (Vous devrez remplacer cette partie par le code approprié pour créer un nouvel utilisateur dans votre modèle d'utilisateur)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Créez un nouvel utilisateur avec les informations fournies
            # Remplacez cette ligne par votre logique de création d'utilisateur
            # Utilisez la fonction create_user ou create de votre modèle d'utilisateur personnalisé
            new_user = User.objects.create_user(username=username, email=email, password=password)
            # Connexion automatique de l'utilisateur après la création du compte
            login(request, new_user)
            return redirect('home')  # Rediriger vers la page d'accueil après l'inscription
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Rediriger vers la page d'accueil après la connexion
            else:
                # Gérer le cas où l'authentification échoue
                # Vous pouvez renvoyer un message d'erreur à l'utilisateur
                pass
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})
