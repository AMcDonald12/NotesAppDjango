from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Note
from .forms import NoteEditor

# Create your views here.
def home(response):
    if response.user.is_authenticated:
        return redirect("/logout")
    return redirect("/login")

def welcome(response):
    if response.user.is_authenticated:
        user_id = response.user.id
        notes = Note.objects.filter(user_id=user_id)
        current_note = notes.first()
        return HttpResponseRedirect("/%i" %current_note.id)
    return redirect('/login')

def notes(response, note_id):
    if response.user.is_authenticated:
        user_id = response.user.id
        notes = Note.objects.filter(user_id=user_id)
        current_note = notes.get(id=note_id)
        form = NoteEditor(initial={'title':current_note.title, 'content':current_note.content})
        return render(response, "notes/notes.html", {"form":form, "notes":notes})
    return redirect('/login')

def create(response):
    if response.method == "POST":
        new_note = Note(title='New Note', content="Start typing notes here.")
        new_note.save()
        response.user.note.add(new_note)
    return HttpResponseRedirect("/%i" %new_note.id)