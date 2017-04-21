from pages import login_selectors
from test_parent import WebdriverTestCase

class TestLogin(WebdriverTestCase):
    def setUp(self):
        self.browser.delete_all_cookies()


    def test_login_with_invalid_email(self):
        self.get_login_page()
        email_id = self.find_element(login_selectors.user_email)
        email_id.clear()
        email_id.send_keys("testuser+12ss@payperks.com")
        passwrd = self.find_element((login_selectors.user_password))
        passwrd.clear()
        passwrd.send_keys("1234567a")
        self.find_element(login_selectors.login_submit).click()
        self.assert_element_is_displayed(login_selectors.email_error_div)

    def test_login_with_invalid_password(self):
        self.get_login_page()
        email_id = self.find_element(login_selectors.user_email)
        email_id.clear()
        email_id.send_keys("testuser+12@payperks.com")
        passwrd = self.find_element((login_selectors.user_password))
        passwrd.clear()
        passwrd.send_keys("1234567")
        self.find_element(login_selectors.login_submit).click()
        self.assert_element_is_displayed(login_selectors.password_error_div)

    def test_login_with_valid_credential(self):
        self.get_login_page()
        email_id = self.find_element(login_selectors.user_email)
        email_id.clear()
        email_id.send_keys("testuser+12@payperks.com")
        passwrd = self.find_element((login_selectors.user_password))
        passwrd.clear()
        passwrd.send_keys("1234567a")
        self.find_element(login_selectors.login_submit).click()
        self.assert_element_is_displayed(login_selectors.afater_login_dashboard_div)
        self.assert_that_nextpage_is_displayed('/dashboard')



