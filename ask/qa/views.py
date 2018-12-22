from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from django.core.paginator import Paginator

@require_GET
def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

def new_question_list(request):
    new_questions = Question.objects.new()
    paginate(request, new_questions)
    paginator.baseurl = '/?page='
    return render(request, 'qa/templates/new_questions.html', {
        new_questions:   page.object_list,
        paginator:  paginator, page: page,
    })

def popular_question_list(request):
    popular_questions = Question.objects.popular()
    paginate(request, popular_questions)
    paginator.baseurl = '/popular/?page='
    return render(request, 'qa/templates/popular_questions.html', {
        popular_questions:  page.object_list,
        paginator:  paginator, page: page,
    })

def question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    try:
        answers = question.answers.all()[:]
    except Answer.DoesNotExist:
        answers = None
    return render(request, 'qa/templates/question.html', {
        'question': question,
        'answers':   answers,
    })


# Create your views here.
