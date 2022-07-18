from django.contrib import admin
from .models import Category, Question,Option,Answer, Quiz

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    exclude = ['slug']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','category',]
    list_display_links = ['question','category',]
    list_filter = ['category']

class OptionAdmin(admin.ModelAdmin):
    list_display = ['option','question','is_answer','get_category']
    list_display_links = ['option','is_answer','question']
    list_filter = ['question','is_answer']

    def get_category(self, obj):
            return obj.question.category

    get_category.admin_order_field  = 'category'
    get_category.short_description = 'Category Name'


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer','question',]
    list_display_links = ['answer']
    list_filter = ['question']

class QuizAdmin(admin.ModelAdmin):
    list_display = ['question']
    list_display_links = ['question']
    list_filter = ['question']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Option,OptionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Quiz,QuizAdmin)