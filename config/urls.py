# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name='pages/contact.html'), name="contact"), 
    url(r'^recommendations/$', TemplateView.as_view(template_name='recommend_all/front.html'), name="recommendations"),
    url(r'^recommendations/all$', 'aggregator.recommend_all.views.index', name="all"),
    # url(r'^recommend_all/all$', TemplateView.as_view(template_name='recommend_all/all.html'), name="recommend_all"),
    url(r'^recommendations/books$', 'aggregator.recommend_all.views.books', name="books"),
    url(r'^recommendations/movies$', 'aggregator.recommend_all.views.movies', name="movies"),
    url(r'^recommendations/music$', 'aggregator.recommend_all.views.music', name="music"),
    url(r'^recommendations/suggest_book$', 'aggregator.recommend_all.views.suggest_book', name="suggest_book"),
    url(r'^recommendations/suggest_movie$', 'aggregator.recommend_all.views.suggest_movie', name="suggest_movie"),
    url(r'^recommendations/suggest_music$', 'aggregator.recommend_all.views.suggest_music', name="suggest_music"),
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    


    # User management
    url(r'^users/', include("aggregator.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', 'django.views.defaults.bad_request'),
        url(r'^403/$', 'django.views.defaults.permission_denied'),
        url(r'^404/$', 'django.views.defaults.page_not_found'),
        url(r'^500/$', 'django.views.defaults.server_error'),
    ]
