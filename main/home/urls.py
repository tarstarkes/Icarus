from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home_base'),
    url(r'^sitemap/', views.sitemap, name="site_map"),
]