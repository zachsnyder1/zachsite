from .locators import LoginLocators, LogoutLocators
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
	"""
	Page objects for the login page.
	"""
	EXPECTED_PATH = '/accounts/login/'
	URL = 'http://127.0.0.1:8000/accounts/login/'
	# ---------------------------------------------------------------
	# ---------------------- GENERAL ACTIONS ------------------------
	# ---------------------------------------------------------------
	def enter_username(self, username):
		"""
		Enters username into input widget.
		"""
		usernameIn = self.get_element_if_visible(LoginLocators.USERNAME_IN)
		usernameIn.clear()
		usernameIn.send_keys(username)
	
	def enter_password(self, password):
		"""
		Enters password into the password input widget.
		"""
		passIn = self.get_element_if_visible(LoginLocators.PASSWORD_IN)
		passIn.clear()
		passIn.send_keys(password)
	
	def login(self):
		"""
		Clicks the submit button.
		"""
		submitBtn = self.get_element_if_visible(LoginLocators.SUBMIT_BTN)
		submitBtn.click()
	
	def follow_forgot_password_link(self):
		"""
		Follow the forgot password link.
		"""
		link = self.get_element_if_visible(LoginLocators.FORGOT_PWD)
		link.click()
	
	def follow_signup_link(self):
		"""
		Follow the link to create new account.
		"""
		link = self.get_element_if_visible(LoginLocators.SIGN_UP)
		link.click()


class LogoutPage(BasePage):
	"""
	Page objects for the logout page.
	"""
	EXPECTED_PATH = '/accounts/logout/'
	URL = 'http://127.0.0.1:8000/accounts/logout/'
	def verify_logged_out(self):
		"""
		Look for the success message.
		"""
		condition = EC.presence_of_element_located(LogoutLocators.LOGIN_BTN)
		return self.verify(condition)
