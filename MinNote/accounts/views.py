from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def login_user(request):
	""" logs in the user and redirects to the notes main page"""
	username = request.POST['username']
	password = request.POST['password']
	
	user = authenticate(username = username, password = password)
	
	if(user is not None):
		login(request,user)
		return redirect('main')
	else:
		#redirect to failed_login.html

def logout_user(request):
	""" logs out user and redirects the user to the login page"""

