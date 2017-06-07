from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home_base'),
    url(r'^sitemap/', views.sitemap, name="site_map"),
    url(r'^subscribe/', views.subscribe, name="subscribe"),
    url(r'^ripples-admin/', views.ripples_dashboard, name="ripples_dashboard"),
    url(r'^ripples/send-newsletter/', views.send_newsletter, name="send_newsletter"),
    url(r'^confirm_subscriber/(?P<email>.*)/(?P<conf_key>.*)/$', views.confirm_subscriber, name='confirm_subscriber'),
    url(r'^unsubscribe/(?P<email>.*)/(?P<conf_key>.*)/$', views.unsubscribe, name='unsubscribe'),

]