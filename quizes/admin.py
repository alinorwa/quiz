from django.contrib import admin
from .models import *

# Register your models here.
class AnswerInlin(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlin]

admin.site.register(Question , QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Result)