from django.urls import path
from django.conf.urls import include, url
from .views import list_view, detail_view


urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]

"""
urlpatterns = [
    url(r'^category$', views.category_list, name='category_list'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
"""