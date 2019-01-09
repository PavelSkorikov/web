from django.conf.urls import url
from django.http import Http404
from django.shortcuts import render
from qa.views import popular_question_list, answer_add, question_add, signup, login_view, logout_view

urlpatterns = [
    url(r'popular', popular_question_list, name='popular_question_list'),
    url(r'question/(?P<pk>\d+)/', answer_add, name='answer_add'),
    url(r'ask/', question_add, name='question_add'),
    url(r'signup/', signup, name='signup'),
    url(r'login/', login_view, name='login_view'),
    url(r'logout/', logout_view, name='logout_view'),
]
