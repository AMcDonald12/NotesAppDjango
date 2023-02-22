from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteEditor

# Create your views here.
def notes(response):
    if response.user.is_authenticated:
        id = response.user.id
        note_db = Note.objects.all()
        notes = {}
        for note in note_db:
            if note.user_id == id:
                notes[note.title] = note.content
        form = NoteEditor()
        return render(response, "notes/notes.html", {"form":form, "notes":notes})
    return redirect('/login')