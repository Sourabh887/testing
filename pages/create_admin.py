from selenium.webdriver.common.by import By
from pages.base_page_object import BasePage
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CreateAdminPage(BasePage):
    locator_dictionary = {
        "Admin_tab": (By.XPATH, "//ul/li[2]/a/span[2]"),
        "create_administrator": (By.XPATH, "//span[text()='Create Administrator']"),
        "verify_admin_modal": (By.XPATH,"//h4[text()='Create an Administrator']"),
        "first_name": (By.NAME, "first_name"),
        "last_name": (By.NAME, "last_name"),
        "email": (By.NAME, "email"),
        "select_role":(By.NAME, "user_role"),
        "select_permission": (By.NAME, "permission"),
        "submit_admin_details": (By.XPATH, "//footer//button[@type='submit']"),
        "verify_created_admin":(By.XPATH, "//admin-component//table/tbody/tr[2]/td[1]"),
        "verify_created_admin_inactive": (By.XPATH, "//admin-component//table/tbody/tr[2]/td[5]"),
        "loader": (By.ID, "api-loader")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def click_create_administrator(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Admin_tab'])
        del page4
        self.find_element(*self.locator_dictionary['Admin_tab']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['create_administrator']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_admin_owner(self,first_name,last_name,email):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['first_name'])
        del page4
        self.find_element(*self.locator_dictionary['first_name']).send_keys(first_name)
        self.find_element(*self.locator_dictionary['last_name']).send_keys(last_name)
        self.find_element(*self.locator_dictionary['email']).send_keys(email)
        select_role = self.find_element(*self.locator_dictionary['select_role'])
        select = Select(select_role)
        select.select_by_value("1")
        select_permission = self.find_element(*self.locator_dictionary['select_permission'])
        select = Select(select_permission)
        select.select_by_value("1")
        del select
        self.find_element(*self.locator_dictionary['submit_admin_details']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_admin_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_admin_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_admin_modal'])
        link_2 = link_1.text
        link_3 = "Create an Administrator"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_created_admin(self,created_admin_fname):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_admin'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_admin'])
        link_2 = link_1.text
        print(link_2)
        assert link_2 == created_admin_fname, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, created_admin_fname)
        del link_1
        del link_2

    def verify_created_admin_inactive_state(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_admin_inactive'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_admin_inactive'])
        link_2 = link_1.text
        print(link_2)
        link_3 = "Inactive"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_created_admin_active_state(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_admin_inactive'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_admin_inactive'])
        link_2 = link_1.text
        print(link_2)
        link_3 = "Active"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_admin_view_not_displayed(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_administrator'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['create_administrator'])
        link_2 = link_1.text
        print(link_2)
        link_3 = "Create Administrator"
        assert link_2 != link_3, "Admin tab visible to admin with edit permission" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_created_admin_pending_state(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_admin_inactive'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_admin_inactive'])
        link_2 = link_1.text
        print(link_2)
        link_3 = "Pending"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3