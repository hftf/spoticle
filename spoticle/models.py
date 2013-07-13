from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Quiz(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=40, unique=True) # generated
	description = models.CharField(max_length=1000, blank=True)
	require_in_order = models.BooleanField()
	timer_seconds = models.TimeField()
	tags = models.CharField(max_length=400, blank=True) # to make m2m

	question = models.CharField(max_length=200, blank=True)
	answers = models.CharField(max_length=200, blank=True)

	path = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published') # or never
	created_by = models.ForeignKey(User)

	def __unicode__(self):
		return "%s (%s)" % (self.name, self.id)

	def save(self, *args, **kwargs):
		"""
		TODO: check if slug is a dupe
		"""
		if not self.slug:
			self.slug = slugify(self.name)
		super(Quiz, self).save()

	class Meta:
		verbose_name_plural = "Quizzes"
		ordering = ['-pub_date']

class QuizAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ('name', ) }

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
	question = models.CharField(max_length=200, blank=True)
	answers = models.CharField(max_length=200)

	def __unicode__(self):
		return "[%s] %s (%s)" % (self.position, self.quiz, self.clip)

	class Meta:
		ordering = ['position']
