from django.urls import path, include 
from django.http import HttpResponse
import views

urlpatterns = [
    path('',views.view_all_notes, name = "main"),
    path('delete/<int:note_id>',views.delete_note, name = "delete"),
    path('edit/<int:note_id>',views.edit_note, name = "edit"),
    path('add',views.add_note, name = "add")

]
