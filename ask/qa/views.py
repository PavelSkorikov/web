from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
#import django.contrib.sessions
from django.contrib.auth.decorators import login_required



def paginate(request, qs):
    global paginator
    global page
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        pg = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    #try:
    page = paginator.page(pg)
    #except EmptyPage:
     #   page = paginator.page(paginator.num_pages)
    return page

def new_question_list(request):
    new_questions = Question.objects.new()
    paginate(request, new_questions)
    paginator.baseurl = '/?page='
    return render(request, 'new_questions.html', {
        'new_questions':   page.object_list,
        'paginator':  paginator,
        'page': page,
    })

def popular_question_list(request):
    popular_questions = Question.objects.popular()
    paginate(request, popular_questions)
    paginator.baseurl = '/popular/?page='
    return render(request, 'popular_questions.html', {
        'popular_questions':  page.object_list,
        'paginator':  paginator,
        'page': page,
    })

"""def question(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    return render(request, 'question.html', {
        'question': question,
        'answers':   answers,
    })"""

@login_required
def question_add(request):
    if request.method == "POST":
        form = AskForm(request.user, request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm(request.user)
    return render(request, 'askform.html', {
        'form': form,
    })
@login_required
def answer_add(request, pk):
    if request.method == 'POST':
        q = request.POST.get('question')
        form = AnswerForm(request.user, request.POST)
        if form.is_valid():
            answer = form.save()
            url = '/question/' + q + '/'
            return HttpResponseRedirect(url)
    else:
        question = get_object_or_404(Question, id=pk)
        answers = question.answer_set.all()
        form = AnswerForm(request.user, initial={'question': question.id})
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })
def login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    url = '/'
                    return HttpResponseRedirect(url)
                else:
                    error = 'Аккаунт отключен'
            else:
                error = 'Неверный логин / пароль'
    else:
        form = LoginForm()
    return render(request, 'loginform.html', {
        'form': form,
        'error': error,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = request.POST.get('username')
            se = request.POST.get('password')
            user = authenticate(username=user_name, password=se)
            login(request, user)
            url = '/'
            return HttpResponseRedirect(url)
    else:
        form = SignupForm()
    return render(request, 'signupform.html', {
        'form': form,
    })
def logout_view(request):
    logout(request)
    url = '/login/'
    return HttpResponseRedirect(url)

