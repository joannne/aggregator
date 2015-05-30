from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=100) 
	author = models.CharField(max_length = 50)
	genre = models.CharField(max_length=20)
	user = models.CharField(max_length=20)

class Movie(models.Model):
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=20)
	user = models.CharField(max_length=20)

class Music(models.Model):
	title = models.CharField(max_length=100)
	artist = models.CharField(max_length=40)
	genre = models.CharField(max_length=20)
	user = models.CharField(max_length=20)
