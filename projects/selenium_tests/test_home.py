import unittest
import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from projects.selenium_tests.base_tests import BaseProjectsTests
from projects.selenium_tests.pages import ProjectsHomePage
from selenium import webdriver


class ProjectsHomeTests(BaseProjectsTests, unittest.TestCase):
	"""
	Methods to test projects homepage.
	"""
	def setUp(self):
		"""
		Make the driver, get the page.
		"""
		self.driver = webdriver.Firefox()
		self.driver.get(ProjectsHomePage.URL)
		self.page = ProjectsHomePage(self.driver)
	
	def tearDown(self):
		"""
		Close driver.
		"""
		self.driver.close()
	
	def test_all_projects_displayed(self):
		"""
		Make sure that all the projects in the dropdown menu
		are displayed in the projects section.
		"""
		dropdown = self.page.get_projs_from_dropdown()
		displayed = self.page.get_projects_displayed()
		self.assertTrue(len(dropdown) == (len(displayed) + 1))
	
if __name__ == '__main__':
	unittest.main()
	