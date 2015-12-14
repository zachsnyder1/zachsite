from django.test import TestCase
from zachsite.models import QuestionAndAnswer, Blurb


class ZachsiteTemplateContextTestCase(TestCase):
	"""
	Test methods for index page.
	"""
	fixtures = ["fixture3.json"]
	
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
			'A miserable little nightmare of a town in the heart of Colorado.',
			'Sure.  In fact, he has several skills.',
			'A job.  Pure and simple.'
		]
		
		contextQuestions, contextAnswers = [], []
		for qAObj in self.response.context['QAs']:
			contextQuestions.append(qAObj.question)
			contextAnswers.append(qAObj.answer)
		
		self.assertEqual(expectedQuestions, contextQuestions)
		self.assertEqual(expectedAnswers, contextAnswers)
	
	def test_index_context_blurbs(self):
		"""
		Test that index page has all blurbs from fixture.
		"""
		expectedTitles = [
			'About me',
			'About You',
			'About Our Children'
		]
		expectedText = [
			'I\'m a wild horse grazing on a high pasture, nostrils flared, staring down the thunderhead.  I\'m a chilly duck on the placid surface of a lost lake somewhere tens of kilometers from the nearest gulag, content to eat algae and meditate, steadfast, on the atrocities of humanity, I lose myself in eternity; an owl overhead hoots, I ruffle my feathers.  I\'m the rock beneath their boots, and the dust between their teeth.  They will shout, assail, congregate, excavate, fasten, hoist, rebel, ascend, raze; I will mop and drain the blood they spill.',
			'I\'m a wild horse grazing on a high pasture, nostrils flared, staring down the thunderhead.  I\'m a chilly duck on the placid surface of a lost lake somewhere tens of kilometers from the nearest gulag, content to eat algae and meditate, steadfast, on the atrocities of humanity, I lose myself in eternity; an owl overhead hoots, I ruffle my feathers.  I\'m the rock beneath their boots, and the dust between their teeth.  They will shout, assail, congregate, excavate, fasten, hoist, rebel, ascend, raze; I will mop and drain the blood they spill.',
			'I\'m a wild horse grazing on a high pasture, nostrils flared, staring down the thunderhead.  I\'m a chilly duck on the placid surface of a lost lake somewhere tens of kilometers from the nearest gulag, content to eat algae and meditate, steadfast, on the atrocities of humanity, I lose myself in eternity; an owl overhead hoots, I ruffle my feathers.  I\'m the rock beneath their boots, and the dust between their teeth.  They will shout, assail, congregate, excavate, fasten, hoist, rebel, ascend, raze; I will mop and drain the blood they spill.'
		]
		
		contextTitles, contextText = [], []
		for blurbObj in self.response.context['blurbList']:
			contextTitles.append(blurbObj.title)
			contextText.append(blurbObj.text)
		
		self.assertEqual(expectedTitles, contextTitles)
		self.assertEqual(expectedText, contextText)
	
	def test_index_context_projects(self):
		"""
		Test that index page has all projects from fixture.
		"""
		expectedTitles = [
			'AudioIO',
			'KayaIO',
			'Putin App'
		]
		
		contextTitles = []
		for projObj in self.response.context['projectList']:
			contextTitles.append(projObj.title)
		
		self.assertEqual(expectedTitles, contextTitles)
	
	