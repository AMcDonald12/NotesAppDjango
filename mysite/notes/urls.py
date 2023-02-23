from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.welcome, name='welcome'),
    path('<int:note_id>', views.notes, name='notes'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name='update'),
]