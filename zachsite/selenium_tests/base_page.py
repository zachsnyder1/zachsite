from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
from .base_locators import BaseLocators

class BasePage:
	"""
	Base class for page objects.
	"""
	EXPECTED_PATH = None
	
	def __init__(self, driver):
		self.driver = driver
	
	def verify(self, condition, time=2):
		"""
		Return True if condition is verified within time.
		"""
		try:
			WebDriverWait(self.driver, time).until(condition)
			return True
		except TimeoutException:
			return False
	
	def get_element_if_present(self, locator, time=2):
		"""
		Wait for element to be present in DOM, return element, or
		None if it never shows up.
		"""
		p = self.verify(EC.presence_of_element_located(locator), time=time)
		if p:
			return self.driver.find_element(*locator)
		else:
			return None
	
	def get_element_if_visible(self, locator, timeP=2, timeV=2):
		"""
		Wait for presence in DOM, get element, wait for it to be visible,
		return element, or None if it is either not present or not visible.
		"""
		element = self.get_element_if_present(locator, time=timeP)
		if element:
			v = self.verify(EC.visibility_of(element), time=timeV)
			if v:
				return element
			else:
				pass
		else:
			pass
		# If either condition is false, return None
		return None
	
	def absent(self, locator):
		"""
		Return True if element is absent, else False.
		"""
		try:
			el = self.driver.find_element(*locator)
			return False
		except NoSuchElementException:
			return True
	
	def verify_path(self, time=2):	
		"""
		True if expected path matches the current path.
		"""
		u = urlparse(self.driver.current_url)
		condition = lambda driver: self.__class__.EXPECTED_PATH == u.path
		return self.verify(condition, time=time)
	
	def set_doc_ready_timeout(self, time=100):
		"""
		Run a script that sets a flag time miliseconds after document
		has loaded, giving time for long scripts to fully run before a
		desired testing action is performed.  An implicit wait.
		"""
		id = BaseLocators.DOC_READY_FLAG[1]
		script = '$(document).ready(function() {' + \
			'var f = function(){$(\'<div id="' + id + '"><div>\').' + \
			'appendTo($(\'body\'))};' + \
			'setTimeout(f, ' + str(time) + ');' + \
			'});'
		self.driver.execute_script(script)
	
	def wait_for_doc_ready(self, time=2):
		"""
		Verify presence of doc ready flag.
		"""
		# Using webdriver, wait for doc ready flag
		return self.get_element_if_present(
			BaseLocators.DOC_READY_FLAG,
			time=time
		)
