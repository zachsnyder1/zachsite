from selenium import webdriver
import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from zachsite.selenium_tests.base_tests import BaseTests


class BlogBaseTests(BaseTests):
	"""
	Base blog tests.
	"""
	def test_section_header_present(self):
		"""
		Make sure the section header stuff is there...
		"""
		self.assertTrue(self.page.verify_header_section_visible())
		self.assertTrue(self.page.verify_header_backgnd_visible())
		self.assertTrue(self.page.verify_header_title_contains("Blog"))
	
	def test_blog_header_present(self):
		"""
		Make sure the blog header stuff is there...
		"""
		self.assertTrue(self.page.verify_blog_img_present())
		self.assertTrue(self.page.verify_blog_title_contains("About the Blog"))
		self.assertTrue(self.page.verify_blog_description_contains("enjoy"))
	