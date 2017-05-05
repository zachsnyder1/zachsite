from .locators import LoginLocators, LogoutLocators, HomeLocators
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    """
    Page objects for ZachSite home page.
    """
    EXPECTED_PATH = '/'
    # ---------------------------------------------------------------
    # ---------------------- GENERAL ACTIONS ------------------------
    # ---------------------------------------------------------------

    def get_answer_text(self):
        """
        Get the text currently displayed in the carousel answer div.
        """
        answer = self.get_element_if_visible(HomeLocators.CAR_ANSWER)
        return answer.text

    def wait_for_qa_change(self, time=12):
        """
        Wait for the answer in the QA carousel to change.
        """
        answer = self.get_answer_text()

        def condition(driver): return self.get_answer_text() != answer
        return self.verify(condition, time=time)

    def click_qa_prev(self):
        """
        Click the previous button on the QA carousel
        """
        prev = self.get_element_if_visible(HomeLocators.CAR_PREV)
        prev.click()

    def click_qa_next(self):
        """
        Click the next button on the QA carousel
        """
        next = self.get_element_if_visible(HomeLocators.CAR_NEXT)
        next.click()

    def get_blurbs(self):
        """
        Return list of blurb elements.
        """
        return self.get_elements_if_present(HomeLocators.BLURBS)

    def get_project_titles(self):
        """
        Return list of project title h3 elements.
        """
        return self.get_elements_if_present(HomeLocators.PROJECT_TITLES)


HomePage.URL = BasePage.DOMAIN + HomePage.EXPECTED_PATH


class LoginPage(BasePage):
    """
    Page objects for the login page.
    """
    EXPECTED_PATH = '/accounts/login/'
    # ---------------------------------------------------------------
    # ---------------------- GENERAL ACTIONS ------------------------
    # ---------------------------------------------------------------

    def enter_username(self, username):
        """
        Enters username into input widget.
        """
        usernameIn = self.get_element_if_visible(LoginLocators.USERNAME_IN)
        usernameIn.clear()
        usernameIn.send_keys(username)

    def enter_password(self, password):
        """
        Enters password into the password input widget.
        """
        passIn = self.get_element_if_visible(LoginLocators.PASSWORD_IN)
        passIn.clear()
        passIn.send_keys(password)

    def login(self):
        """
        Clicks the submit button.
        """
        submitBtn = self.get_element_if_visible(LoginLocators.SUBMIT_BTN)
        submitBtn.click()

    def follow_forgot_password_link(self):
        """
        Follow the forgot password link.
        """
        link = self.get_element_if_visible(LoginLocators.FORGOT_PWD)
        link.click()

    def follow_signup_link(self):
        """
        Follow the link to create new account.
        """
        link = self.get_element_if_visible(LoginLocators.SIGN_UP)
        link.click()


LoginPage.URL = BasePage.DOMAIN + LoginPage.EXPECTED_PATH


class LogoutPage(BasePage):
    """
    Page objects for the logout page.
    """
    EXPECTED_PATH = '/accounts/logout/'

    def verify_logged_out(self):
        """
        Look for the success message.
        """
        condition = EC.presence_of_element_located(LogoutLocators.LOGIN_BTN)
        return self.verify(condition)


LogoutPage.URL = BasePage.DOMAIN + LogoutPage.EXPECTED_PATH
