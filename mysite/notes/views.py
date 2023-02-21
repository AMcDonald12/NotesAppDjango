from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Create your views here.
def index(response):
    return render(response, "notes/base.html", {})