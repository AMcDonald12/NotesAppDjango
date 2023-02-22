from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteEditor

# Create your views here.
def home(response):
    return render(response, "notes/home.html", {})

def notes(response, id):
    notes = Note.objects.all()
    form = NoteEditor()
    return render(response, "notes/notes.html", {"form":form, "notes":notes})