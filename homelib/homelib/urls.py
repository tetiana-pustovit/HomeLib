from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homelib.views.home', name='home'),
    # url(r'^homelib/', include('homelib.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'movies.views.index'),
    url(r'^add_movie', 'movies.views.add_movie_view' ),
    url(r'^add', 'movies.views.add'),
    url(r'^movies', 'movies.views.navigate_to_movies_view')
)
