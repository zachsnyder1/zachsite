import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(),
                                                           os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from zachsite.selenium_tests.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class BlogBaseLocators(BaseLocators):
    """
    Base blog locators.
    """
    HEADER_SECTION = (By.CLASS_NAME, 'header-section')
    HEADER_BACKGND = (By.CLASS_NAME, 'header-background')
    HEADER_TITLE = (By.ID, 'header-title')
    BLOG_IMG = (By.ID, 'blog-image')
    BLOG_TITLE = (By.XPATH, '//div[@id=\'blog-about-div\']//h3')
    BLOG_DESC = (By.XPATH, '//div[@id=\'blog-about-div\']//p')


class BlogHomeLocators(BlogBaseLocators):
    """
    Locators for blog home page.
    """
    ENTRIES = (By.CLASS_NAME, 'entry-about-div')


class BlogDetailLocators(BlogBaseLocators):
    """
    Locators for the blog detail page.
    """
    TITLE = (By.CLASS_NAME, 'entry-title')
    TAGLINE = (By.CLASS_NAME, 'entry-tagline')
    BODY = (By.CLASS_NAME, 'entry-text')
