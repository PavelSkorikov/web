from django.conf.urls import url
from django.http import Http404
from django.shortcuts import render
from qa.views import popular_question_list, question

urlpatterns = [
    url(r'popular', popular_question_list, name='popular_question_list'),
    url(r'question/(?P<pk>\d+)/', question, name='question'),
]
