from django.urls import path
from .views import quizzes, page, new, question

urlpatterns = [
    path("", quizzes, name="quizzes"),
    path("page/", page, name="page"),
    path("page/<str:pk>", question, name="question"),
]
