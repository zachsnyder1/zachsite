from selenium import webdriver
import os
import sys
PACKAGE_ROOT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from projects.selenium_tests.pages import ProjectsHomePage
from zachsite.selenium_tests.base_tests import BaseTests


class BaseProjectsTests(BaseTests):
	"""
	Methods to test the projects banner and subnav functionality.
	"""
	def test_projects_banner(self):
		"""
		Test that the banner exists...
		"""
		self.assertTrue(self.page.verify_header_section_visible())
		self.assertTrue(self.page.verify_header_backgnd_visible())
		self.assertTrue(self.page.verify_header_title_visible())
	
	def test_projects_subnav(self):
		"""
		Test that the subnav is present, and that it drops down.
		"""
		pHome = ProjectsHomePage(self.driver)
		if pHome.verify_path(): # No subnav to test on projects home page
			return
		else:
			self.assertTrue(self.page.verify_subnav_visible(time=4))
	