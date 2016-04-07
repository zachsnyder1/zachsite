from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
	"""
	Base class for page objects.
	"""
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
	
	def absent(self, locator):
		"""
		Return True if element is absent, else False.
		"""
		try:
			el = self.driver.find_element(*locator)
			return False
		except NoSuchElementException:
			return True