from django.contrib import admin
from spoticle.models import Quiz, QuizAdmin, Clip, QuizClip

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Clip)
admin.site.register(QuizClip)
