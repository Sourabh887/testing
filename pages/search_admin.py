from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from pages.create_user_api import *


class SearchAdminPage(BasePage):
    locator_dictionary = {
        "search_field": (By.XPATH,"(//div[@class='row']/div/input)[2]"),
        "verify_searched_admin": (By.XPATH, "(//table//tr[2]/td[1])[2]"),
        "select_admin": (By.XPATH, "(//tabset//select)[2]"),
        "loader": (By.ID, "api-loader")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def verify_searched_admin(self,admin_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_searched_admin'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_searched_admin'])
        link_2 = link_1.text
        link_3 = admin_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def search_with_inactive_filter(self,first_name1):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located((self.locator_dictionary['search_field']))).clear()
        del wait
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_inactive_filter = self.find_element(*self.locator_dictionary['select_admin'])
        select = Select(select_inactive_filter)
        select.select_by_value("0")
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['search_field'])
        del page4
        self.find_element(*self.locator_dictionary['search_field']).send_keys(first_name1)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def search_with_active_filter(self,first_name1):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located((self.locator_dictionary['search_field']))).clear()
        del wait
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_inactive_filter = self.find_element(*self.locator_dictionary['select_admin'])
        select = Select(select_inactive_filter)
        select.select_by_value("1")
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['search_field'])
        del page4
        self.find_element(*self.locator_dictionary['search_field']).send_keys(first_name1)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def search_with_pending_filter(self,first_name1):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.presence_of_element_located((self.locator_dictionary['search_field']))).clear()
        del wait
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_inactive_filter = self.find_element(*self.locator_dictionary['select_admin'])
        select = Select(select_inactive_filter)
        select.select_by_value("Pending")
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['search_field'])
        del page4
        self.find_element(*self.locator_dictionary['search_field']).send_keys(first_name1)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait