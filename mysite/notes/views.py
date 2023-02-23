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
        default_note = list(notes.keys())[0]
        form = NoteEditor(initial={'title':default_note, 'content':notes[default_note]})
        return render(response, "notes/notes.html", {"form":form, "notes":notes})
    return redirect('/login')

def create(response):
    if response.method == "POST":
        new_note = Note(title='New Note', content="Start typing notes here.")
        new_note.save()
        response.user.note.add(new_note)
    return redirect('/')

def select(response, id):

    return render(response, "notes/notes.html", )