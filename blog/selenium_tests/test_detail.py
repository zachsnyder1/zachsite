from selenium import webdriver
import unittest
import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from blog.selenium_tests.pages import BlogHomePage, BlogDetailPage
from blog.selenium_tests.base_tests import BlogBaseTests


class BlogDetailTests(BlogBaseTests, unittest.TestCase):
	"""
	Methods to test the blog detail pages.
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
	
	def test_entry_elements_present(self):
		"""
		Make sure title, tagline, and text are all there.
		"""
		self.page.click_an_entry()
		self.page = BlogDetailPage(self.driver)
		self.assertTrue(self.page.verify_path())
		self.assertTrue(self.page.verify_title_present())
		self.assertTrue(self.page.verify_tagline_present())
		self.assertTrue(self.page.verify_body_present())

if __name__ == '__main__':
	unittest.main()
	