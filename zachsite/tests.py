from django.test import TestCase


class ZachsiteTemplateContextTestCase(TestCase):
	"""
	Test methods for index page. 
	"""
	fixtures = ["tester.json"]
	
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
		expectedQuestions = [
			'Zach?  Who is that?',
			'Where does he come from?',
			'Does he do anything special?',
			'What does he want?'
		]
		expectedAnswers = [
			'Zach is a pretty standup, friendly dude.',
			'A sleepy little town next to some hills in Colorado.',
			'Sure.  In fact, he has several skills.',
			'A job.  Pure and simple.'
		]
		
		contextQuestions, contextAnswers = [], []
		for qAObj in self.response.context['QAs']:
			contextQuestions.append(qAObj.question)
			contextAnswers.append(qAObj.answer)
		
		self.assertEqual(expectedQuestions, contextQuestions)
		self.assertEqual(expectedAnswers, contextAnswers)
	
	def test_index_context_projects(self):
		"""
		Test that index page has all projects from fixture.
		"""
		expectedTitles = [
			'AudioIO', 'ZachSite'
		]
		
		contextTitles = []
		for projObj in self.response.context['projectList']:
			contextTitles.append(projObj.title)
		
		self.assertEqual(expectedTitles, contextTitles)
	
	