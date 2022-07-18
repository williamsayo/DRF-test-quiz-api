from django.urls import path
from .views import CategoryAnswersApi,AnswerApi, OptionApi, CategoryApi,QuestionApi,QuizApi, QuizByCategoryApi, UpdateOptionApi, UpdateQuestionApi

urlpatterns = [
    path('category/',CategoryApi.as_view()),
    path('question/',QuestionApi.as_view()),
    path('question/update/<pk>/',UpdateQuestionApi.as_view()),
    path('option/',OptionApi.as_view()),
    path('option/update/<pk>/',UpdateOptionApi.as_view()),
    path('answer/',AnswerApi.as_view()),
    path('answer/<str>/',CategoryAnswersApi.as_view()),
    path('quiz/',QuizApi.as_view()),
    path('quiz/<str>/',QuizByCategoryApi.as_view()),
]