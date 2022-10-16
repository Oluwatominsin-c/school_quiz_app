from django.shortcuts import render
from .models import Quiz
# Create your views here.

def quizzes(request):
    query = Quiz.objects.all()
    return render(request, "quizzes.html", {"query": query})


def phy101(request):
    return render(request, "phy101.html")

