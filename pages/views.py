from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.views.generic import CreateView, UpdateView


# Create your views here.
class HomepageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
