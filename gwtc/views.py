from django.shortcuts import render
from django.views import generic

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'homepage/index.html'