from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'search/$',views.getSearchTerm),
    url(r'tweet',views.showTweets),
    url('^$',views.index, name='index'),
    
    
]