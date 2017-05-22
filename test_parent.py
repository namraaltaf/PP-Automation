from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import unittest
import setting
from selenium import webdriver
from selenium.webdriver.support import ui
from pages import login_selectors



class WebdriverTestCase(unittest.TestCase):
    BROWSER = setting.BROWSER

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def get(self, url=""):
        self.browser.get('{base_url}{page_url}'.format(base_url=setting.BASE_URL, page_url=url))

    def find_element(self, element_selector):
        if element_selector.startswith("xpath"):
            return self.browser.find_element_by_xpath(element_selector[6:])
        else:
            return self.browser.find_element_by_css_selector(element_selector)

    def find_elements(self, element_selector):
        if element_selector.startswith("xpath"):
            return self.browser.find_elements_by_xpath(element_selector[6:])
        else:
            return self.browser.find_elements_by_css_selector(element_selector)

    def is_element_present(self, element_selector):
        self.browser.implicitly_wait(0)
        try:
            self.find_element(element_selector)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.browser.implicitly_wait(setting.DEFAULT_TIMEOUT)

    def get_login_page(self):
        self.get('/login')

    def assert_element_is_displayed_using_css(self, element_css):
        ui.WebDriverWait(self.browser, setting.DEFAULT_TIMEOUT, 1,
                         (StaleElementReferenceException, NoSuchElementException)). \
            until(lambda driver: driver.find_element_by_css_selector(element_css).is_displayed())

    def element_is_displayed_using_xpath(self, element_xpath):
        ui.WebDriverWait(self.browser, setting.DEFAULT_TIMEOUT, 1,
                         (StaleElementReferenceException, NoSuchElementException)). \
            until(lambda driver: self.browser.find_element_by_xpath(element_xpath).is_displayed())

    def assert_that_nextpage_is_displayed(self, page_link):
        browser_current_url = self.browser.current_url
        browser_base_url = setting.BASE_URL + page_link
        self.assertEqual(browser_current_url, browser_base_url)

    def assert_equal_text_using_css(self, selector, expected_text):
        return self.assertEqual(self.browser.find_element_by_css_selector(selector).text, expected_text)

    def assert_equal_text_using_xpath(self, selector, expected_text):
        return self.assertEqual(self.browser.find_element_by_xpath(selector).text, expected_text)

    def login(self,username,password):
        self.get('/login')
        email_id = self.find_element(login_selectors.user_email)
        email_id.clear()
        email_id.send_keys(username)
        pasword = self.find_element(login_selectors.user_password)
        pasword.clear()
        pasword.send_keys(password)
        self.find_element(login_selectors.login_submit).click()