"""
Model based tests for the zachsite app.
"""
from django.test import TestCase


class ZachsiteTemplateContextTestCase(TestCase):
    """
    Test methods for index page.
    """
    fixtures = ["tester2.json"]

    def setUp(self):
        """
        Get index page.
        """
        self.response = self.client.get('/')

    def test_index_status_code_correct_template(self):
        """
        Test that index page responds with status code = 200.
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'zachsite/index.html')

    def test_index_context_question_and_answer(self):
        """
        Test that index page has all Q&A from fixture.
        """
        expected_questions = [
            'Zach?  Who is that?',
            'Where does he come from?',
            'Does he do anything special?',
            'What does he want?'
        ]
        expected_answers = [
            'Zach is a pretty standup, friendly person.',
            'A sleepy little town next to some hills in Colorado.',
            'Sure.  In fact, he has several skills.',
            'A job.  Pure and simple.'
        ]

        context_questions, context_answers = [], []
        for qa_obj in self.response.context['QAs']:
            context_questions.append(qa_obj.question)
            context_answers.append(qa_obj.answer)

        self.assertEqual(expected_questions, context_questions)
        self.assertEqual(expected_answers, context_answers)

    def test_index_context_projects(self):
        """
        Test that index page has all projects from fixture.
        """
        expected_titles = [
            'SignalHook',
            'ZachSite'
        ]

        context_titles = []
        for project_obj in self.response.context['projectList']:
            context_titles.append(project_obj.title)

        self.assertEqual(expected_titles, context_titles)
