import datetime

# from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from ..models import Question


def create_question(text="What's up?", offset=0):
    date = timezone.now + datetime.timedelta(days=offset)
    return Question.objects.create(question_text=text, pub_date=date)


class QuestionViewTests(TestCase):
    def test_index_view__no_questions(self):
        pass

    def test_index_view__future_question(self):
        pass

    def test_index_view__recent_question(self):
        """
        Recent (last 24 hours) questions should show up in the context
        """
        question = create_question("When did you poop recently?")
        response = self.client.get(reverse('polls:index'))
        import ipdb; ipdb.set_trace()
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view__past_question(self):
        pass

    def test_index_view__past_and_future_questions(self):
        pass

    def test_index_view__2_past_questions(self):
        pass
