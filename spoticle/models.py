from django.db import models

class Quiz(models.Model):
	path = models.CharField(max_length=200)

class Clip(models.Model):
	youtube_url = models.CharField(max_length=200)
	start_time = models.IntegerField(default=0)
	end_time = models.IntegerField()
	duration = models.IntegerField()
	path = models.CharField(max_length=200)

class QuizClip(models.Model):
	quiz = models.ForeignKey(Quiz)
	clip = models.ForeignKey(Clip)
	position = models.IntegerField()
	question = models.CharField(max_length=200)
	answers = models.CharField(max_length=200)
