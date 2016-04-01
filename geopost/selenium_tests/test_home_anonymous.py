import unittest
import os
import time
import sys
PACKAGE_ROOT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
import selenium_tests.pages as pages
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class HomeAnonymousTests(unittest.TestCase):
	"""
	Methods to test app homepage as anonymuos user.
	"""
	def setUp(self):
		"""
		Make the driver, get the page.
		"""
		self.driver = webdriver.Firefox()
		self.driver.get('http://127.0.0.1:8000/projects/geopost/')
		self.page = pages.GeopostHomeAnonymousPage(self.driver)
	
	def tearDown(self):
		"""
		Close driver.
		"""
		self.driver.close()
	
	def test_modal_open_and_close(self):
		self.assertFalse(self.page.is_info_displayed())
		self.page.click_point()
		self.assertTrue(self.page.is_info_displayed())
		self.page.dismiss_info()
		self.assertFalse(self.page.is_info_displayed())

if __name__ == '__main__':
	unittest.main()