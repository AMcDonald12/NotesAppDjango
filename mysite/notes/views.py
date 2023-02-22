from django.shortcuts import render
from .models import Note
from .forms import NoteEditor

# Create your views here.
def notes(response):
    id = response.user.id
    note_db = Note.objects.all()
    notes = {}
    for note in note_db:
        if note.user_id == id:
            notes[note.title] = note.content
    form = NoteEditor()
    return render(response, "notes/notes.html", {"form":form, "notes":notes})