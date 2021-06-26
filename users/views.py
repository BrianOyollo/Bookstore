from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


# Create your views here.
""" No longer being used. Sign up is being handled by allauth """
# class SignUpPageView(CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'signup.html'
#     success_url = reverse_lazy('login')
