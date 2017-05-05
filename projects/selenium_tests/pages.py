import os
import sys
PACKAGE_ROOT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(),
                                                           os.path.expanduser(__file__))))
PACKAGE_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_ROOT))
sys.path.append(PACKAGE_PATH)
from projects.selenium_tests.locators import ProjectsLocators
from zachsite.selenium_tests.base_page import BasePage


class ProjectsBasePage(BasePage):
    """
    Base page attributes.
    """
    # ---------------------------------------------------------------
    # ------------------- VERIFICATION METHODS ----------------------
    # ---------------------------------------------------------------

    def verify_header_section_visible(self):
        """
        Return header section if present and visible.
        """
        hSect = self.get_element_if_visible(ProjectsLocators.HEADER_SECTION)
        return hSect

    def verify_header_backgnd_visible(self):
        """
        Return header background image if visible.
        """
        hBkg = self.get_element_if_visible(ProjectsLocators.HEADER_BACKGND)
        return hBkg

    def verify_header_title_visible(self):
        """
        Return header title if present and visible.
        """
        hTitle = self.get_element_if_visible(ProjectsLocators.HEADER_TITLE)
        return hTitle

    def verify_subnav_visible(self, time=2):
        """
        Return subnav if visible.
        """
        snav = self.get_element_if_visible(ProjectsLocators.SUBNAV)
        return snav


class ProjectsHomePage(ProjectsBasePage):
    """
    Page objects for the projects home page.
    """
    EXPECTED_PATH = '/projects/'
    # ---------------------------------------------------------------
    # ---------------------- GENERAL ACTION(S) ----------------------
    # ---------------------------------------------------------------

    def get_projects_displayed(self):
        """
        Return list of projects displayed.
        """
        return self.get_elements_if_present(ProjectsLocators.PROJECT_TITLES)


ProjectsHomePage.URL = BasePage.DOMAIN + ProjectsHomePage.EXPECTED_PATH
