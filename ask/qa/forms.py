from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)

    def clean_text(self):
        text = self.cleaned_data['text']
        return text
    def clean_title(self):
        title = self.cleaned_data['title']
        return title

    def save(self):
        """self.cleaned_data['author'] = self._user"""
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean_text(self):
        text = self.cleaned_data['text']
        return text
    def clean_question(self):
        question = self.cleaned_data['question']
        return question

    def save(self):
        """self.cleaned_data['author'] = self._user"""
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


