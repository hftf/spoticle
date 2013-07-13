from django.db import models

class Quiz(models.Model):
	name = models.CharField(max_length=200)
	path = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Quizzes"

class Clip(models.Model):
	youtube_url = models.CharField(max_length=200)
	start_seconds = models.IntegerField(default=0)
	end_seconds = models.IntegerField()
	duration = models.IntegerField()
	path = models.CharField(max_length=200)

class QuizClip(models.Model):
	quiz = models.ForeignKey(Quiz)
	clip = models.ForeignKey(Clip)

	position = models.IntegerField()
	question = models.CharField(max_length=200)
	answers = models.CharField(max_length=200)

