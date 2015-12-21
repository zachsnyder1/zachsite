from django.test import TestCase


class ProjectsHomeTemplateContextTestCase(TestCase):
	"""
	Test methods for projects_home page.
	"""
	fixtures = ["fixture1.json"]
	
	def setUp(self):
		"""
		Get projects_home page.
		"""
		self.response = self.client.get('/projects/')
	
	def test_projects_home_status_code_correct_template(self):
		"""
		Test that projects_home page responds with status code = 200.
		"""
		self.assertEqual(self.response.status_code, 200)
		self.assertTemplateUsed(self.response, 'projects/projects_home.html')
	
	def test_projects_home_context_project_list(self):
		"""
		Test that projects_home page has all projects from fixture.
		"""
		expectedProjectTitles = [
			'AudioIO',
			'KayaIO',
			'Putin App'
		]
		
		contextProjectTitles = []
		for project in self.response.context['projectList']:
			contextProjectTitles.append(project.title)
		
		self.assertEqual(expectedProjectTitles, contextProjectTitles)