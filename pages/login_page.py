from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.create_user_api import *


orgs = Create_user.getOrgs()
class LoginPage(BasePage):
    locator_dictionary = {
        "Login": (By.XPATH,"//a[text()='Login']"),
        "email": (By.XPATH, "//input[@name='email']"),
        "password": (By.XPATH, "//input[@name='password']"),
        "signin_button": (By.XPATH, "//button[@type='submit']"),
        "Organization_AfterLogin":(By.XPATH, "//span[text()='Create Organization']"),
        "OrganizationViewReadPermission":(By.XPATH,"//span[text()='Organizations']"),
        "loader":(By.ID,"api-loader")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def login(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Login'])
        del page4
        self.find_element(*self.locator_dictionary['Login']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['email']).clear()
        self.find_element(*self.locator_dictionary['password']).clear()
        self.find_element(*self.locator_dictionary['email']).send_keys(orgs['benemaxadmin_email'])
        self.find_element(*self.locator_dictionary['password']).send_keys("12345678")
        self.find_element(*self.locator_dictionary['signin_button']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_afterlogin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Organization_AfterLogin'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['Organization_AfterLogin'])
        link_2 = link_1.text
        link_3 = "Create Organization"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_org_text_afterlogin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['OrganizationViewReadPermission'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['OrganizationViewReadPermission'])
        link_2 = link_1.text
        link_3 = "Organizations"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def dynamic_login_with_click_loginink(self,email,password):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Login'])
        del page4
        self.find_element(*self.locator_dictionary['Login']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['email']).send_keys(email)
        self.find_element(*self.locator_dictionary['password']).send_keys(password)
        self.find_element(*self.locator_dictionary['signin_button']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def dynamic_login_without_click_loginink(self,email,password):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['email'])
        del page4
        self.find_element(*self.locator_dictionary['email']).clear()
        self.find_element(*self.locator_dictionary['password']).clear()
        self.find_element(*self.locator_dictionary['email']).send_keys(email)
        self.find_element(*self.locator_dictionary['password']).send_keys(password)
        self.find_element(*self.locator_dictionary['signin_button']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait