from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
from .base_locators import BaseLocators


class BasePage:
    """
    Base class for page objects.
    """
    DOMAIN = 'https://zach-site.com'
    EXPECTED_PATH = None
    URL = None

    # ---------------------------------------------------------------
    # --------------- INHERITED HELPER METHODS ----------------------
    # ---------------------------------------------------------------
    def __init__(self, driver):
        self.driver = driver

    def verify(self, condition, time=2):
        """
        Return True if condition is verified within time.
        """
        try:
            WebDriverWait(self.driver, time).until(condition)
            return True
        except TimeoutException:
            return False

    def get_element_if_present(self, locator, time=2):
        """
        Wait for element to be present in DOM, return element, or
        None if it never shows up.
        """
        p = self.verify(EC.presence_of_element_located(locator), time=time)
        if p:
            return self.driver.find_element(*locator)
        else:
            return None

    def get_elements_if_present(self, locator, time=2):
        """
        Wait for elements to be present in DOM, return list of elements,
        or None if they never show up.
        """
        def c(driver): return EC.presence_of_all_elements_located(locator)
        if self.verify(c, time=time):
            return self.driver.find_elements(*locator)
        else:
            return None

    def get_element_if_visible(self, locator, timeP=2, timeV=2):
        """
        Wait for presence in DOM, get element, wait for it to be visible,
        return element, or None if it is either not present or not visible.
        """
        element = self.get_element_if_present(locator, time=timeP)
        if element:
            v = self.verify(EC.visibility_of(element), time=timeV)
            if v:
                return element
            else:
                pass
        else:
            pass
        # If either condition is false, return None
        return None

    def absent(self, locator):
        """
        Return True if element is absent, else False.
        """
        try:
            el = self.driver.find_element(*locator)
            return False
        except NoSuchElementException:
            return True

    def verify_path(self, time=2):
        """
        True if expected path matches the current path.
        """
        u = urlparse(self.driver.current_url)

        def condition(driver): return self.__class__.EXPECTED_PATH == u.path
        return self.verify(condition, time=time)

    def verify_url(self, expected):
        """
        True if current url matches expected url.
        """
        return self.verify(lambda driver: self.driver.current_url == expected)

    # ---------------------------------------------------------------
    # ------------------ NAVBAR: GENERAL ACTIONS --------------------
    # ---------------------------------------------------------------
    def click_nav_thumb(self):
        """
        Click on the thumb icon on the navbar.
        """
        thumb = self.get_element_if_visible(BaseLocators.THUMB)
        thumb.click()

    def click_home_link(self):
        """
        Follow the home link.
        """
        home = self.get_element_if_visible(BaseLocators.HOME_BTN)
        home.click()

    def toggle_projects_dropdown(self):
        """
        Toggle the projects dropdown.
        """
        projs = self.get_element_if_visible(BaseLocators.PROJECTS_BTN)
        projs.click()

    def click_proj_home_link(self):
        """
        Follow link to projects home.
        """
        projHome = self.get_element_if_visible(BaseLocators.PROJ_HOME_BTN)
        projHome.click()

    def click_blog_link(self):
        """
        Follow the blog link.
        """
        blog = self.get_element_if_visible(BaseLocators.BLOG_BTN)
        blog.click()

    def click_linkedin_logo(self):
        """
        Follow link to linkedin page.
        """
        li = self.get_element_if_visible(BaseLocators.LINKEDIN_LOGO)
        li.click()

    def click_github_logo(self):
        """
        Follow link to github page.
        """
        gh = self.get_element_if_visible(BaseLocators.GITHUB_LOGO)
        gh.click()

    def click_login(self):
        """
        Follow link to login.
        """
        login = self.get_element_if_visible(BaseLocators.LOGIN_BTN)
        login.click()

    def click_logout(self):
        """
        Follow link to logout.
        """
        logout = self.get_element_if_visible(BaseLocators.LOGOUT_BTN)
        logout.click()

    def get_projs_from_dropdown(self):
        """
        Return list of project link elements from the projects dropdown.
        """
        return self.get_elements_if_present(BaseLocators.PROJECTS_BTNS)

    # ---------------------------------------------------------------
    # ------------------- VERIFICATION METHODS ----------------------
    # ---------------------------------------------------------------
    def verify_linkedin_url(self):
        """
        Verify current url matches expected for linkedin page.
        """
        return self.verify_url(BaseLocators.LINKEDIN_URL)

    def verify_github_url(self):
        """
        Verify current url matches expected for github page.
        """
        return self.verify_url(BaseLocators.GITHUB_URL)
