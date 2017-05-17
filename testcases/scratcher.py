from test_parent import WebdriverTestCase
from pages import scratcher_selectors
from pages import login_selectors
from time import sleep
import setting

class TestLogin(WebdriverTestCase):

    def setUp(self):
        self.browser.delete_all_cookies()

    def test_scratcher_page_form_headings_images(self):
        self.login(setting.USER,setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.assert_element_is_displayed(scratcher_selectors.scrtcher_fan_iamge)
        self.assert_element_is_displayed(scratcher_selectors.scrtcher_form_title)
        self.assert_equal_text(scratcher_selectors.scrtcher_form_title, "Claim your Scratcher Points")
        self.assert_element_is_displayed(scratcher_selectors.scrtcher_form_desc_text)
        self.assert_equal_text(scratcher_selectors.scrtcher_form_desc_text, "To claim your Scratcher Points, simply enter your Scratcher Code below.")

    # def test_tooltip_icon_displyed(self):
    #     self.login(setting.USER, setting.PASSWORD)
    #     self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
    #     self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
    #     self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
    #     sleep(2)
    #     self.assert_element_is_displayed(".trigger-tooltip .icon-tooltip")
    #     self.find_element(".trigger-tooltip .icon-tooltip").click()
    #     sleep(5)
    #     self.assert_element_is_displayed(scratcher_selectors.tooltip_description)

    def test_scratcher_code_with_empty_value(self):
        self.login(setting.USER, setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.find_element(scratcher_selectors.scratcher_code).clear()
        self.find_element(scratcher_selectors.scrtcher_submit).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_inline_error)
        self.assert_equal_text(scratcher_selectors.scratcher_inline_error, "Please enter a scratcher code")


    def test_scratcher_code_with_invalid_value(self):
        self.login(setting.USER, setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.find_element(scratcher_selectors.scratcher_code).send_keys("testcodetesting")
        self.find_element(scratcher_selectors.scrtcher_submit).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_inline_error)
        self.assert_equal_text(scratcher_selectors.scratcher_inline_error, "It looks like this scratcher code is not valid. Please check it and try again.")
    #
    def test_inactive_scratcher_code(self):
        self.login(setting.USER, setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.find_element(scratcher_selectors.scratcher_code).send_keys("KHYNYFNR")
        self.find_element(scratcher_selectors.scrtcher_submit).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_inline_error)
        self.assert_equal_text(scratcher_selectors.scratcher_inline_error, "It looks like this scratcher code is not valid. Please check it and try again.")


    def test_scratcher_code_consumed_by_other_user(self):
        self.login(setting.USER, setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.find_element(scratcher_selectors.scratcher_code).send_keys("TTBLGVVL")
        self.find_element(scratcher_selectors.scrtcher_submit).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_inline_error)
        self.assert_equal_text(scratcher_selectors.scratcher_inline_error, "Sorry, this code has already been used.")

    def test_scratcher_code_consumed_by_same_user(self):
        self.login(setting.user_emailaddress_with_claimed_scratcher, setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.find_element(scratcher_selectors.scratcher_code).send_keys("TTBLGVVL")
        self.find_element(scratcher_selectors.scrtcher_submit).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_inline_error)
        self.find_element(scratcher_selectors.already_redeemed_scratcher_link).click()
        self.assert_element_is_displayed(scratcher_selectors.activity_scratcher_claim_filter)
        self.assert_that_nextpage_is_displayed("/activity/scratcher-claim")

    def test_redeem_valid_scratcher_code_for_nocard_user(self):
        self.login(setting.nocard_user_emailaddress, setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.find_element(scratcher_selectors.scratcher_code).send_keys("dddddddd")
        self.find_element(scratcher_selectors.scrtcher_submit).click()
        self.assert_element_is_displayed(scratcher_selectors.you_have_claimed_your_scratcher_page)
        self.assert_that_nextpage_is_displayed("/programs/direct-express/link?scratcher-claim-points=10")

    def test_redeem_valid_scratcher_code_for_suspected_user(self):
        self.login(setting.suspeced_user_emailaddress, setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.find_element(scratcher_selectors.scratcher_code).send_keys("ddddddde")
        self.find_element(scratcher_selectors.scrtcher_submit).click()
        self.assert_element_is_displayed(scratcher_selectors.you_have_claimed_your_scratcher_page)
        self.assert_that_nextpage_is_displayed("/programs/direct-express/link?scratcher-claim-points=10")

    def test_redeem_valid_scratcher_code_for_linked_user(self):
        self.login(setting.linked_user_emailaddress, setting.PASSWORD)
        self.assert_element_is_displayed(scratcher_selectors.claim_a_scratcher_nav_button)
        self.find_element(scratcher_selectors.claim_a_scratcher_nav_button).click()
        self.assert_element_is_displayed(scratcher_selectors.scratcher_page)
        self.find_element(scratcher_selectors.scratcher_code).send_keys("DDDDDDDA")
        self.find_element(scratcher_selectors.scrtcher_submit).click()
        self.assert_element_is_displayed(scratcher_selectors.whats_next_page)
        self.assert_that_nextpage_is_displayed("/claim-scratcher-success?type=scratcher&id=1")


