from rest_framework import serializers
from .models import Category, Question,Option,Answer,Quiz

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category','slug']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question']

class OptionsSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.question')
    class Meta:
        model = Option
        fields = ['id','question','option','is_answer']

class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='question.id')
    category = serializers.CharField(source='question.category')
    question = serializers.CharField()
    answer = serializers.CharField()
    class Meta:
        model = Answer
        fields = ['id','category','question','answer']

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id','option','is_answer']

class QuizSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='question.id')
    question = serializers.CharField()
    options = OptionSerializer(read_only=True , many=True)
    class Meta:
        model = Quiz
        fields = ['id','question','options']