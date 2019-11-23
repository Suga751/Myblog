#.......................Apps Urls.............................
from django.conf.urls import url
from . import views

                    
urlpatterns = [
    url(r'^$', views.home),
    url(r'^about$', views.about),
    url(r'^post/(?P<post_id>\d+)$', views.post_detail, name='post_detail'),
    url(r'^comment/(?P<post_id>\d+)$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<comment_id>\d+)/remove/(?P<post_id>\d+)$', views.comment_remove, name='comment_remove'),
    url(r'^new$', views.new_post, name='new_post'),
    url(r'^mentor$', views.mentor_page)    
    
]   