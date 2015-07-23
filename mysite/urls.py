from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contact/', views.contact, name='contact'),
    url(r'^projects/', views.projects_listing, name='projects_listing'),
    url(r'^project/(?P<pk>\d+)/', views.project_detail, name='project_detail'),
    url(r'^about/', views.about, name='about'),
    url(r'^post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    url(r'^$', views.posts_listing, name='posts_listing'),
]