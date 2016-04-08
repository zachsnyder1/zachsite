from selenium.webdriver.common.by import By

class GeopostLocators():
	"""
	Locators common to all Geopost pages.
	"""
	# Available to both anonymous and auth'ed users
	MAP = (By.ID, 'map')
	ATTRIBUTION = (By.CLASS_NAME, 'ol-attribution')
	ATTR_BTN = (By.XPATH, "//button[@title='Attributions']")
	# Only for auth'ed users
	TOOLBAR = (By.ID, 'toolbar')
	TOOLBAR_TOGGLE = (By.ID, 'toolbar-toggle')
	TOOLBAR_BTNS = (By.CLASS_NAME, 'toolbar-btn')

class HomeLocators(GeopostLocators):
	"""
	Locators for the home page.
	"""
	# Available to both anonymous and auth'ed users
	INFO_MODAL = (By.ID, 'info')
	ENTRY_TITLE = (By.ID, 'title')
	ENTRY_BODY = (By.ID, 'body')
	ENTRY_IMG = (By.ID, 'photo')
	CLOSE_BTN = (By.ID, 'close-btn')
	# Only for auth'ed users
	EDIT_BTN = (By.ID, 'edit-btn')
	DELETE_BTN = (By.ID, 'delete-btn')

class EntryLocators(GeopostLocators):
	"""
	Locators for the entry page.
	"""
	# class names for reference
	ACTIVE = 'btn-danger'
	INACTIVE = 'btn-success'
	# the locators
	DRAW_BTN = (By.ID, 'drawbtn')
	MODIFY_BTN = (By.ID, 'modbtn')
	TITLE_IN = (By.ID, 'title')
	BODY_IN = (By.ID, 'body')
	PHOTO_IN = (By.ID, 'photo')
	DUMMY_SUBMIT = (By.ID, 'dummy-submit')
