from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class EditAdminPage(BasePage):
    locator_dictionary = {
        "Admin_tab": (By.XPATH, "//ul/li[2]/a/span[2]"),
        "Open_EditAdmin": (By.XPATH,"(//table/tbody/tr[2]/td[6]//div)[1]"),
        "Edit_Admin": (By.XPATH, "//table//tr[2]/td[6]//ul/li[1]/a"),
        "Deactivate_Admin":(By.XPATH, "//table//tr[2]/td[6]//ul/li[2]/a"),
        "deactivate_Admin": (By.XPATH, "//span[text()='Yes, Deactivate']"),
        "verify_admin_tab": (By.XPATH, "//h4[text()='Administrator Details']"),
        "first_name": (By.NAME, "first_name"),
        "last_name": (By.NAME, "last_name"),
        "email": (By.NAME, "email"),
        "select_role":(By.NAME, "user_role"),
        "select_permission": (By.XPATH, "(//section/form//select)[2]"),
        "submit_admin_details": (By.XPATH, "//button[text()='Save Changes']"),
        "verify_edited_admin":(By.XPATH, "//admin-component//table/tbody/tr[2]/td[1]"),
        "verify_edited_admin_inactive": (By.XPATH, "//admin-component//table/tbody/tr[2]/td[5]"),
        "verify_edited_admin_active": (By.XPATH, "//admin-component//table/tbody/tr[2]/td[5]"),
        "search_field": (By.XPATH, "(//div[@class='row']/div/input)[2]"),
        "loader": (By.ID, "api-loader")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )
    def click_admin_tab(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Admin_tab'])
        del page4
        self.find_element(*self.locator_dictionary['Admin_tab']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_edit_administrator(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Admin_tab'])
        del page4
        self.find_element(*self.locator_dictionary['Admin_tab']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['Open_EditAdmin']).click()
        time.sleep(1)
        link_1 = self.find_element(*self.locator_dictionary['Edit_Admin'])
        link_2 = link_1.text
        link_3 = "Edit Administrator"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_edit_administrator(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Admin_tab'])
        del page4
        self.find_element(*self.locator_dictionary['Admin_tab']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['Open_EditAdmin']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['Edit_Admin']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def deactivate_admin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Open_EditAdmin'])
        del page4
        self.find_element(*self.locator_dictionary['Open_EditAdmin']).click()
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Deactivate_Admin'])
        del page4
        self.find_element(*self.locator_dictionary['Deactivate_Admin']).click()
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['deactivate_Admin'])
        del page4
        self.find_element(*self.locator_dictionary['deactivate_Admin']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def edit_admin_owner(self,first_name,last_name,email):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['first_name'])
        del page4
        self.find_element(*self.locator_dictionary['first_name']).clear()
        self.find_element(*self.locator_dictionary['first_name']).send_keys(first_name)
        self.find_element(*self.locator_dictionary['last_name']).clear()
        self.find_element(*self.locator_dictionary['last_name']).send_keys(last_name)
        self.find_element(*self.locator_dictionary['email']).clear()
        self.find_element(*self.locator_dictionary['email']).send_keys(email)
        select_role = self.find_element(*self.locator_dictionary['select_role'])
        select = Select(select_role)
        select.select_by_visible_text("CP")
        select_permission = self.find_element(*self.locator_dictionary['select_permission'])
        select = Select(select_permission)
        select.select_by_value("1")
        del select

        try :
         submit = self.find_element(*self.locator_dictionary['submit_admin_details'])
         submit.click()
         del submit
        except:
         print("element is not clickable at this point")

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait



    def edit_admin_owner_pending(self,first_name,last_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Edit_Admin'])
        del page4
        self.find_element(*self.locator_dictionary['Edit_Admin']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['first_name']).clear()
        self.find_element(*self.locator_dictionary['first_name']).send_keys(first_name)
        self.find_element(*self.locator_dictionary['last_name']).clear()
        self.find_element(*self.locator_dictionary['last_name']).send_keys(last_name)
        try :
         submit = self.find_element(*self.locator_dictionary['submit_admin_details'])
         submit.click()
         del submit
        except:
         print("element is not clickable at this point")

        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_admin_tab(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_admin_tab'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_admin_tab'])
        link_2 = link_1.text
        link_3 = "Administrator Details"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_edited_admin(self,edited_admin_fname):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edited_admin'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edited_admin'])
        link_2 = link_1.text
        print(link_2)
        assert link_2 == edited_admin_fname, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, edited_admin_fname)
        del link_1
        del link_2

    def verify_edited_admin_inactive_state(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edited_admin_inactive'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edited_admin_inactive'])
        link_2 = link_1.text
        print(link_2)
        link_3 = "Inactive"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_edited_admin_active_state(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edited_admin_active'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edited_admin_active'])
        link_2 = link_1.text
        print(link_2)
        link_3 = "Active"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def search_admin(self,search_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['search_field'])
        del page4
        self.find_element(*self.locator_dictionary['search_field']).send_keys(search_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_admin_edit_permission(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_permission'])
        del page4
        select_permission = self.find_element(*self.locator_dictionary['select_permission'])
        select = Select(select_permission)
        select.select_by_value("2")
        del select

        try:
            submit = self.find_element(*self.locator_dictionary['submit_admin_details'])
            submit.click()
            del submit
        except:
            print("element is not clickable at this point")

        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_admin_read_permission(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_permission'])
        del page4
        select_permission = self.find_element(*self.locator_dictionary['select_permission'])
        select = Select(select_permission)
        select.select_by_value("3")
        del select

        try:
            submit = self.find_element(*self.locator_dictionary['submit_admin_details'])
            submit.click()
            del submit
        except:
            print("element is not clickable at this point")

        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait