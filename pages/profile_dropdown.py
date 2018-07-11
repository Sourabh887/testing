from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Profile_dropdown_page(BasePage):
    locator_dictionary = {
        "button_dropdown": (By.XPATH, "//button[@class='dropdown-toggle userinfo']"),
        "switch_role": (By.XPATH, "//div[@role='button']"),
        "verify_employee_role": (By.XPATH,"//ul/li/a[text()='Employee']"),
        "verify_orgadmin_role": (By.XPATH, "//ul/li/a[text()='Organization Administrator']"),
        "verify_organization": (By.XPATH,"//p[@class='limit-textoverflow']"),
        "benemax_admin":(By.LINK_TEXT,"Benemax Administrator"),
        "popup": (By.XPATH, "//div[@class='close-button']"),
        "message": (By.ID, "toasty"),
        "loader": (By.ID, "api-loader")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def close_dropdown(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['button_dropdown'])
        del page4
        self.find_element(*self.locator_dictionary['button_dropdown']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def open_switch_role(self):
        try:
            wait = WebDriverWait(self.browser, 15)
            wait.until(EC.visibility_of_element_located((self.locator_dictionary['message'])))
            del wait
            a = self.find_element(*self.locator_dictionary["popup"])
            if a.is_displayed() and a.is_enabled():
                a.click()
        except:
            print("pop up is not visible")
        time.sleep(1)
        try:
            self.find_element(*self.locator_dictionary['button_dropdown']).click()
        except:
            self.find_element(*self.locator_dictionary['button_dropdown']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['switch_role']).click()


    def verify_employee_role(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_employee_role'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_employee_role'])
        link_2 = link_1.text
        link_3 = "Employee"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_orgadmin_role(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_orgadmin_role'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_orgadmin_role'])
        link_2 = link_1.text
        link_3 = "Organization Administrator"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_employee_orgadmin_role(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_orgadmin_role'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_orgadmin_role'])
        link_2 = link_1.text
        link_3 = "Organization Administrator"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_employee_role'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_employee_role'])
        link_2 = link_1.text
        link_3 = "Employee"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_employee_org_admin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_employee_role'])
        del page4
        self.find_element(*self.locator_dictionary['verify_employee_role']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['button_dropdown'])
        del page4
        self.find_element(*self.locator_dictionary['button_dropdown']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['switch_role'])
        del page4
        self.find_element(*self.locator_dictionary['switch_role']).click()
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_orgadmin_role'])
        del page4
        self.find_element(*self.locator_dictionary['verify_orgadmin_role']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_organization_in_header(self,organization_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_organization'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_organization'])
        link_2 = link_1.text
        link_3 = organization_name
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        time.sleep(1)

    def click_employee(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_employee_role'])
        del page4
        self.find_element(*self.locator_dictionary['verify_employee_role']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_orgadmin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_orgadmin_role'])
        del page4
        self.find_element(*self.locator_dictionary['verify_orgadmin_role']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_benemax_admin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['benemax_admin'])
        del page4
        self.find_element(*self.locator_dictionary['benemax_admin']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

