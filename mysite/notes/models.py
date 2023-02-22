from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note", null=True)
    title = models.CharField(max_length=200)
    notes = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title