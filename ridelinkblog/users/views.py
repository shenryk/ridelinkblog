from django.shortcuts import render
from django.views import generic 
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
# Create your views here.
# def profile(request):
#     return render (request, 'users/profile.html')

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

# class UserLoginView(LoginView):
#     template_name = 'users/login.html'
#     success_url = reverse_lazy('home')