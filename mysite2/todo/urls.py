from django.conf.urls import patterns, url

from todo import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<list_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<list_id>\d+)/add/$', views.add, name='add'),
    # ex: /polls/5/vote/
    url(r'^(?P<list_id>\d+)/vote/$', views.vote, name='vote'),
)