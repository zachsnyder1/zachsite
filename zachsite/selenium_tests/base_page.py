from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

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
