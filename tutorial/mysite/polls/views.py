from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import  get_object_or_404
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # return HttpResponse(template.render(context, request))



def detail(request, question_id):
    # try:
    #     Question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("そんなのない！")
    # return HttpResponse("あなたは%s番目の質問をみてます" % question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    # response = ("あなたは%s番目の質問の結果を見ています" )
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question" : question})

def vote(request, question_id):
    # return HttpResponse("あなたは%s番目の質問に投票しました。" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_massage": "えらんでなくね？",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# Create your views here.
