from django.contrib import admin
from questions.models import Question, Answer
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["content", "author","created","modified"]

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ["author", "body","created","modified"]

admin.site.register(Answer, AnswerAdmin)
