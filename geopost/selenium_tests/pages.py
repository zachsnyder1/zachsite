import os
import sys
from .locators import HomeLocators
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from zachsite.selenium_tests.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GeopostPageBase(BasePage):
	"""
	Defines methods common to both home page and entry page
	of the app.
	"""
	# ---------------------------------------------------------------
	# ---------------------- GENERAL ACTION(S) ----------------------
	# ---------------------------------------------------------------
	def toggle_attribution(self):
		"""
		Click the attribution button to open/close it.
		"""
		attrBtn = self.driver.find_element(*HomeLocators.ATTR_BTN)
		attrBtn.click()
	
	# ---------------------------------------------------------------
	# ------------------- VERIFICATION METHODS ----------------------
	# ---------------------------------------------------------------
	def verify_attribution_displayed(self):
		"""
		Wait for attribution to be displayed.
		"""
		attribution = self.driver.find_element(*HomeLocators.ATTRIBUTION)
		c = 'ol-collapsed' # the class indicating that attr is collapsed
		condition = lambda driver: c in attribution.get_attribute('class')
		return self.verify(condition)
	
	def verify_attribution_not_displayed(self):
		"""
		Wait for attribution to be not displayed.
		"""
		attribution = self.driver.find_element(*HomeLocators.ATTRIBUTION)
		c = 'ol-collapsed' # collapsed class
		condition = lambda driver: c not in attribution.get_attribute('class')
		return self.verify(condition)
	
	def verify_toolbar_present(self):
		"""
		Wait for toolbar to be present.
		"""
		condition = EC.presence_of_element_located(HomeLocators.TOOLBAR)
		return self.verify(condition)
	
	def verify_toolbar_absent(self):
		"""
		True if toolbar is absent.
		"""
		return self.absent(HomeLocators.TOOLBAR)
	
	

class GeopostHomePage(GeopostPageBase):
	"""
	Page objects for Geopost home page.
	"""
	def __init__(self, driver):
		"""
		Get the page...
		"""
		super().__init__(driver)
		self.driver.get('http://127.0.0.1:8000/projects/geopost/')
	# ---------------------------------------------------------------
	# ---------------------- GENERAL ACTIONS ------------------------
	# ---------------------------------------------------------------
	def get_img_src(self):
		"""
		Get the src attribute of the entry img element.
		"""
		elem = self.driver.find_element(*HomeLocators.ENTRY_IMG)
		return elem.get_attribute('src')
	
	def open_entry(self):
		"""
		Click on an entry in the map to display its content.
		"""
		script = '$(document).ready(function() {' + \
			'var feat = OL_OBJ.entriessource.getFeatures()[0];' + \
			'OL_OBJ.select.getFeatures().push(feat);' + \
			'OL_OBJ.select.dispatchEvent(\'select\');' + \
			'});'
		self.driver.execute_script(script)
	
	def dismiss_info(self):
		"""
		Close the info modal.
		"""
		closebtn = self.driver.find_element(*HomeLocators.CLOSE_BTN)
		closebtn.click()
	
	# ---------------------------------------------------------------
	# ------------------- VERIFICATION METHODS ----------------------
	# ---------------------------------------------------------------
	def verify_entry_displayed(self):
		"""
		Return True if info modal is displayed.
		"""
		info = self.driver.find_element(*HomeLocators.INFO_MODAL)
		return self.verify(EC.visibility_of(info))
	
	def verify_entry_hidden(self):
		"""
		Return True if info modal is not displayed.
		"""
		condition = EC.invisibility_of_element_located(HomeLocators.INFO_MODAL)
		return self.verify(condition)
	
	def verify_title_empty(self):
		"""
		Wait for title to be empty. 
		""" 
		title = self.driver.find_element(*HomeLocators.ENTRY_TITLE)
		return self.verify(lambda driver: title.text == '')
	
	def verify_title_not_empty(self):
		"""
		Wait for title to be not empty.
		"""
		title = self.driver.find_element(*HomeLocators.ENTRY_TITLE)
		return self.verify(lambda driver: title.text != '')
	
	def verify_body_empty(self):
		"""
		Wait for body to be empty.
		"""
		body = self.driver.find_element(*HomeLocators.ENTRY_BODY)
		return self.verify(lambda driver: body.text == '')
	
	def verify_body_not_empty(self):
		"""
		Wait for body to be not empty.
		"""
		body = self.driver.find_element(*HomeLocators.ENTRY_BODY)
		return self.verify(lambda driver: body.text != '')
	
	def verify_img_load(self):
		"""
		Wait for the image to load.
		"""
		return self.verify(lambda driver: self.get_img_src() != '', time=8)
	
	def verify_edit_button_present(self):
		"""
		Wait for edit button to be present.
		"""
		condition = EC.presence_of_element_located(HomeLocators.EDIT_BTN)
		return self.verify(condition)
	
	def verify_edit_button_absent(self):
		"""
		True if edit button is absent.
		"""
		return self.absent(HomeLocators.EDIT_BTN)
	
	def verify_delete_button_present(self):
		"""
		Wait for delete button to be present.
		"""
		condition = EC.presence_of_element_located(HomeLocators.DELETE_BTN)
		return self.verify(condition)
	
	def verify_delete_button_absent(self):
		"""
		True if delete button is absent.
		"""
		return self.absent(HomeLocators.DELETE_BTN)


class GeopostEntryPage(GeopostPageBase):
	"""
	
	"""
	def __init__(self, driver, q=''):
		"""
		Get the page...
		"""
		super().__init__(driver)
		self.driver.get('http://127.0.0.1:8000/projects/geopost/entry/' + q)
