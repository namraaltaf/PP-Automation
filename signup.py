from pages import signup_selectors
from test_parent import WebdriverTestCase
from time import sleep
import setting
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin(WebdriverTestCase):
    def setUp(self):
        self.browser.delete_all_cookies()


    def get_home_page(self):
        self.get("")

    def test_view_signup_form(self):
        self.get_home_page()
        self.assert_element_is_displayed(signup_selectors.signup_form)


    def test_signup_with_empty_values(self):
        self.get_home_page()
        self.find_element(signup_selectors.first_name).clear()
        self.find_element(signup_selectors.email_address).clear()
        self.find_element(signup_selectors.password).clear()
        self.find_element(signup_selectors.confirm_password).clear()

        self.find_element(signup_selectors.create_account_btn).click()
        self.assert_element_is_displayed(signup_selectors.first_name_error)
        self.assert_equal_text(signup_selectors.first_name_error, 'Please provide a valid First Name')
        self.assert_element_is_displayed(signup_selectors.email_error)
        self.assert_equal_text(signup_selectors.email_error, 'Please provide a valid email address')
        self.assert_element_is_displayed(signup_selectors.password_error)
        self.assert_equal_text(signup_selectors.password_error, 'Please provide your password')
        self.assert_element_is_displayed(signup_selectors.confirm_password_error)
        self.assert_equal_text(signup_selectors.confirm_password_error, 'Please provide your password')

    def test_signup_with_invalid_name(self):
        self.get_home_page()
        first_name = self.find_element(signup_selectors.first_name)
        first_name.clear()
        first_name.send_keys("sobia%$")
        email = self.find_element(signup_selectors.email_address)
        email.clear()
        email.send_keys("sobia@test.com")
        passwordd = self.find_element(signup_selectors.password)
        passwordd.clear()
        passwordd.send_keys("1234567a")
        cofirm_passwordd = self.find_element(signup_selectors.confirm_password)
        cofirm_passwordd.clear()
        cofirm_passwordd.send_keys("1234567a")
        self.find_element(signup_selectors.create_account_btn).click()
        self.assert_element_is_displayed(signup_selectors.first_name_error)
        self.assert_equal_text(signup_selectors.first_name_error, 'Name can only include letters, spaces, periods, dashes, commas and apostrophes.')


    def test_signup_with_invalid_email(self):
        self.get_home_page()
        first_name = self.find_element(signup_selectors.first_name)
        first_name.clear()
        first_name.send_keys("sobia")
        email = self.find_element(signup_selectors.email_address)
        email.clear()
        email.send_keys("sobia@test.comm")
        passwordd = self.find_element(signup_selectors.password)
        passwordd.clear()
        passwordd.send_keys("1234567a")
        cofirm_passwordd = self.find_element(signup_selectors.confirm_password)
        cofirm_passwordd.clear()
        cofirm_passwordd.send_keys("1234567a")
        self.find_element(signup_selectors.create_account_btn).click()
        self.assert_element_is_displayed(signup_selectors.email_error)
        self.assert_equal_text(signup_selectors.email_error, 'Oops! Looks like you might have mis-typed your email address. Please check the domain name (the part after the @) and try again.')


    def test_signup_with_invalid_password_length(self):
        self.get_home_page()
        first_name = self.find_element(signup_selectors.first_name)
        first_name.clear()
        first_name.send_keys("sobia")
        email = self.find_element(signup_selectors.email_address)
        email.clear()
        email.send_keys("sobia@test.com")
        passwordd = self.find_element(signup_selectors.password)
        passwordd.clear()
        passwordd.send_keys("1234567")
        cofirm_passwordd = self.find_element(signup_selectors.confirm_password)
        cofirm_passwordd.clear()
        cofirm_passwordd.send_keys("1234567a")
        self.find_element(signup_selectors.create_account_btn).click()
        self.assert_element_is_displayed(signup_selectors.password_error)
        self.assert_equal_text(signup_selectors.password_error, 'Your new password must be at least 8 characters and contain at least one number and letter.')

    def test_signup_with_invalid_confirm_password(self):
        self.get_home_page()
        first_name = self.find_element(signup_selectors.first_name)
        first_name.clear()
        first_name.send_keys("sobia")
        email = self.find_element(signup_selectors.email_address)
        email.clear()
        email.send_keys("sobia@test.com")
        passwordd = self.find_element(signup_selectors.password)
        passwordd.clear()
        passwordd.send_keys("1234567a")
        cofirm_passwordd = self.find_element(signup_selectors.confirm_password)
        cofirm_passwordd.clear()
        cofirm_passwordd.send_keys("1234567b")
        self.find_element(signup_selectors.create_account_btn).click()
        self.assert_element_is_displayed(signup_selectors.confirm_password_error)
        self.assert_equal_text(signup_selectors.confirm_password_error, 'The new passwords you entered do not match.')


    def test_signup_check_tooltip(self):
        self.get_home_page()
        self.find_element(signup_selectors.tooltip_icon).click()
        self.assert_element_is_displayed(signup_selectors.tooltip_password_div)
        self.assert_equal_text(signup_selectors.tooltip_password_div, 'Passwords must be at least eight characters long and contain both letters and a number.')


    def test_signup_with_valid_values(self):
        self.get_home_page()
        self.find_element(signup_selectors.first_name).send_keys("sobia")
        self.find_element(signup_selectors.email_address).send_keys("testuser1@test.com")
        self.find_element(signup_selectors.password).send_keys("1234567a")
        self.find_element(signup_selectors.confirm_password).send_keys("1234567a")
        self.find_element(signup_selectors.create_account_btn).click()
        self.assert_element_is_displayed(signup_selectors.signup_scratcher_form)
        self.assert_that_nextpage_is_displayed('/signup/scratcher')



