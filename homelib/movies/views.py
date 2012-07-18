# Create your views here.
from django.shortcuts import render_to_response, HttpResponseRedirect
from movies.models import Movies
from django.template import RequestContext
from django.core.urlresolvers import reverse

def index(request):
	full_movies_list = Movies.objects.all()
	movie = Movies.objects.get(pk = 1)
	return render_to_response('movies/index.html', {'full_movies' : full_movies_list, 'movie' : movie})

def add_movie_view(request):
	return render_to_response('movies/add.html', context_instance=RequestContext(request))

def add(request):
	mov_name = request.POST.get('name')
	mov_descr = request.POST.get('descr')
	mov_gen = request.POST.get('genre')
	new_movie = Movies(name = mov_name, description = mov_descr, genre = mov_gen)
	new_movie.save()
	return HttpResponseRedirect(reverse('movies.views.index'))