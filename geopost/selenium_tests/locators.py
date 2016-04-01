from selenium.webdriver.common.by import By

class HomeLocators():
	"""
	Locators for the home page.
	"""
	# Available to both anonymous and auth'ed users
	MAP = (By.ID, 'map')
	ATTRIBUTION = (By.CLASS_NAME, 'ol-attribution')
	ATTR_BTN = (By.XPATH, '//div[@class=\'ol-attribution\']/button')
	INFO_MODAL = (By.ID, 'info')
	ENTRY_TITLE = (By.ID, 'title')
	ENTRY_BODY = (By.ID, 'body')
	ENTRY_IMG = (By.ID, 'photo')
	CLOSE_BTN = (By.ID, 'close-btn')
	# Only for auth'ed users
	TOOLBAR = (By.ID, 'toolbar')
	TOOLBAR_TOGGLE = (By.ID, 'toolbar-toggle')
	TOOL_BTNS = (By.CLASS_NAME, 'toolbar-btn')
	TOOL_LINKS = (By.XPATH, '//div[@id=\'toolbar\']/a')
	EDIT_BTN = (By.ID, 'edit-btn')
	DELETE_BTN = (By.ID, 'delete-btn')
	