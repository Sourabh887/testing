from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class Group_class_divisionPage(BasePage):
    locator_dictionary = {
        "first_org":(By.XPATH, "//table/tbody/tr[2]/td[1]/a"),
        "group" : (By.XPATH, "//*[text()='Groups']"),
        "divisions" : (By.XPATH,"//*[text()='Divisions']"),
        "classes" : (By.XPATH,"//*[text()='Classes']"),

        "create_group" : (By.XPATH,"//*[text()='Create Group']"),
        "verify_create_group_modal": (By.XPATH, "//*[text()='Create a Group']"),
        "verify_edit_group_modal": (By.XPATH, "//*[text()='Update a Group']"),
        "create_group_name":(By.NAME,"group_name"),
        "direct_id_group":(By.NAME,"one_direct_id"),
        "direct_id_group_edit":(By.NAME,"direct_id"),
        "create_group_btn":(By.XPATH,"//button[@type='submit']"),
        "verify_created_group":(By.XPATH,"(//table//tr[2]/td[1])[2]"),
        "edit_group_ellipses":(By.XPATH,"(//div[@class='btn-more-options-cover'])[1]"),
        "org_admin_edit_group_ellipses":(By.XPATH,"(//div[@class='btn-more-options-cover'])[3]"),
        "edit_group":(By.XPATH,"(//table//ul/li/a)[1]"),
        "edit_group_name": (By.NAME, "name"),

        "create_division": (By.XPATH, "//*[text()='Create Division']"),
        "verify_create_division_modal": (By.XPATH, "//*[text()='Create a Division']"),
        "verify_edit_division_modal": (By.XPATH, "//*[text()='Update a Division']"),
        "division_name": (By.NAME, "division_name"),
        "select_group":(By.NAME, "selected_group"),
        "direct_id_division": (By.NAME, "one_direct_id"),
        "create_division_btn": (By.XPATH, "//button[@type='submit']"),
        "verify_created_division": (By.XPATH, "(//table/tbody/tr[2]/td[2])[2]"),
        "edit_division_ellipses": (By.XPATH, "(//div[@class='btn-more-options-cover'])[2]"),
        "org_admin_edit_division_ellipses":(By.XPATH,"(//div[@class='btn-more-options-cover'])[5]"),
        "edit_division": (By.LINK_TEXT, "Edit Division"),

        "create_class": (By.XPATH, "//*[text()='Create Class']"),
        "verify_create_class_modal": (By.XPATH, "//*[text()='Create a Class']"),
        "verify_edit_class_modal": (By.XPATH, "//*[text()='Update a Class']"),
        "class_name": (By.NAME, "class_name"),
        "direct_id_class": (By.NAME, "direct_id"),
        "create_class_btn": (By.XPATH, "//button[@type='submit']"),
        "verify_created_class": (By.XPATH, "(//table/tbody/tr[2]/td[1])[4]"),
        "edit_class_ellipses": (By.XPATH, "(//div[@class='btn-more-options-cover'])[3]"),
        "org_admin_edit_class_ellipses": (By.XPATH, "(//div[@class='btn-more-options-cover'])[7]"),
        "edit_class": (By.LINK_TEXT, "Edit Class"),
        "close_modal": (By.XPATH, "(//a[@class='close-modal'])[2]"),

        "mouse_hover_element":(By.XPATH,"//navigation/nav//figure"),
        "People":(By.LINK_TEXT,"People"),
        "loader": (By.ID, "api-loader")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def click_org(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['first_org'])
        del page4
        self.find_element(*self.locator_dictionary['first_org']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_close_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['close_modal'])
        del page4
        self.find_element(*self.locator_dictionary['close_modal']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_group(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['group'])))
        del wait
        self.find_element(*self.locator_dictionary['group']).click()
        time.sleep(1)

    def click_create_group(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['create_group'])))
        del wait
        self.find_element(*self.locator_dictionary['create_group']).click()
        time.sleep(1)

    def create_group(self,group_name,direct_id):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_group_name'])
        del page4
        self.find_element(*self.locator_dictionary['create_group_name']).send_keys(group_name)
        self.find_element(*self.locator_dictionary['direct_id_group']).send_keys(direct_id)
        self.find_element(*self.locator_dictionary['create_group_btn']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_create_group_btn(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_group'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['create_group'])
        link_2 = link_1.text
        link_3 = "Create Group"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_create_group_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_create_group_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_create_group_modal'])
        link_2 = link_1.text
        link_3 = "Create a Group"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_created_group(self,created_group):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_group'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_group'])
        link_2 = link_1.text
        link_3 = created_group
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_edit_group_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edit_group_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edit_group_modal'])
        link_2 = link_1.text
        link_3 = "Update a Group"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_edit_group(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_group_ellipses'])
        del page4
        time.sleep(1)
        self.find_element(*self.locator_dictionary['edit_group_ellipses']).click()
        time.sleep(1)

    def org_admin_click_edit_group(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['org_admin_edit_group_ellipses'])
        del page4
        time.sleep(1)
        self.find_element(*self.locator_dictionary['org_admin_edit_group_ellipses']).click()
        time.sleep(1)


    def click_edit_group_btn(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_group'])
        del page4
        self.find_element(*self.locator_dictionary['edit_group']).click()
        time.sleep(1)

    def edit_group(self,group_name,direct_id):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_group_name'])
        del page4
        self.find_element(*self.locator_dictionary['edit_group_name']).clear()
        self.find_element(*self.locator_dictionary['direct_id_group_edit']).clear()
        self.find_element(*self.locator_dictionary['edit_group_name']).send_keys(group_name)
        self.find_element(*self.locator_dictionary['direct_id_group_edit']).send_keys(direct_id)
        self.find_element(*self.locator_dictionary['create_group_btn']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_edited_group(self,edited_group):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_group'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_group'])
        link_2 = link_1.text
        link_3 = edited_group
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_division(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['divisions'])))
        del wait
        self.find_element(*self.locator_dictionary['divisions']).click()
        time.sleep(1)

    def click_create_division(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['create_division'])))
        del wait
        self.find_element(*self.locator_dictionary['create_division']).click()
        time.sleep(1)

    def create_division(self, division_name, direct_id,group_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['division_name'])
        del page4
        self.find_element(*self.locator_dictionary['division_name']).send_keys(division_name)
        select_group1 = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group1)
        select.select_by_visible_text(group_name)
        self.find_element(*self.locator_dictionary['direct_id_division']).send_keys(direct_id)
        time.sleep(1)
        self.find_element(*self.locator_dictionary['create_division_btn']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_create_division_btn(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_division'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['create_division'])
        link_2 = link_1.text
        link_3 = "Create Division"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_create_division_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_create_division_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_create_division_modal'])
        link_2 = link_1.text
        link_3 = "Create a Division"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_created_division(self, created_division):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_division'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_division'])
        link_2 = link_1.text
        print(link_2)
        link_3 = created_division
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_edit_division_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edit_division_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edit_division_modal'])
        link_2 = link_1.text
        link_3 = "Update a Division"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_edit_division(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_division_ellipses'])
        del page4
        time.sleep(1)
        self.find_element(*self.locator_dictionary['edit_division_ellipses']).click()
        time.sleep(1)

    def org_admin_click_edit_division(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['org_admin_edit_division_ellipses'])
        del page4
        time.sleep(1)
        self.find_element(*self.locator_dictionary['org_admin_edit_division_ellipses']).click()
        time.sleep(1)

    def click_edit_division_btn(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_division'])
        del page4
        self.find_element(*self.locator_dictionary['edit_division']).click()
        time.sleep(1)

    def edit_division(self, division_name, direct_id):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['division_name'])
        del page4
        self.find_element(*self.locator_dictionary['division_name']).clear()
        self.find_element(*self.locator_dictionary['direct_id_division']).clear()
        self.find_element(*self.locator_dictionary['division_name']).send_keys(division_name)
        self.find_element(*self.locator_dictionary['direct_id_division']).send_keys(direct_id)
        self.find_element(*self.locator_dictionary['create_division_btn']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_edited_division(self, edited_division):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_division'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_division'])
        link_2 = link_1.text
        link_3 = edited_division
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_class(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['classes'])))
        del wait
        self.find_element(*self.locator_dictionary['classes']).click()
        time.sleep(1)

    def click_create_class(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['create_class'])))
        del wait
        self.find_element(*self.locator_dictionary['create_class']).click()
        time.sleep(1)

    def create_class(self,class_name,direct_id):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['class_name'])
        del page4
        self.find_element(*self.locator_dictionary['class_name']).send_keys(class_name)
        self.find_element(*self.locator_dictionary['direct_id_class']).send_keys(direct_id)
        self.find_element(*self.locator_dictionary['create_class_btn']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_create_class_btn(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_class'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['create_class'])
        link_2 = link_1.text
        link_3 = "Create Class"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_create_class_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_create_class_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_create_class_modal'])
        link_2 = link_1.text
        link_3 = "Create a Class"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_created_class(self,created_class):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_class'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_class'])
        link_2 = link_1.text
        link_3 = created_class
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_edit_class_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edit_class_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edit_class_modal'])
        link_2 = link_1.text
        link_3 = "Update a Class"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_edit_class(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_class_ellipses'])
        del page4
        time.sleep(1)
        self.find_element(*self.locator_dictionary['edit_class_ellipses']).click()
        time.sleep(1)

    def org_admin_click_edit_class(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['org_admin_edit_class_ellipses'])
        del page4
        time.sleep(1)
        self.find_element(*self.locator_dictionary['org_admin_edit_class_ellipses']).click()
        time.sleep(1)

    def click_edit_class_btn(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_class'])
        del page4
        self.find_element(*self.locator_dictionary['edit_class']).click()
        time.sleep(1)

    def edit_class(self,class_name,direct_id):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['class_name'])
        del page4
        self.find_element(*self.locator_dictionary['class_name']).clear()
        self.find_element(*self.locator_dictionary['direct_id_class']).clear()
        self.find_element(*self.locator_dictionary['class_name']).send_keys(class_name)
        self.find_element(*self.locator_dictionary['direct_id_class']).send_keys(direct_id)
        self.find_element(*self.locator_dictionary['create_class_btn']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_edited_class(self,edited_class):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_class'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_class'])
        link_2 = link_1.text
        link_3 = edited_class
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def mousehover_click_people(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mouse_hover_element'])
        del page4
        self.find_element(*self.locator_dictionary['mouse_hover_element']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['People']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait