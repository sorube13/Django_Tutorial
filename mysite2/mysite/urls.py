from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^todo/', include('todo.urls', namespace="todo")),
    url(r'^admin/', include(admin.site.urls)),
)