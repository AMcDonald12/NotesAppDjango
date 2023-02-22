from django import forms
from tinymce.widgets import TinyMCE
from .models import Note

class NoteEditor(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "notes"]
