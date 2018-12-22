from django.conf.urls import url
from django.http import Http404
from django.shortcuts import render

from . import views

urlpatterns = [
    url(r'^', qa.views.new_question_list, name='new_question_list'),
    url(r'^popular/', qa.views.popular_question_list, name='popular_question_list'),
    url(r'^question/(?P<slug>\d+)/$', qa.views.question, name='question'),
]
