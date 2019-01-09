from django import forms
from django.contrib.auth.models import User
#from django.contrib.sessions.models import Session
#from django.contrib.auth import authenticate, login
from django.urls import reverse
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    def __init__(self, user, *args, **kwargs):
        self._user = user
        super(AskForm, self).__init__(*args, **kwargs)
    def clean_text(self):
        text = self.cleaned_data['text']
        return text
    def clean_title(self):
        title = self.cleaned_data['title']
        return title
    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
    def __init__(self, user, *args, **kwargs):
        self._user = user
        super(AnswerForm, self).__init__(*args, **kwargs)
    def clean_text(self):
        text = self.cleaned_data['text']
        return text
    def clean_question(self):
        question = self.cleaned_data['question']
        return question
    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
    def clean_username(self):
        username = self.cleaned_data['username']
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        return email
    def clean_password(self):
        password = self.cleaned_data['password']
        return password
    def save(self):
        user = User.objects.create_user(self.clean_username(), self.clean_email(), self.clean_password())
        user.save()
        return user

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    def clean_username(self):
        username = self.cleaned_data['username']
        return username
    def clean_password(self):
        password = self.cleaned_data['password']
        return password
    def save(self):
        user = User(**self.cleaned_data)
        return user

