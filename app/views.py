from django.shortcuts import render
from .models import Quiz, Phy101
# Create your views here.
num = 0

def quizzes(request):
    query = Quiz.objects.all()
    return render(request, "quizzes.html", {"query": query})


def phy101(request):
    query = Phy101.objects.all()
    print(query)
    if request.method == "POST":
        quest = query[num]
        option_picked = request.POST["options"]
        correct_answer = quest.answer
        print(correct_answer)
    

    else:
        return render(request, "phy101.html", {"i": query[num]})


def new(request):
    return render(request, "new.html")
