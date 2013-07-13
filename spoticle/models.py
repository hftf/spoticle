from django.db import models

class Quiz(models.Model):
	name = models.CharField(max_length=200)
	path = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return "%s (%s)" % (self.name, self.id)

	def ordered_quizclips(self):
		return self.quizclip_set.order_by("position")

	class Meta:
		verbose_name_plural = "Quizzes"

class Clip(models.Model):
	name = models.CharField(max_length=200)
	path = models.CharField(max_length=200)
	youtube_url = models.CharField(max_length=200)
	start_seconds = models.IntegerField(default=0)
	end_seconds = models.IntegerField()
	duration = models.IntegerField()

	def __unicode__(self):
		return "%s (%s)" % (self.name, self.id)

class QuizClip(models.Model):
	quiz = models.ForeignKey(Quiz)
	clip = models.ForeignKey(Clip)

	position = models.IntegerField()
	question = models.CharField(max_length=200)
	answers = models.CharField(max_length=200)

	def __unicode__(self):
		return "[%s] %s (%s)" % (self.position, self.quiz, self.clip)

