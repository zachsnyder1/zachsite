from .locators import HomeLocators

class BasePage:
	"""
	Base class for page objects.
	"""
	def __init__(self, driver):
		self.driver = driver

class GeopostHomeAnonymousPage(BasePage):
	"""
	Page objects for Geopost home page as anonymous user.
	"""
	def is_info_displayed(self):
		"""
		Return BOOL indicating whether info modal is displayed.
		"""
		info = self.driver.find_element(*HomeLocators.INFO_MODAL)
		style = info.get_attribute('style')
		return 'display: block' in style
	
	def click_point(self):
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
	
	def get_title(self):
		"""
		Get the title currently displayed. 
		""" 
		elem = self.driver.find_element(*HomeLocators.ENTRY_TITLE)
		return elem.getText()
	
	def get_body(self):
		"""
		Get the text body currently displayed.
		"""
		elem = self.driver.find_element(*HomeLocators.ENTRY_BODY)
		return elem.getText()
	
	def get_img_src(self):
		"""
		Get the src attribute of the entry img element.
		"""
		elem = self.driver.find_element(*HomeLocators.ENTRY_IMG)
		return elem.get_attribute('src')
	
	def is_attribution_displayed(self):
		"""
		Return BOOL indicating whether attribution on map is displayed.
		"""
		attribution = self.driver.find_element(*HomeLocators.ATTRIBUTION)
		classStr = attribution.get_attribute('class')
		return 'ol-collapsed' not in classStr
	
	def toggle_attribution(self):
		"""
		Click the attribution button to open/close it.
		"""
		attrBtn = self.driver.find_element(*HomeLocators.ATTR_BTN)
		attrBtn.click()

class GeopostHomeAuthPage(GeopostHomeAnonymousPage):
	"""
	Additional methods for Geopost home page as auth'ed user.
	"""
	pass