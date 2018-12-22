from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, related_name='likes_set')
    def get_url(self):
        return reverse('question', kwargs={'slug': self.slug})
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    author = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, null=False, on_delete=models.PROTECT)



# Create your models here.
