from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', views.index, name-'index'),

]
