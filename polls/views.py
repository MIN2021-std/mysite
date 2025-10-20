from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.db.models import F


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    
    loader.get_template("polls/index.html")
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(output)
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
    # POST와 Redirect는 하나의 세트임. POST로 호출되면 Response는 Redict로 해줌.
    # url 하드 코딩하지 않기 위해 reverse를 사용해서 앱 이름과 url 이름 사용