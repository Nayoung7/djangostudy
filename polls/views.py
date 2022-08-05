from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# Create your views here.
def index(request):
    # 1. Basic view
    # return HttpResponse("Hello, world. You're at the polls index.")

    # 2. Actually do something
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]     # 출판일자로 정렬하여 5개까지만 데이터 가져오기
    # output = ', ' .join([q.question_text for q in latest_question_list])    # 5개를 콤마로 연결하겠다.
    # return HttpResponse(output)

    # 3. Use the template
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]   
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 4. Use the shortcut - render
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 1
    # return HttpResponse("You're looking at question %s." % question_id)

    # 2
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question' : question})

    # 3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    # 1
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    # 2
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})

def vote(request, question_id):
    # 1
    # return HttpResponse("You're voting on question %s." % question_id)

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question' : question,
                'error_message' : "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# (3) view 내부의 index 함수에서는 Hello, world 라는 응답을 클라이언트에게 전달해줌