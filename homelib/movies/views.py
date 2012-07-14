# Create your views here.
from django.shortcuts import render_to_response
from movies.models import Movies

def index(request):
	full_movies_list = Movies.objects.all()
	movie = Movies.objects.get(pk = 1)
	return render_to_response('movies/index.html', {'full_movies' : full_movies_list, 'movie' : movie})