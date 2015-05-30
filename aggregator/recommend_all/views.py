from django.shortcuts import render, redirect, render_to_response
from models import * 
from .forms import * 
from django.http import HttpResponse 

# Create your views here.
def index(request):
	all_books = Book.objects.all().order_by('-id')
	all_movies = Movie.objects.all().order_by('-id')
	all_music = Music.objects.all().order_by('-id')
	all_data = {'music' : all_music, 'movies' : all_movies, 'books' : all_books}
	return render_to_response('recommend_all/all.html', all_data)

def books(request):
	all_books = Book.objects.all().order_by('-id')
	book_data = {'books' : all_books} 
	return render_to_response('recommend_all/books.html', book_data)


def movies(request):
	all_movies = Movie.objects.all().order_by('-id')
	movie_data = {'movies' : all_movies} 
	return render_to_response('recommend_all/movies.html', movie_data)


def music(request):
	all_music = Music.objects.all().order_by('-id')
	music_data = {'music' : all_music} 
	return render_to_response('recommend_all/music.html', music_data)


def suggest_book(request):
	if request.user.is_authenticated(): 
		username = request.user 
	else: 
		username = "anonymous"
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			save_it = form.save(commit=False)
			save_it.user = username
			save_it.save()
			return render_to_response('recommend_all/confirmed.html') 
	else:
		form = BookForm()
	form_data = {'form': form}
	return render(request, 'recommend_all/suggest_book.html', form_data)


def suggest_movie(request):
	if request.user.is_authenticated(): 
		username = request.user 
	else: 
		username = "anonymous"
	if request.method == "POST":
		form = MovieForm(request.POST)
		if form.is_valid():
			save_it = form.save(commit=False)
			save_it.user = username
			save_it.save()
			return render_to_response('recommend_all/confirmed.html') 
	else:
		form = MovieForm()
	form_data = {'form': form}
	return render(request, 'recommend_all/suggest_movie.html', form_data)



def suggest_music(request):
	if request.user.is_authenticated(): 
		username = request.user 
	else: 
		username = "anonymous"
	if request.method == "POST":
		form = MusicForm(request.POST)
		if form.is_valid():
			save_it = form.save(commit=False)
			save_it.user = username
			save_it.save()
			return render_to_response('recommend_all/confirmed.html') 
	else:
		form = MusicForm()
	form_data = {'form': form}
	return render(request, 'recommend_all/suggest_music.html', form_data)

