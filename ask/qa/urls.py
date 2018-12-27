from django.conf.urls import url
from django.http import Http404
from django.shortcuts import render

from qa.views import new_question_list, popular_question_list, question

urlpatterns = [
    url(r'^\?page=', new_question_list, name='new_question_list'),
    url(r'^popular/', popular_question_list, name='popular_question_list'),
    url(r'^question/(?P<pk>\d+)/', question, name='question'),
]