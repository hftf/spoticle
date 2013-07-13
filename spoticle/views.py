from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render

from spoticle.models import Quiz

def index(request):
	quizzes = Quiz.objects.order_by('-pub_date')
	context = {
		'quizzes': quizzes,
	}
	return render(request, 'index.html', context)

def quiz(request, quiz_id):
	return HttpResponse('You\'re looking at quiz %s' % quiz_id)
