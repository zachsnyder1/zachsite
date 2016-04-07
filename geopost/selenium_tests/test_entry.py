import unittest
import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from zachsite.selenium_tests.pages import LoginPage, LogoutPage
from geopost.selenium_tests.pages import GeopostEntryPage
from selenium import webdriver


class EntryTests(unittest.TestCase):
	"""
	Methods to test the entry page of the app (create/edit/delete).
	"""
	def setUp(self):
		"""
		Make driver, page, sign in.
		"""
		with open('/etc/zachsite_test_creds.txt') as f:
			testCreds = f.readlines()
		self.driver = webdriver.Firefox()
		self.page = LoginPage(self.driver)
		self.page.enter_username(testCreds[0].strip())
		self.page.enter_password(testCreds[1].strip())
		self.page.login()
		self.page = GeopostEntryPage(self.driver)
	
	def tearDown(self):
		"""
		Close driver.
		"""
		self.page = LogoutPage(self.driver)
		self.assertTrue(self.page.verify_logged_out())
		self.driver.close()
	
	def test_attribution_displayed(self):
		"""
		Test that the attribution is displayed initially, and that it
		collapses after click.
		"""
		self.assertTrue(self.page.verify_attribution_displayed())
		self.page.toggle_attribution()
		self.assertTrue(self.page.verify_attribution_not_displayed())


if __name__ == '__main__':
	unittest.main()	
