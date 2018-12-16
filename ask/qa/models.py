from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    likes = models.ManyToMany.Field(User, related_name='likes_set')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.PROTECT)
    author = models.ForeignKey(User, null=False, on_delete=models.PROTECT)

# Create your models here.
