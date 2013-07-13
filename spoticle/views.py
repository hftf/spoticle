from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404

from spoticle.models import Quiz, QuizClip, Clip

def index(request):
	quizzes = Quiz.objects.order_by('-pub_date')
	context = {
		'quizzes': quizzes,
	}
	return render(request, 'index.html', context)

def quiz(request, quiz_id):
	quiz = get_object_or_404(Quiz, pk=quiz_id)
	return render(request, 'quiz.html', { 'quiz': quiz })

def clip(request, clip_id):
	clip = get_object_or_404(Clip, pk=clip_id)
	return render(request, 'clip.html', { 'clip': clip })