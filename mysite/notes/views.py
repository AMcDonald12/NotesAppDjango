from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Note
from .forms import NoteEditor

#Call this when creating a new user, creating a new note
def new_note(response):
    new_note = Note(title='New Note', content="Start typing notes here.")
    new_note.save()
    response.user.note.add(new_note)
    return new_note

# Create your views here.
def welcome(response):
    if response.user.is_authenticated:
        user_id = response.user.id
        notes = Note.objects.filter(user_id=user_id)
        current_note = notes.first()
        if current_note:
            return HttpResponseRedirect("/%i" %current_note.id)
        new = new_note(response)
        return HttpResponseRedirect("/%i" %new.id)
    return redirect('/login')

def notes(response, note_id):
    try:
        if response.user.is_authenticated:
            user_id = response.user.id
            notes = Note.objects.filter(user_id=user_id)
            current_note = notes.get(id=note_id)
            form = NoteEditor(initial={'title':current_note.title, 'content':current_note.content})
            return render(response, "notes/notes.html", {"form":form, "notes":notes, "note_id":current_note.id})
        return redirect('/login')
    except:
        return redirect('/')

def create(response):
    if response.method == "POST":
        new = new_note(response)
    return HttpResponseRedirect("/%i" %new.id)

def update(response):
    if response.method == "POST" and "save" in response.POST:
        note_id = response.POST["save"]
        note_to_update = Note.objects.get(id=note_id)
        note_to_update.title = response.POST['title'] 
        note_to_update.content = response.POST['content']
        note_to_update.save()
        return HttpResponseRedirect("/%i" %int(note_id))
    if response.method == "POST" and "delete" in response.POST:
        note_id = response.POST["delete"]
        note_to_delete = Note.objects.get(id=note_id)
        note_to_delete.delete()
        return redirect("/")