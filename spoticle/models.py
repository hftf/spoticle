from django.db import models

class QuizClip(models.Model):
	quiz = models.ForeignKey(Quiz)
	clip = models.ForeignKey(Clip)
	position = models.IntegerField()
	question = models.CharField(max_length=200)
	answers = models.CharField(max_length=200)