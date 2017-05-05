from selenium.webdriver.common.by import By


class BaseLocators():
    """
    Universally useful locators.
    """
    # external link constants
    LINKEDIN_URL = 'https://www.linkedin.com/in/zachsnyder3'
    GITHUB_URL = 'https://github.com/zachsnyder1'
    # locators
    THUMB = (By.ID, 'nav-brand-thumb')
    LOGO = (By.CLASS_NAME, 'navbar-text')
    HOME_BTN = (By.LINK_TEXT, 'Home')
    PROJECTS_BTN = (By.XPATH, '//li[@id=\'projects-dropdown\']/a[1]')
    PROJECTS_BTNS = (By.XPATH, '//li[@id=\'projects-dropdown\']/ul//a')
    PROJ_HOME_BTN = (By.LINK_TEXT, 'Projects Home')
    BLOG_BTN = (By.LINK_TEXT, 'Blog')
    LINKEDIN_LOGO = (By.ID, 'nav-linkedin-logo')
    GITHUB_LOGO = (By.ID, 'nav-github-logo')
    LOGIN_BTN = (By.LINK_TEXT, 'Login')
    LOGOUT_BTN = (By.LINK_TEXT, 'Logout')
