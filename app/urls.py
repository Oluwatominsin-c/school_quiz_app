from django.urls import path
from .views import quizzes, phy101

urlpatterns = [
    path("", quizzes, name="quizzes"),
    path("phy101/", phy101, name="phy101"),
]
