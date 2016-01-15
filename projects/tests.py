from django.test import TestCase


class ProjectsHomeTemplateContextTestCase(TestCase):
	"""
	Test methods for projects_home page.
	"""
	fixtures = ["tester2.json"]
	
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
			'SignalHook', 
			'ZachSite'
		]
		
		contextProjectTitles = []
		for project in self.response.context['projectList']:
			contextProjectTitles.append(project.title)
		
		self.assertEqual(expectedProjectTitles, contextProjectTitles)


class ProjectsAboutTemplateContextTestCase(TestCase):
	"""
	Test methods for projects_about template.
	"""
	fixtures = ["tester2.json"]
	
	def setUp(self):
		"""
		Get AudioIO readme page.
		"""
		self.response = self.client.get('/projects/1/SignalHook/')
		
	def test_project_about_status_code_correct_template(self):
		"""
		Test that AudioIO readme page responds with status code = 200.
		"""
		self.assertEqual(self.response.status_code, 200)
		self.assertTemplateUsed(self.response, 'projects/project_about.html')
	
	def test_project_about_context_project_list(self):
		"""
		Test that AudioIO readme page has correct context data.
		"""
		# CONTEXT ITEM: projectList
		# expected:
		expectedProjectTitles = [
			'SignalHook', 
			'ZachSite'
		]
		# actual:
		contextProjectTitles = []
		for project in self.response.context['projectList']:
			contextProjectTitles.append(project.title)
		# assertion:
		self.assertEqual(expectedProjectTitles, contextProjectTitles)
		
		# CONTEXT ITEM: projectLen
		# expected:
		expectedProjectLen = '2'
		# actual:
		contextProjectLen = self.response.context['projectLen']
		# assertion:
		self.assertEqual(expectedProjectLen, contextProjectLen)
		
		# CONTEXT ITEM: curr_project
		# expected:
		expectedCurrProjTitle = "SignalHook"
		# actual:
		contextCurrProjTitle = self.response.context['curr_project'].title
		# assertion:
		self.assertEqual(expectedCurrProjTitle, contextCurrProjTitle)
		
		# CONTEXT ITEM: codeExampleList
		# expected:
		expectedCodeExampleFirstLine = "# Everything you will need here is located in the engine module.  Don't forget"
		# actual:
		contextCodeExamples = self.response.context['codeExampleList'][0].codetext
		# assertion:
		self.assertIn(expectedCodeExampleFirstLine, contextCodeExamples)
		
		# CONTEXT ITEM: readme_location
		# expected:
		expectedReadmeLocation = "projects/SignalHook/readme.html"
		# actual:
		contextReadmeLocation = self.response.context['readme_location']
		# assertion:
		self.assertEqual(expectedReadmeLocation, contextReadmeLocation)
		