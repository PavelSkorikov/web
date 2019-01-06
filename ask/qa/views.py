from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.core.paginator import Paginator




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

def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'askform.html', {
        'form': form
    })
def answer_add(request, pk):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = '/question/' + pk + '/'
            return HttpResponseRedirect(url)
    else:
        question = get_object_or_404(Question, id=pk)
        answers = question.answer_set.all()
        form = AnswerForm(initial={'question': question.id})
    return render(request, 'question.html', {
        'pk': pk,
        'question': question,
        'answers': answers,
        'form': form
    })
