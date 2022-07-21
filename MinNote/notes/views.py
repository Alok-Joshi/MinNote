from django.shortcuts import render
from django.http import HttpResponse


def view_all_notes(request):
	""" Loads the main page of the app, displays all the notes """
	#will first authenticate (use login required decorator or do it yourself), then use templates to render notes page 

def delete_note(request,note_id):
	""" deletes a note and refreshes the main page """

def edit_note(request,note_id):
	""" edits a note and redirects to the main page """

def add_note(request):
	""" Adds a note and redirects to the main page """ 

