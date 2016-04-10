import unittest
import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from zachsite.selenium_tests.base_tests import BaseTests
from zachsite.selenium_tests.pages import HomePage, LoginPage, LogoutPage
from selenium import webdriver


class HomePageTests(BaseTests, unittest.TestCase):
	"""
	Methods to test the ZachSite home page.
	"""
	def setUp(self):
		"""
		Driver, page..
		"""
		self.driver = webdriver.Firefox()
		self.driver.get(HomePage.URL)
		self.page = HomePage(self.driver)
	
	def tearDown(self):
		"""
		Close driver.
		"""
		self.driver.close()
	
	def test_qa_carousel(self):
		"""
		Test that the qa carousel is revolving and the answer
		text is changing.  Test that buttons work.
		"""
		t1 = self.page.get_answer_text()
		self.assertTrue(self.page.wait_for_qa_change())
		t2 = self.page.get_answer_text()
		self.assertNotEqual(t1, t2)
		self.page.click_qa_prev()
		self.assertTrue(self.page.wait_for_qa_change())
		t3 = self.page.get_answer_text()
		self.assertEqual(t1, t3)
		self.page.click_qa_next()
		self.assertTrue(self.page.wait_for_qa_change(time=3))
		self.page.click_qa_next()
		self.assertTrue(self.page.wait_for_qa_change(time=3))
		t4 = self.page.get_answer_text()
		self.assertNotEqual(t2, t4)
	
	def test_blurbs_present(self):
		"""
		Just make sure the blurbs are present.
		"""
		self.assertTrue(self.page.get_blurbs())
	
	def test_projects_div_matches_projects_dropdown(self):
		"""
		Make sure that all the projects in the dropdown menu
		are displayed in the projects section.
		"""
		dropdown = self.page.get_projs_from_dropdown()
		titles = self.page.get_project_titles()
		self.assertTrue(len(dropdown) == (len(titles) + 1))

if __name__ == '__main__':
	unittest.main()
