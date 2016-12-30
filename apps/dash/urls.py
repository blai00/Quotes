from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^quotes$', views.quotes),
    url(r'^submit_quote$', views.submit_quote),
    url(r'^logout$', views.logout)


]
