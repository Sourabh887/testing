from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Active_Deactive_Org(BasePage):
    locator_dictionary = {
        "Open_EditOrganization": (By.CLASS_NAME, "ellipse"),
        "activate_Organization": (By.XPATH, "//table//tr[2]/td[8]//ul/li[2]/a"),
        "Activate_Organization": (By.XPATH,"//span[text()='Yes, Activate']"),
        "verify_activate_org_tab": (By.XPATH,"//span[text()='Yes, Activate']"),
        "Org_filter": (By.XPATH, "//select"),
        "verify_activate_organization":(By.XPATH, "//table//tr[2]/td[1]"),
        "Deactivate_Organization": (By.XPATH, "//span[text()='Yes, Deactivate']"),
        "verify_deactivate_org_tab": (By.XPATH, "//span[text()='Yes, Deactivate']"),
        "verify_deactivate_organization": (By.XPATH, "//table//tr[2]/td[1]"),
        "loader": (By.ID, "api-loader")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def click_active_organization(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Open_EditOrganization'])
        del page4
        self.find_element(*self.locator_dictionary['Open_EditOrganization']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['activate_Organization']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_active_org_Modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_activate_org_tab'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_activate_org_tab'])
        link_2 = link_1.text
        link_3 = "Yes, Activate"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3



    def click_yes_activate(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Activate_Organization'])
        del page4
        self.find_element(*self.locator_dictionary['Activate_Organization']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait



    def verify_activated_organization(self,link_3 ):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_activate_organization'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_activate_organization'])
        link_2 = link_1.text
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_deactive_org_Modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_deactivate_org_tab'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_deactivate_org_tab'])
        link_2 = link_1.text
        link_3 = "Yes, Deactivate"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                     " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_yes_deactivate(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Deactivate_Organization'])
        del page4
        self.find_element(*self.locator_dictionary['Deactivate_Organization']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_deactivated_organization(self, link_3):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_deactivate_organization'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_deactivate_organization'])
        link_2 = link_1.text
        assert link_2 == link_3, "Visible Text is not as expected" \
                                     " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3