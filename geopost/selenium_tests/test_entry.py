import unittest
import os
import sys
import time
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
		self.driver.get('http://127.0.0.1:8000/accounts/login/')
		self.page = LoginPage(self.driver)
		self.page.enter_username(testCreds[0].strip())
		self.page.enter_password(testCreds[1].strip())
		self.page.login()
		self.driver.get('http://127.0.0.1:8000/projects/geopost/entry')
		self.page = GeopostEntryPage(self.driver)
	
	def tearDown(self):
		"""
		Close driver.
		"""
		self.driver.get('http://127.0.0.1:8000/accounts/logout/')
		self.page = LogoutPage(self.driver)
		self.assertTrue(self.page.verify_logged_out())
		self.driver.close()
	
	def test_attribution_not_displayed(self):
		"""
		Test that the attribution is displayed initially, and that it
		collapses after click.
		"""
		self.assertTrue(self.page.verify_attribution_not_displayed())
		self.page.toggle_attribution()
		self.assertTrue(self.page.verify_attribution_displayed())
	
	def test_toolbar_open_and_close(self):
		"""
		Make sure the toolbar opens and closes when toggled.
		"""
		self.assertTrue(self.page.verify_toolbar_displayed())
		self.page.toggle_toolbar()
		self.assertTrue(self.page.verify_toolbar_not_displayed())
		self.page.toggle_toolbar()
		self.assertTrue(self.page.verify_toolbar_displayed())
	
	def test_create_new_entry(self):
		"""
		Draw point, fill in form, submit.
		"""
		self.page.toggle_draw()
		self.page.draw_point()
		time.sleep(3)


if __name__ == '__main__':
	unittest.main()	
