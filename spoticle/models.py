from django.db import models

class QuizClip(models.Model):
	quiz = models.ForeignKey(Quiz)
	clip = models.ForeignKey(Clip)
	position = models.IntegerField()
	question = models.CharField(max_length=200)
	answers = models.CharField(max_length=200)

class Quiz(models.Model):
	path = models.CharField(max_length=200)

class Clips(models.Model):
	YTurl = models.CharField(max_length=200)
	startTime = models.IntegerField(default=0)
	endTime = models.IntegerField()
	duration = models.IntegerField()
	path = models.CharField(max_length=200)


