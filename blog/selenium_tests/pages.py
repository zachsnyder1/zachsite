import re
import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from urllib.parse import urlparse
from zachsite.selenium_tests.base_page import BasePage
from blog.selenium_tests.locators import BlogHomeLocators, BlogDetailLocators, \
	BlogBaseLocators
from selenium.webdriver.support import expected_conditions as EC


class BlogBasePage(BasePage):
	"""
	Base blog page.
	"""
	# ---------------------------------------------------------------
	# ------------------- VERIFICATION METHODS ----------------------
	# ---------------------------------------------------------------
	def verify_header_section_visible(self):
		"""
		Return header section if present and visible.
		"""
		hSect = self.get_element_if_visible(BlogBaseLocators.HEADER_SECTION)
		return hSect
	
	def verify_header_backgnd_visible(self):
		"""
		Return header background image if visible.
		"""
		hBkg = self.get_element_if_visible(BlogBaseLocators.HEADER_BACKGND)
		return hBkg
	
	def verify_header_title_contains(self, text):
		"""
		True if header title contains the given text.
		"""
		hTitle = self.get_element_if_visible(BlogBaseLocators.HEADER_TITLE)
		return text in hTitle.text
	
	def verify_blog_img_present(self):
		"""
		Return blog img if present and visible.
		"""
		bImg = self.get_element_if_visible(BlogBaseLocators.BLOG_IMG)
		return bImg
	
	def verify_blog_title_contains(self, text):
		"""
		True if blog title contains the given text.
		"""
		bTitle = self.get_element_if_visible(BlogBaseLocators.BLOG_TITLE)
		return text in bTitle.text
	
	def verify_blog_description_contains(self, text):
		"""
		True if blog description contains the given text.
		"""
		bDesc = self.get_element_if_visible(BlogBaseLocators.BLOG_DESC)
		return text in bDesc.text
	

class BlogHomePage(BlogBasePage):
	"""
	Page objects for the blog home page.
	"""
	EXPECTED_PATH = '/blog/'
	
	# ---------------------------------------------------------------
	# ---------------------- GENERAL ACTION(S) ----------------------
	# ---------------------------------------------------------------
	def get_entries(self):
		"""
		Return list of all entries.
		"""
		entries = self.get_elements_if_present(BlogHomeLocators.ENTRIES)
		return entries
	
	def click_an_entry(self):
		"""
		Click an entry.
		"""
		entries = self.get_entries()
		entries[0].click()

BlogHomePage.URL = BasePage.DOMAIN + BlogHomePage.EXPECTED_PATH


class BlogDetailPage(BlogBasePage):
	"""
	Page objects for the blog detail page.
	"""
	EXPECTED_PATH = r'^/blog/([0-9A-Fa-f-]+)/([0-9A-Za-z_-]+)/$'
	URL = None
	
	# ---------------------------------------------------------------
	# ------------------- OVERRIDE OF VERIFY PATH -------------------
	# ---------------------------------------------------------------
	def verify_path(self, time=2):	
		"""
		True if expected path matches the current path.
		"""
		u = urlparse(self.driver.current_url)
		c = lambda driver: re.fullmatch(self.__class__.EXPECTED_PATH, u.path)
		return self.verify(c, time=time)
	
	# ---------------------------------------------------------------
	# ------------------- VERIFICATION METHODS ----------------------
	# ---------------------------------------------------------------
	def verify_title_present(self):
		"""
		Return title element if present.
		"""
		title = self.get_element_if_visible(BlogDetailLocators.TITLE)
		return title
	
	def verify_tagline_present(self):
		"""
		Return tagline element if present.
		"""
		tagline = self.get_element_if_visible(BlogDetailLocators.TAGLINE)
		return tagline
	
	def verify_body_present(self):
		"""
		Return body element if present.
		"""
		body = self.get_element_if_visible(BlogDetailLocators.BODY)
		return body
	