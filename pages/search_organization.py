from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class SearchOrganization(BasePage):
    locator_dictionary = {
        "search_field": (By.ID,"search"),
        "verify_searched_organization": (By.XPATH, "//table//tr[2]/td[1]"),
        "select_organization": (By.XPATH, "//tabset//select"),
        "loader": (By.ID, "api-loader")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def search(self,org):
        self.find_element(*self.locator_dictionary['search_field']).send_keys(org)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_searched_org(self):
        link_1 = self.find_element(*self.locator_dictionary['verify_searched_organization'])
        link_2 = link_1.text
        link_3 = "Northout Solutions"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def search_with_inactive_filter(self,org):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located(self.locator_dictionary['search_field'])).clear()
        del wait
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_inactive_filter = self.find_element(*self.locator_dictionary['select_organization'])
        select = Select(select_inactive_filter)
        select.select_by_value("0")
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['search_field'])
        del page4
        self.find_element(*self.locator_dictionary['search_field']).send_keys(org)
        time.sleep(1)
        wait = WebDriverWait(self.browser,20)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def search_with_active_filter(self,org):
        wait = WebDriverWait(self.browser, 15)
        a = wait.until(EC.visibility_of_element_located(self.locator_dictionary['search_field']))
        a.clear()
        del wait,a

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_inactive_filter = self.find_element(*self.locator_dictionary['select_organization'])
        select = Select(select_inactive_filter)
        select.select_by_value("1")
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['search_field'])
        del page4
        self.find_element(*self.locator_dictionary['search_field']).send_keys(org)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def search_with_pending_filter(self,org):
        wait = WebDriverWait(self.browser, 15)
        a = wait.until(EC.visibility_of_element_located(self.locator_dictionary['search_field']))
        a.clear()
        del wait, a
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_inactive_filter = self.find_element(*self.locator_dictionary['select_organization'])
        select = Select(select_inactive_filter)
        select.select_by_value("Pending")
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['search_field'])
        del page4
        self.find_element(*self.locator_dictionary['search_field']).send_keys(org)
        time.sleep(1)
        wait = WebDriverWait(self.browser,20)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait