from django.shortcuts import render
from django.contrib.auth.views import TemplateView


# Create your views here.
class HomepageView(TemplateView):
    template_name = 'home.html'
