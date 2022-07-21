from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
	#user_id = models.ForeignKey(
	title = models.CharField(max_length = 25)
	content = models.CharField(max_length = 1000) 

