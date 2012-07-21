# Create your views here.
from django.shortcuts import render_to_response, HttpResponseRedirect
from movies.models import Movies
from django.template import RequestContext
from django.core.urlresolvers import reverse
from movies.forms import MovieAddingForm

def index(request):
	full_movies_list = Movies.objects.all()
<<<<<<< HEAD
	movie = Movies.objects.get(pk = 1)
	return render_to_response('base.html', context_instance=RequestContext(request))

def navigate_to_movies_view(request):
	return render_to_response('movies/movies.html', {'full_movies' : full_movies_list, 'movie' : movie})

def add_movie_view(request):
	return render_to_response('movies/add.html', context_instance=RequestContext(request))
=======
##	movie = Movies.objects.get(pk = 1)
	return render_to_response('movies/index.html', {'full_movies' : full_movies_list})
>>>>>>> upstream/master

def add(request):
	if request.method == 'POST':
		form = MovieAddingForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			genre = form.cleaned_data['genre']
			description = form.cleaned_data['description']
			new_movie = Movies(name = name, genre = genre, description = description)
			new_movie.save()
			return HttpResponseRedirect('')
	else:
		form = MovieAddingForm()

	return render_to_response('movies/add.html', { 'form' : form, }, context_instance=RequestContext(request))

