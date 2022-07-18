from unicodedata import category
from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    category = models.CharField(max_length=50,unique=True)
    slug = models.CharField(max_length=50)

    def save(self):
        self.slug = slugify(self.category)
        return super().save()

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'

class Question(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    question = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.question

class Option(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    option = models.CharField(max_length=20)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.option

    def save(self):
        if self.is_answer:
            if Option.objects.filter(question=self.question).filter(is_answer=True).exists():
                former_answer = Option.objects.filter(question=self.question).filter(is_answer=True)[0]
                former_answer.is_answer = False
                former_answer.save()
            
            super().save()

            if Answer.objects.filter(question=self.question).exists():
                prev_answer = Answer.objects.filter(question=self.question)[0]
                prev_answer.answer = self
                prev_answer.save()

            else:
                Answer.objects.create(question=self.question,answer=self)
        
        super().save()
        
        quiz,created = Quiz.objects.get_or_create(question=self.question)

        if created:
            quiz = Quiz.objects.get(question=self.question)
            quiz.options.add(self)
        
        else:
            quiz.options.add(self)

        return super().save()

class Answer(models.Model):
    question = models.OneToOneField(Question,on_delete=models.CASCADE,blank=False,null=False)
    answer = models.OneToOneField(Option,on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return self.answer.option

class Quiz(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    options = models.ManyToManyField(Option,related_name='options')

    def __str__(self):
        return self.question.question