import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL)

    def was_published_recently(self):
        """
        True if the question ws published in the last 24 hours
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode(self):
        return self.choice_text
