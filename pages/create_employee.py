from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import calendar
from selenium.webdriver.support.select import Select
from pages.create_user_api import *
from environment import email_before_gmail_domain

orgs = Create_user.getOrgs()
class Create_employeePage(BasePage):
    locator_dictionary = {
        "create_an_employee_btn": (By.LINK_TEXT,"Create an Employee"),
        "create_an_employee_option": (By.XPATH, "//a[text()='Create an Employee']"),
        "verify_create_employee_modal":(By.XPATH,"//h4[text()='Create an Employee']"),
        "fname_employee": (By.NAME, "first_name"),
        "middle_name_employee": (By.NAME, "middle_name"),
        "lname_employee": (By.NAME, "last_name"),
        "email_employee": (By.NAME, "email"),
        "verify_employee_checkbox_selected":(By.XPATH,"//label[@for='checkboxG4']"),
        "select_group":(By.NAME,"selected_group"),
        "select_division":(By.NAME,"selected_division"),
        "select_class":(By.NAME,"selected_class"),
        "open_calendar":(By.NAME,"doh"),
        # "choose_date":(By.XPATH,"//table//tbody//tr[1]//td[6]"),
        "choose_date":(By.XPATH,"//table[@role='grid']/tbody//tr//td[@role='gridcell']//span[not(@class='disabled') and not(@class ='disabled is-other-month') and not(@class='is-other-month')]"),
        "ssn":(By.NAME,"ssn"),
        "edit_ssn":(By.NAME,"ssn1"),
        "org_admin_checkbox_no": (By.XPATH, "//label[@for='checkbox60']"),
        "create_employee":(By.XPATH,"//button[text()='Create Employee']"),
        "apply_employee_filter":(By.XPATH,"//select"),
        "search_employee":(By.NAME,"search"),
        "verify_pending_employee":(By.XPATH,"(//table/tbody/tr[2]/td[1])[1]"),
        "pending_state":(By.XPATH,"//table/tbody/tr[2]/td[4]"),
        "employee_tab":(By.XPATH,"//span[text()='Employees']"),
        "employee_checkbox_no":(By.XPATH,"//label[@for='checkboxG5']"),
        "select_permission_org_admin":(By.NAME,"selected_permission"),
        "edit_employee_ellipse":(By.XPATH,"(//div[@class='btn-more-options'])[1]"),
        "edit_employee_btn":(By.LINK_TEXT,"Edit Employee"),
        "save_changes":(By.XPATH,"//button[text()='Save Changes']"),
        "benemax_logo":(By.XPATH,"//figure[@class='headerlogo org-logo']"),
        "back_to_admin":(By.LINK_TEXT,"Back to Admin"),
        "people":(By.LINK_TEXT,"People"),
        "programs":(By.LINK_TEXT,"Programs"),
        "deactivate_employee":(By.LINK_TEXT,"Deactivate Employee"),
        "yes_deactivate":(By.XPATH,"//footer//span"),
        "activate_employee": (By.LINK_TEXT, "Activate Employee"),
        "yes_activate": (By.XPATH, "//footer//span"),
        "verify_employee_dashboard":(By.XPATH,"//*[text()='Your Tasks']"),
        "verify_edit_employee_modal":(By.XPATH,"//h4[text()='Update an Employee']"),
        "loader": (By.ID, "api-loader")

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def access_employee_tab(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['employee_tab'])
        del page4
        self.find_element(*self.locator_dictionary['employee_tab']).click()
        time.sleep(1)

    def verify_employee_tab(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['employee_tab'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['employee_tab'])
        link_2 = link_1.text
        link_3 = "Employees"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_employee_edit_employee_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edit_employee_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edit_employee_modal'])
        link_2 = link_1.text
        link_3 = "Update an Employee"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_edit_employee(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_employee_ellipse'])
        del page4
        self.find_element(*self.locator_dictionary['edit_employee_ellipse']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['edit_employee_btn']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_employee_dashboard(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_employee_dashboard'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_employee_dashboard'])
        link_2 = link_1.text
        link_3 = "Your Tasks"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_create_employee_btn(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_an_employee_btn'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['create_an_employee_btn'])
        link_2 = link_1.text
        link_3 = "Create an Employee"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_create_employee(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_an_employee_btn'])
        del page4
        self.find_element(*self.locator_dictionary['create_an_employee_btn']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['create_an_employee_option']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_create_employee_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_create_employee_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_create_employee_modal'])
        link_2 = link_1.text
        link_3 = "Create an Employee"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def create_employee(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi1")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain1")
        a = email_before_gmail_domain+"+"+"20"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        self.find_element(*self.locator_dictionary['org_admin_checkbox_no']).click()
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d=b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele :
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break

        # self.find_element(*self.locator_dictionary['choose_date']).click()
        # time.sleep(1)
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_enroll_employee(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi_enroll")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain")
        page = Create_user(self)
        a = page.benemaxadmin_email1
        del page
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break

        # self.find_element(*self.locator_dictionary['choose_date']).click()
        # time.sleep(1)
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        time.sleep(1)
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_employee2(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi1")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain1")
        a = email_before_gmail_domain+"+"+"21"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        self.find_element(*self.locator_dictionary['org_admin_checkbox_no']).click()
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d=b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele :
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break

        # self.find_element(*self.locator_dictionary['choose_date']).click()
        # time.sleep(1)
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_employee3(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi2")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain1")
        a = email_before_gmail_domain+"+"+"22"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        self.find_element(*self.locator_dictionary['org_admin_checkbox_no']).click()
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d=b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele :
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break

        # self.find_element(*self.locator_dictionary['choose_date']).click()
        # time.sleep(1)
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_employee_org_admin(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("Nainsi4")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("Jain4")
        a = orgs['EditEmployeeEmail']
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Read")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_employee_org_admin_pending(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("Nainsi#")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("Jain#")
        a = email_before_gmail_domain+"+"+"23"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_employee_org_admin_pending(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Pending Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys("Nainsi#")
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['edit_employee_ellipse']).click()
        self.find_element(*self.locator_dictionary['edit_employee_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Read")
        del select
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_himself_org_admin(self,emp_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(emp_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['edit_employee_ellipse']).click()
        self.find_element(*self.locator_dictionary['edit_employee_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Read")
        del select
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_employee_org_admin_himself(self,group_name,division_name,class_name,emp_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys(emp_name)
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("Jain%")
        a = orgs['BenemaxAdminEmail']
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_pending_state_created_employee(self,pending_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Pending Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(pending_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "nainsi1"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_pending_state_created_employee2(self,pending_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Pending Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(pending_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "nainsi2"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_pending_state_created_employee1(self,pending_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Pending Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(pending_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "Nainsi#"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_pending_state_employee(self):
        link_1 = self.find_element(*self.locator_dictionary['pending_state'])
        link_2 = link_1.text
        link_3 = "Pending"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_active_state_created_employee(self,active_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(active_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "Nainsi2"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_active_state_created_employee2(self,active_employee_name,verify_emp_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(active_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = verify_emp_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_active_state_created_employee3(self,active_employee_name,verify_emp_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(active_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = verify_emp_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_active_state_employee(self):
        link_1 = self.find_element(*self.locator_dictionary['pending_state'])
        link_2 = link_1.text
        link_3 = "Active"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def create_org_admin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi3")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain3")
        a = email_before_gmail_domain+"+"+"24"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        self.find_element(*self.locator_dictionary['employee_checkbox_no']).click()
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_org_admin1(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi3")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain3")
        a = email_before_gmail_domain+"+"+"25"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        self.find_element(*self.locator_dictionary['employee_checkbox_no']).click()
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_org_admin2(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi4")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain3")
        a = email_before_gmail_domain+"+"+"26"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        self.find_element(*self.locator_dictionary['employee_checkbox_no']).click()
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_pending_state_created_orgadmin(self,pending_orgadmin_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Pending Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(pending_orgadmin_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "nainsi3"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_pending_state_created_orgadmin1(self,pending_orgadmin_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Pending Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(pending_orgadmin_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "nainsi4"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_pending_state_orgadmin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['pending_state'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['pending_state'])
        link_2 = link_1.text
        link_3 = "Pending"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_active_state_created_org_admin(self,active_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(active_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "Nainsi4"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_active_state_orgadmin(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['pending_state'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['pending_state'])
        link_2 = link_1.text
        link_3 = "Active"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def create_org_admin_employee(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi5")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain5")
        a = email_before_gmail_domain+"+"+"27"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_org_admin_employee1(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi5")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain5")
        a = email_before_gmail_domain+"+"+"28"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_org_admin_employee2(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fname_employee'])
        del page4
        self.find_element(*self.locator_dictionary['fname_employee']).send_keys("nainsi6")
        self.find_element(*self.locator_dictionary['middle_name_employee']).send_keys("j")
        self.find_element(*self.locator_dictionary['lname_employee']).send_keys("jain5")
        a = email_before_gmail_domain+"+"+"29"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
        self.find_element(*self.locator_dictionary['email_employee']).send_keys(a)
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        self.find_element(*self.locator_dictionary['ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        select_permission = self.find_element(*self.locator_dictionary['select_permission_org_admin'])
        select = Select(select_permission)
        select.select_by_visible_text("Edit")
        del select
        self.find_element(*self.locator_dictionary['create_employee']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_pending_state_created_orgadmin_employee(self,pending_orgadmin_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Pending Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(pending_orgadmin_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "nainsi5"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_pending_state_created_orgadmin_employee1(self,pending_orgadmin_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Pending Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(pending_orgadmin_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "nainsi6"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_pending_state_orgadmin_employee(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['pending_state'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['pending_state'])
        link_2 = link_1.text
        link_3 = "Pending"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_active_state_created_org_admin_employee(self,active_employee_orgadmin_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(active_employee_orgadmin_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "Nainsi6"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_active_state_orgadmin_employee(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['pending_state'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['pending_state'])
        link_2 = link_1.text
        link_3 = "Active"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def edit_employee_remove_org_admin_make_employee(self,group_name,division_name,class_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys("Nainsi4")
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        self.find_element(*self.locator_dictionary['edit_employee_ellipse']).click()
        self.find_element(*self.locator_dictionary['edit_employee_btn']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['org_admin_checkbox_no']).click()
        self.find_element(*self.locator_dictionary['verify_employee_checkbox_selected']).click()
        select_group = self.find_element(*self.locator_dictionary['select_group'])
        select = Select(select_group)
        select.select_by_visible_text(group_name)
        del select
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        select_division = self.find_element(*self.locator_dictionary['select_division'])
        select = Select(select_division)
        select.select_by_visible_text(division_name)
        del select
        select_class = self.find_element(*self.locator_dictionary['select_class'])
        select = Select(select_class)
        select.select_by_visible_text(class_name)
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['open_calendar']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        self.find_element(*self.locator_dictionary['edit_ssn']).send_keys(str(calendar.timegm(time.gmtime())))
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_employee_remove_org_admin_make_employee1(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['org_admin_checkbox_no'])
        del page4
        self.find_element(*self.locator_dictionary['org_admin_checkbox_no']).click()
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_back_to_admin(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['benemax_logo'])
        del page4
        self.find_element(*self.locator_dictionary['benemax_logo']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['back_to_admin']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_programs(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['benemax_logo'])
        del page4
        self.find_element(*self.locator_dictionary['benemax_logo']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['programs']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait



    def click_people_org_admin(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['benemax_logo'])
        del page4
        self.find_element(*self.locator_dictionary['benemax_logo']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['people']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def search_employee_deactivate_him(self,active_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(active_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['edit_employee_ellipse']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['deactivate_employee']).click()
        wait = WebDriverWait(self.browser, 6)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['yes_deactivate'])))
        del wait
        self.find_element(*self.locator_dictionary['yes_deactivate']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_deactive_state_edited__employee(self,deactive_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Deactive Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(deactive_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "Nainsi4"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_deactive_state_employee(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['pending_state'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['pending_state'])
        link_2 = link_1.text
        link_3 = "Deactive"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        time.sleep(2)

    def search_employee_activate_him(self,deactive_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Deactive Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(deactive_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['edit_employee_ellipse']).click()
        self.find_element(*self.locator_dictionary['activate_employee']).click()
        wait = WebDriverWait(self.browser, 6)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['yes_activate'])))
        del wait
        self.find_element(*self.locator_dictionary['yes_activate']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_active_state_created_employee1(self,active_employee_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_employee_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_employee_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Employees")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_employee']).send_keys(active_employee_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_employee'])
        link_2 = link_1.text
        link_3 = "Nainsi4"
        assert link_2 == link_3, "Visible text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

