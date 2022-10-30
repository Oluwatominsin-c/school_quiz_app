from django.shortcuts import render, redirect
from .models import Quiz, Phy101, Phy103, Che101, Gns101
# Create your views here.

def quizzes(request):
    query = Quiz.objects.all()
    return render(request, "quizzes.html", {"query": query})


def page(request):
    return render(request, "page.html")

def question(request, pk):
    print(pk)
    if pk == "PHY103":
        query = Phy103.objects.all()
        return render(request, "page.html", {"query": query, "name": "PHY103"})
    elif pk == "PHY101":
        return redirect("/")
    elif pk == "CHE101":
        return redirect("/")
    elif pk == "GNS101":
        return redirect("/")
    else:
        return redirect("/")

def new(request):
    return render(request, "new.html")
