import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently__future(self):
        """
        should be false for future questions
        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently__2_days_ago(self):
        """
        should be false for >1 day old questions
        """

        time = timezone.now() - datetime.timedelta(days=2)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently__12_hours_ago(self):
        """
        should be true for < 1 day old questions
        """

        time = timezone.now() - datetime.timedelta(hours=12)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), True)
