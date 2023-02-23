from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteEditor

def get_user_notes(user_id):
    user_notes = Note.objects.filter(user_id=user_id)
    notes = {note.title:note.content for note in user_notes}
    return notes

# Create your views here.
def notes(response):
    if response.user.is_authenticated:
        user_id = response.user.id
        notes = get_user_notes(user_id)
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

def select(response):

    return redirect('/')