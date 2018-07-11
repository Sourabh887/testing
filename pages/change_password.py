from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import calendar
from pages.create_user_api import *

orgs = Create_user.getOrgs()
class Change_Password_Page(BasePage):
    locator_dictionary = {
        "change_password": (By.LINK_TEXT,"Change Password"),
        "current_password": (By.ID,"password"),
        "new_password": (By.ID,"new_password"),
        "confirm_new_password": (By.ID,"confirm_new_password"),
        "change_password_btn": (By.XPATH, "//section/form/footer/button[2]"),
        "loader": (By.ID, "api-loader")

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def click_change_password(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['change_password'])
        del page4
        self.find_element(*self.locator_dictionary['change_password']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def change_password_admin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['current_password'])
        del page4
        self.find_element(*self.locator_dictionary['current_password']).clear()
        self.find_element(*self.locator_dictionary['current_password']).send_keys("12345678")
        self.find_element(*self.locator_dictionary['new_password']).clear()
        self.find_element(*self.locator_dictionary['new_password']).send_keys("123456789")
        self.find_element(*self.locator_dictionary['confirm_new_password']).clear()
        self.find_element(*self.locator_dictionary['confirm_new_password']).send_keys("123456789")
        self.find_element(*self.locator_dictionary['change_password_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait



