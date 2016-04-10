import unittest
from selenium import webdriver
import os
import sys
PACKAGE_ROOT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), 
	os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from zachsite.selenium_tests.pages import HomePage, LoginPage, LogoutPage
from blog.selenium_tests.pages import BlogHomePage
from projects.selenium_tests.pages import ProjectsHomePage

class BaseTests():
	"""
	Methods to test the navbar, present in all other pages.
	"""
	def test_nav_thumb_link(self):
		"""
		Click the thumb link and make sure it leads to home page.
		"""
		self.page.click_nav_thumb()
		self.page = HomePage(self.driver)
		self.assertTrue(self.page.verify_path())
	
	def test_nav_home_link(self):
		"""
		Click the home link and make sure it leads to home page.
		"""
		self.page.click_home_link()
		self.page = HomePage(self.driver)
		self.assertTrue(self.page.verify_path())
	
	def test_nav_projects_home_link(self):
		"""
		Toggle projects dropdown, then click proj home link.
		"""
		self.page.toggle_projects_dropdown()
		self.page.click_proj_home_link()
		self.page = ProjectsHomePage(self.driver)
		self.assertTrue(self.page.verify_path())
	
	def test_nav_blog_link(self):
		"""
		Click the blog link and make sure it leads to blog page.
		"""
		self.page.click_blog_link()
		self.page = BlogHomePage(self.driver)
		self.assertTrue(self.page.verify_path())
	
	def test_nav_linkedin_link(self):
		"""
		Click the linkedin link, verify it leads to linkedin page.
		"""
		self.page.click_linkedin_logo()
		self.assertTrue(self.page.verify_linkedin_url())
	
	def test_nav_github_link(self):
		"""
		Click the github link, verify it leads to github page.
		"""
		self.page.click_github_logo()
		self.assertTrue(self.page.verify_github_url())
