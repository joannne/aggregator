from django import forms
from .models import *

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ('title', 'author', 'genre',)

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ('title', 'genre',)		

class MusicForm(forms.ModelForm):
	class Meta:
		model = Music
		fields = ('title', 'artist', 'genre',)		
