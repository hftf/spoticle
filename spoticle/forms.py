from django import forms
from spoticle.models import Quiz, QuizClip, QuizClip

class QuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		exclude = ('slug', 'path', 'pub_date', 'created_by')
		widgets = {
			'description': forms.Textarea(
				attrs={ 'placeholder': 'Enter description here', 'rows': 3 }),
		}
