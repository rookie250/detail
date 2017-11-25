from django.conf.urls import url

from . import views
from blog.feeds import AllPostsRssFeed

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
