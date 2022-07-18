from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveDestroyAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Question,Option,Answer,Quiz
from .serializers import QuestionSerializer,OptionsSerializer,AnswerSerializer,QuizSerializer,CategorySerializer

class CategoryApi(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionApi(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UpdateQuestionApi(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class OptionApi(ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionsSerializer

class UpdateOptionApi(RetrieveDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionsSerializer

class AnswerApi(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class CategoryAnswersApi(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def list(self, *args, **kwargs):
        cat = get_object_or_404(Category,slug=kwargs['str'])
        answer = Answer.objects.filter(question__category=cat)
        serializer = self.get_serializer(answer, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class QuizApi(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizByCategoryApi(ListAPIView):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def list(self, *args, **kwargs):
        cat = get_object_or_404(Category,slug=kwargs['str'])
        quiz = Quiz.objects.filter(question__category=cat)
        serializer = self.get_serializer(quiz, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
