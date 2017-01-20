from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='stepwise_home'),
    url(r'^stepwise_portal/$', views.stepwise_portal, name="stepwise_portal")
]