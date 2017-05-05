from .base_locators import BaseLocators
from selenium.webdriver.common.by import By


class HomeLocators(BaseLocators):
    """
    Locators for the home page.
    """
    CAR_PREV = (By.XPATH, '//div[@id=\'question-carousel\']/a[1]')
    CAR_NEXT = (By.XPATH, '//div[@id=\'question-carousel\']/a[2]')
    CAR_ANSWER = (By.ID, 'answer-text')
    BLURBS = (By.CLASS_NAME, 'blurb')
    PROJECT_TITLES = (By.CLASS_NAME, 'project-title')


class LoginLocators(BaseLocators):
    """
    Locators for the login page.
    """
    USERNAME_IN = (By.NAME, 'username')
    PASSWORD_IN = (By.NAME, 'password')
    SUBMIT_BTN = (By.CLASS_NAME, 'submit-btn')
    FORGOT_PWD = (By.XPATH, '(//p[class=\'auth-link\'])[1]/a')
    SIGN_UP = (By.XPATH, '(//p[class=\'auth-link\'])[2]/a')


class LogoutLocators(BaseLocators):
    """
    Locator for the logout page.
    """
    LOGIN_BTN = (By.PARTIAL_LINK_TEXT, 'Login')
    LOGOUT_MSG = (By.CLASS_NAME, 'auth-msg')
