from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import calendar
from pages.create_user_api import *

orgs = Create_user.getOrgs()
class AccountdetailsPage(BasePage):
    locator_dictionary = {
        "account_details_option": (By.LINK_TEXT,"Account Details"),
        "first_name": (By.NAME,"first_name"),
        "middle_name": (By.NAME,"middle_name"),
        "last_name": (By.NAME,"last_name"),
        "email": (By.NAME, "email"),
        "save_changes_button": (By.XPATH, "//section/form/footer/button[2]"),
        "verify_name_header": (By.XPATH,"//span[@class='user-name dev-capitalize']"),
        "verify_benemax_admin_login":(By.XPATH, "//span[text()='Create Organization']"),
        "verify_modal":(By.XPATH,"//h4[text()='Account Details']"),
        "loader": (By.ID, "api-loader")

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def click_account_details(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['account_details_option'])
        del page4
        self.find_element(*self.locator_dictionary['account_details_option']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def change_account_details_admin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['first_name'])
        del page4
        self.find_element(*self.locator_dictionary['first_name']).clear()
        self.find_element(*self.locator_dictionary['first_name']).send_keys("Nainsi")
        self.find_element(*self.locator_dictionary['middle_name']).clear()
        self.find_element(*self.locator_dictionary['middle_name']).send_keys("N")
        self.find_element(*self.locator_dictionary['last_name']).clear()
        self.find_element(*self.locator_dictionary['last_name']).send_keys("Benemax")
        self.find_element(*self.locator_dictionary['email']).clear()
        self.find_element(*self.locator_dictionary['email']).send_keys(orgs['EditEmployeeEmail1'])
        self.find_element(*self.locator_dictionary['save_changes_button']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def change_account_details_org_admin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['first_name'])
        del page4
        self.find_element(*self.locator_dictionary['first_name']).clear()
        self.find_element(*self.locator_dictionary['first_name']).send_keys("Nainsi")
        self.find_element(*self.locator_dictionary['middle_name']).clear()
        self.find_element(*self.locator_dictionary['middle_name']).send_keys("N")
        self.find_element(*self.locator_dictionary['last_name']).clear()
        self.find_element(*self.locator_dictionary['last_name']).send_keys("Benemax")
        self.find_element(*self.locator_dictionary['email']).clear()
        self.find_element(*self.locator_dictionary['email']).send_keys(orgs['OrgAdminEmail1'])
        self.find_element(*self.locator_dictionary['save_changes_button']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def change_account_details_employee(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['first_name'])
        del page4
        self.find_element(*self.locator_dictionary['first_name']).clear()
        self.find_element(*self.locator_dictionary['first_name']).send_keys("Nainsi")
        self.find_element(*self.locator_dictionary['middle_name']).clear()
        self.find_element(*self.locator_dictionary['middle_name']).send_keys("N")
        self.find_element(*self.locator_dictionary['last_name']).clear()
        self.find_element(*self.locator_dictionary['last_name']).send_keys("Benemax")
        self.find_element(*self.locator_dictionary['email']).clear()
        self.find_element(*self.locator_dictionary['email']).send_keys(orgs['EmployeeEmail1'])
        self.find_element(*self.locator_dictionary['save_changes_button']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_name_header(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_name_header'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_name_header'])
        link_2 = link_1.text
        link_3 = "Nainsi Benemax"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_account_details_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_modal'])
        link_2 = link_1.text
        link_3 = "Account Details"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

