from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.views import generic

from spoticle.models import Quiz, QuizClip, Clip

def index(request):
	quizzes = Quiz.objects.order_by('-pub_date')
	context = {
		'quizzes': quizzes,
	}
	return render(request, 'index.html', context)

class IndexView(generic.ListView):
	model = Quiz
	template_name = 'index.html'
	context_object_name = 'quizzes'

class DetailView(generic.DetailView):
	model = Quiz
	template_name = 'quiz.html'
	context_object_name = 'quiz'

class UpdateView(generic.edit.UpdateView):
	model = Quiz
	template_name = 'quiz.html'

def quiz(request, quiz_id):
	quiz = get_object_or_404(Quiz, pk=quiz_id)
	return render(request, 'quiz.html', { 'quiz': quiz })

def clip(request, clip_id):
	clip = get_object_or_404(Clip, pk=clip_id)
	return render(request, 'clip.html', { 'clip': clip })