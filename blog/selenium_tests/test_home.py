from selenium import webdriver
import unittest
import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from blog.selenium_tests.pages import BlogHomePage
from blog.selenium_tests.base_tests import BlogBaseTests


class BaseHomeTests(BlogBaseTests, unittest.TestCase):
	"""
	Methods to test the blog home page.
	"""
	def setUp(self):
		"""
		Make the driver, get the page.
		"""
		self.driver = webdriver.Firefox()
		self.driver.get(BlogHomePage.URL)
		self.page = BlogHomePage(self.driver)
	
	def tearDown(self):
		"""
		Close driver.
		"""
		self.driver.close()
	
	def test_entries_present(self):
		"""
		Make sure at least one entry is displayed.
		"""
		self.assertTrue(self.page.get_entries())

if __name__ == '__main__':
	unittest.main()
	