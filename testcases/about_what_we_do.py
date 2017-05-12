
from test_parent import WebdriverTestCase
from pages import what_wo_do_selectors

class TestLogin(WebdriverTestCase):
    def setUp(self):
        self.browser.delete_all_cookies()


    def get_what_we_do_page(self):
        self.get('/about/what-we-do')

    def test_check_welcome_to_payperks_div(self):
        self.get_what_we_do_page()
        self.assert_element_is_displayed(what_wo_do_selectors.welcome_div)
        self.assert_element_is_displayed(what_wo_do_selectors.welcome_pete)
        self.assert_element_is_displayed(what_wo_do_selectors.h2_welcome_to_payperks)
        self.assert_element_is_displayed(what_wo_do_selectors.welcome_description)
        self.assert_equal_text(what_wo_do_selectors.welcome_description, 'The award winning rewards program that lets you earn chances to win $$$ for learning and building good habits!')


    def test_click_signup_now_btn(self):
        self.get_what_we_do_page()
        self.find_element(what_wo_do_selectors.signup_now).click()
        self.assert_element_is_displayed(what_wo_do_selectors.signup_form_after_btn_click)
        self.assert_that_nextpage_is_displayed('/?utm_source=what-we-do&utm_medium=SignUpButton&utm_campaign=AboutUs')

    def test_check_nav_section_list_items_are_displaying(self):
        self.get_what_we_do_page()
        self.assert_element_is_displayed(what_wo_do_selectors.section_nav_block)
        self.find_element(what_wo_do_selectors.what_we_do_1st_list_item)
        self.assert_equal_text(what_wo_do_selectors.what_we_do_1st_list_item, "What We Do")
        self.find_element(what_wo_do_selectors.how_it_work_2nd_list_item)
        self.assert_equal_text(what_wo_do_selectors.how_it_work_2nd_list_item, "How It Works")
        self.find_element(what_wo_do_selectors.in_the_new_3rd_list_item)
        self.assert_equal_text(what_wo_do_selectors.in_the_new_3rd_list_item, "In the News")
        self.find_element(what_wo_do_selectors.saftey_security_4th_list_item)
        self.assert_equal_text(what_wo_do_selectors.saftey_security_4th_list_item, "Safety & Security")
        self.find_element(what_wo_do_selectors.our_psrtner_5th_list_item)
        self.assert_equal_text(what_wo_do_selectors.our_psrtner_5th_list_item, "Our Partners")
        self.find_element(what_wo_do_selectors.our_team_6th_list_item)
        self.assert_equal_text(what_wo_do_selectors.our_team_6th_list_item, "Our Team")
        self.find_element(what_wo_do_selectors.contact_us_7th_list_item)
        self.assert_equal_text(what_wo_do_selectors.contact_us_7th_list_item, "Contact Us")



    def test_what_we_do_section_point1_perks_for_learning(self):
        self.get_what_we_do_page()
        self.assert_element_is_displayed(what_wo_do_selectors.what_we_do_section)
        self.assert_element_is_displayed(what_wo_do_selectors.learn_cap_iamge)
        self.browser.find_element_by_xpath(what_wo_do_selectors.point1_text_h3)
        self.assert_equal_text_using_xpath(what_wo_do_selectors.point1_text_h3, "Perks for Learning")
        self.browser.find_element_by_xpath(what_wo_do_selectors.point1_description)
        self.assert_equal_text_using_xpath(what_wo_do_selectors.point1_description, "PayPerks lets you earn chances to win a cash prize just for learning about important topics such as budgeting, protecting your security online, nutrition and more! Each chance is entered into our monthly sweepstakes for an opportunity to win a cash prize!")

    def test_what_we_do_section_point2_prizes_each_month(self):
        self.get_what_we_do_page()
        self.assert_element_is_displayed(what_wo_do_selectors.what_we_do_section)
        self.assert_element_is_displayed(what_wo_do_selectors.prize_monthly_image)
        self.browser.find_element_by_xpath(what_wo_do_selectors.point2_text_h3)
        self.assert_equal_text_using_xpath(what_wo_do_selectors.point2_text_h3, "Prizes Each Month")
        self.browser.find_element_by_xpath(what_wo_do_selectors.point2_description)
        self.assert_equal_text_using_xpath(what_wo_do_selectors.point1_description, "PayPerks has given away over $178 in prizes in our monthly sweepstakes and will continue to give away more! You could be our next winner!")

    def test_what_we_do_section_point3_Your_Security_Comes_First(self):
        self.get_what_we_do_page()
        self.assert_element_is_displayed(what_wo_do_selectors.what_we_do_section)
        self.assert_element_is_displayed(what_wo_do_selectors.icone_lock_image)
        self.browser.find_element_by_xpath(what_wo_do_selectors.point3_text_h3)
        self.assert_equal_text_using_xpath(what_wo_do_selectors.point3_text_h3, "Your Security Comes First")
        self.element_is_displayed(what_wo_do_selectors.point3_description)

    def test_what_we_do_section_bottom_signup_section(self):
        self.get_what_we_do_page()
        self.assert_element_is_displayed(what_wo_do_selectors.what_we_do_section)
        self.assert_element_is_displayed(what_wo_do_selectors.what_we_do_bottom_signup)
        self.find_element(what_wo_do_selectors.bottom_signp_button).click()
        self.assert_element_is_displayed(what_wo_do_selectors.signup_form_after_btn_click)




