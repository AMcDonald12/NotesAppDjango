from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteEditor

# Create your views here.
def index(response):
    form = NoteEditor()
    return render(response, "notes/notes.html", {"form":form})