from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from lookup_functions import lookup
from spoticle.models import Quiz, QuizClip

@dajaxice_register
def check_answer(request, client_answer, quiz_id):
	print request, client_answer
	quiz = Quiz.objects.get(pk=quiz_id)
	answers = [quizclip.answers for quizclip in quiz.quizclip_set.all()]


	corrects = lookup(answers, client_answer, None, True)
	return simplejson.dumps(corrects)
