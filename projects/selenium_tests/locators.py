import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from zachsite.selenium_tests.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class ProjectsLocators(BaseLocators):
	"""
	Locators for projects pages.
	"""
	HEADER_SECTION = (By.CLASS_NAME, 'header-section')
	HEADER_BACKGND = (By.CLASS_NAME, 'header-background')
	HEADER_TITLE = (By.ID, 'header-title')
	SUBNAV = (By.ID, 'project-subnav')