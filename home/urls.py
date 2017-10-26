from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^apply/$', views.apply, name='apply'),
    url(r'^apply/nonprofit/$', views.nonprofit, name='nonprofit'),
    url(r'^apply/private/$', views.private, name='private'),
    url(r'^apply/individual/$', views.individual, name='individual')
]
