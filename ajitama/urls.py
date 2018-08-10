from django.urls import path, include
from django.conf.urls import url
from django.views import generic

from . import views

app_name = 'ajitama'

urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./ajitop'), name="index"),
    path('ajitop', include(views.ArticleViewSet().urls), name="ajitop"),
]

