import unittest
import os
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
		self.page = pages.GeopostHomePage(self.driver)
	
	def tearDown(self):
		"""
		Close driver.
		"""
		self.driver.close()
	
	def test_modal_open_and_close(self):
		"""
		Test that the info modal opens when an entry is clicked,
		and then closes when the close button is clicked.
		"""
		self.assertTrue(self.page.verify_entry_hidden())
		self.page.open_entry()
		self.assertTrue(self.page.verify_entry_displayed())
		self.page.dismiss_info()
		self.assertTrue(self.page.verify_entry_hidden())
	
	def test_info_displayed(self):
		"""
		Test that when an entry is clicked, the title and body
		elements of the info modal are populated with information,
		and that a photo is eventually loaded.
		"""
		# First, they should have no info:
		self.assertTrue(self.page.verify_title_empty())
		self.assertTrue(self.page.verify_body_empty())
		self.assertFalse(self.page.get_img_src())
		# Open an entry:
		self.page.open_entry()
		# Now the title and body should be present:
		self.assertTrue(self.page.verify_title_not_empty())
		self.assertTrue(self.page.verify_body_not_empty())
		# ...and the image should load in a few seconds:
		self.assertTrue(self.page.verify_img_load())
	
	def test_auth_elements_not_present(self):
		"""
		Test that Django correctly omitted the toolbar and edit/delete
		buttons for anonymous user.
		"""
		self.assertTrue(self.page.verify_toolbar_absent())
		self.assertTrue(self.page.verify_edit_button_absent())
		self.assertTrue(self.page.verify_delete_button_absent())
		

if __name__ == '__main__':
	unittest.main()