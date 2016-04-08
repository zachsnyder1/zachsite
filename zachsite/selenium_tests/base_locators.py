from selenium.webdriver.common.by import By

class BaseLocators():
	"""
	Universally useful locators.
	"""
	DOC_READY_FLAG = (By.ID, "SELENIUM_DOCUMENT_READY")
