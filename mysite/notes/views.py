from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
from .forms import NoteEditor

# Create your views here.
def home(response):
    return render(response, "notes/home.html", {})

def notes(response, id):
    note_db = Note.objects.all()
    notes = {}
    for note in note_db:
        if note.user_id == id:
            notes[note.title] = note.content
    form = NoteEditor()
    return render(response, "notes/notes.html", {"form":form, "notes":notes})