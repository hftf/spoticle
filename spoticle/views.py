from django.http import HttpResponse
from django.template import RequestContext, loader

from spoticle.models import Quiz

def index(request):
	quizzes = Quiz.objects.order_by('-pub_date')
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'quizzes': quizzes,
	})
	return HttpResponse(template.render(context))

def quiz(request, quiz_id):
	return HttpResponse('You\'re looking at quiz %s' % quiz_id)
