from django.shortcuts import HttpResponse
# make sure to change the above to HttpResponse, it is not the default, and not doing so will prevent the view from rendering
from django.shortcuts import render

from .models import Question

def index(request):
    # this simple view will render the text above at the defined path.
    # return HttpResponse("Hello, world. You're at the polls index")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
