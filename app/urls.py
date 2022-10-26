from django.urls import path
from .views import quizzes, phy101, new

urlpatterns = [
    path("", quizzes, name="quizzes"),
    path("phy101/", phy101, name="phy101"),
    path("new/", new)
]
