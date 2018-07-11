from selenium.webdriver.common.by import By
from pages.base_page_object import *
from datetime import timedelta
from datetime import datetime
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import calendar
from selenium.webdriver.support.select import Select
from environment import *


class Create_ProgramPage(BasePage):
    locator_dictionary = {
        "create_program_modal": (By.XPATH, "//h4[text()='Create a Program']"),
        "create_program": (By.XPATH,"//span[text()='Create Program ']"),
        "program_name": (By.NAME, "name"),
        "calendar_enroll_start_date":(By.NAME,"enrollement_start_date"),
        "calendar_enroll_end_date":(By.NAME,"enrollement_end_date"),
        "calendar_program_start_date":(By.NAME,"effective_start_date"),
        "calendar_program_end_date":(By.NAME,"effective_end_date"),
        "choose_date": (By.XPATH, "//table[@role='grid']/tbody//tr//td[@role='gridcell']//span[not(@class='disabled') and not(@class ='disabled is-other-month') and not(@class='is-other-month')]"),
        "continue_btn":(By.XPATH,"//button[text()='Continue']"),
        "select_grp":(By.XPATH,"//label[@for='Group0']"),
        "select_division":(By.XPATH,"//label[@for='Division0']"),
        "select_class":(By.XPATH,"//label[@for='Class0']"),
        "create_program_btn":(By.XPATH,"//button[text()='Create Program']"),
        "apply_program_filter": (By.XPATH, "//select"),
        "search_program": (By.NAME, "search"),
        "verify_pending_program": (By.XPATH, "(//table/tbody/tr[2]/td[1])[1]"),
        "edit_program_ellipse": (By.XPATH, "(//div[@class='btn-more-options'])[1]"),
        "edit_program_btn": (By.XPATH, "//ul[@role='menu']/li[1]/a"),
        "verify_edit_program_modal": (By.XPATH, "//h4[text()='Edit Program']"),
        "save_changes":(By.XPATH,"//button[text()='Save Changes']"),
        "active_state": (By.XPATH,"//table/tbody/tr[2]/td[2]"),
        "deactivate_program_btn": (By.XPATH, "//table/tbody/tr[2]/td[6]/div/ul/li[2]/a"),
        "verify_deactivate_program_modal": (By.XPATH, "//span[text()='Yes, Deactivate']"),
        "click_deactivate_btn":(By.XPATH,"//footer/button[2]"),
        "verify_activate_program_modal": (By.XPATH, "//span[text()='Yes, Activate']"),
        "click_activate_btn": (By.XPATH, "//footer/button[2]"),
        "loader": (By.ID, "api-loader"),
        "next_month": (By.XPATH,"//button[@class='next']"),
        "previous_month":(By.XPATH,"//button[@class='previous']"),
        "month":(By.XPATH,"(//button[@class='current']//span)[1]")

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    # def remove_zero(self, day1):
    #     if day1 == "0":
    #         day2 = day1.replace("0", "")
    #         print(day2)
    #     else:
    #         day2 = day1

    def click_create_program(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_program'])
        del page4
        self.find_element(*self.locator_dictionary['create_program']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_create_program_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_program_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['create_program_modal'])
        link_2 = link_1.text
        link_3 = "Create a Program"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def create_program_pending(self,group_name,division_name,class_name,program_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['program_name'])
        del page4
        self.find_element(*self.locator_dictionary['program_name']).clear()
        self.find_element(*self.locator_dictionary['program_name']).send_keys(program_name)
        b1 = (datetime.now()+timedelta(days=1)).strftime('%d')
        print(b1)
        if b1[0] == "0":
            d1 = b1.replace("0", "")
            print(d1)
        else:
            d1 = b1

        self.find_element(*self.locator_dictionary['calendar_enroll_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        elen1 = self.find_elements(*self.locator_dictionary['choose_date'])
        lia = []
        for elem1 in elen1 :
            lia.append(elem1.text)
            global test1
            test1= lia
            print(test1)
        if not (d1 in test1):
            self.find_element(*self.locator_dictionary['next_month']).click()
        elen2 = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele1 in elen2:
            if ele1.text == d1:
                print("enter in first if loop")
                print(ele1.text)
                time.sleep(1)
                ele1.click()
                break
        time.sleep(2)
        del b1,d1,elen1,elen2,test1,lia

        b2 = (datetime.now() + timedelta(days=2)).strftime('%d')
        print(b2)
        if b2[0] == "0":
            d2 = b2.replace("0", "")
            print(d2)
        else:
            d2 = b2
        self.find_element(*self.locator_dictionary['calendar_enroll_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
        elen3 = self.find_elements(*self.locator_dictionary['choose_date'])
        lib1 = []
        for elem2 in elen3 :
            lib1.append(elem2.text)
            global test2
            test2 = lib1
            print(test2)
        if not (d2 in test2):
            self.find_element(*self.locator_dictionary['next_month']).click()
        elen4 = self.find_elements(*self.locator_dictionary['choose_date'])

        print("get all the dates")
        for ele2 in elen4:
            if ele2.text == d2:
                print("enter in second if loop")
                print(ele2.text)
                time.sleep(1)
                ele2.click()
                break
        time.sleep(2)
        del b2, d2, elen3, elen4, test2, lib1

        b3 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b3)
        if b3[0] == "0":
            d3 = b3.replace("0", "")
            print(d3)
        else:
            d3 = b3
        self.find_element(*self.locator_dictionary['calendar_program_start_date']).click()
        time.sleep(1)
        print("Click on third Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia3 = []
        for elem3 in ele:
            lia3.append(elem3.text)
            global test3
            test3 = lia3
            print(test3)
        if not (d3 in test3):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele3 in ele:
            if ele3.text == d3:
                print("enter in third if loop")
                print(ele3.text)
                time.sleep(1)
                ele3.click()
                break
        time.sleep(2)
        del b3, d3, ele, test3, lia3

        b4 = (datetime.now() + timedelta(days=4)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['calendar_program_end_date']).click()
        time.sleep(1)
        print("Click on fourth Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia4 = []
        for elem4 in ele:
            lia4.append(elem4.text)
            global test4
            test4 = lia4
            print(test4)
        if not (d4 in test4):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele4 in ele:
            if ele4.text == d4 :
                print("enter in third if loop")
                print(ele4.text)
                time.sleep(1)
                ele4.click()
                break

        del b4, d4, ele, test4, lia4
        self.find_element(*self.locator_dictionary['continue_btn']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_grp']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['select_division']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_class']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['create_program_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_pending_program(self,pending_program_name,verify_pending_program):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_program_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_program_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Upcoming Programs")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).send_keys(pending_program_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_program'])
        link_2 = link_1.text
        link_3 = verify_pending_program
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        link_1 = self.find_element(*self.locator_dictionary['active_state'])
        link_2 = link_1.text
        link_3 = "Active"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_edit_program(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_program_ellipse'])
        del page4
        self.find_element(*self.locator_dictionary['edit_program_ellipse']).click()
        self.find_element(*self.locator_dictionary['edit_program_btn']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_program_to_open_enrollment(self,group_name,division_name,class_name,program_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['program_name'])
        del page4
        self.find_element(*self.locator_dictionary['program_name']).clear()
        self.find_element(*self.locator_dictionary['program_name']).send_keys(program_name)
        b1 = (datetime.now()).strftime('%d')
        e1 = (datetime.now()).strftime('%B')
        print(b1)
        print(e1)
        if b1[0] == "0":
            d1 = b1.replace("0", "")
            print(d1)
        else:
            d1 = b1
        self.find_element(*self.locator_dictionary['calendar_enroll_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        current_month = self.find_element(*self.locator_dictionary['month'])
        current_month1 = current_month.text
        print(current_month1)
        if (e1 != current_month1):
            self.find_element(*self.locator_dictionary['previous_month']).click()
        elen1 = self.find_elements(*self.locator_dictionary['choose_date'])
        lia = []
        for elem1 in elen1:
            lia.append(elem1.text)
            global test1
            test1 = lia
            print(test1)
        if not (d1 in test1):
            self.find_element(*self.locator_dictionary['next_month']).click()

        elen2 = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele1 in elen2:
            if ele1.text == d1:
                print("enter in first if loop")
                print(ele1.text)
                time.sleep(1)
                ele1.click()
                break
        time.sleep(2)
        del b1, current_month, current_month1, d1, elen1, elen2, test1, lia

        b2 = (datetime.now() + timedelta(days=1)).strftime('%d')
        e2 = (datetime.now() + timedelta(days=1)).strftime('%B')
        print(b2)
        print(e2)
        if b2[0] == "0":
            d2 = b2.replace("0", "")
            print(d2)
        else:
            d2 = b2
        self.find_element(*self.locator_dictionary['calendar_enroll_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
        current_month2 = self.find_element(*self.locator_dictionary['month'])
        current_month3 = current_month2.text
        print(current_month3)
        if (e2 != current_month3):
            self.find_element(*self.locator_dictionary['previous_month']).click()
        elen3 = self.find_elements(*self.locator_dictionary['choose_date'])
        lib1 = []
        for elem2 in elen3:
            lib1.append(elem2.text)
            global test2
            test2 = lib1
            print(test2)
        if not (d2 in test2):
            self.find_element(*self.locator_dictionary['next_month']).click()

        elen4 = self.find_elements(*self.locator_dictionary['choose_date'])

        print("get all the dates")
        for ele2 in elen4:
            if ele2.text == d2:
                print("enter in second if loop")
                print(ele2.text)
                time.sleep(1)
                ele2.click()
                break
        time.sleep(2)
        del b2, current_month2, current_month3, d2, elen3, elen4, test2, lib1

        b3 = (datetime.now() + timedelta(days=2)).strftime('%d')
        e3 = (datetime.now() + timedelta(days=2)).strftime('%B')
        print(b3)
        print(e3)
        if b3[0] == "0":
            d3 = b3.replace("0", "")
            print(d3)
        else:
            d3 = b3
        self.find_element(*self.locator_dictionary['calendar_program_start_date']).click()
        time.sleep(1)
        print("Click on third Calendar")
        current_month4 = self.find_element(*self.locator_dictionary['month'])
        current_month5 = current_month4.text
        print(current_month5)
        if (e3 != current_month5):
            self.find_element(*self.locator_dictionary['previous_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia3 = []
        for elem3 in ele:
            lia3.append(elem3.text)
            global test3
            test3 = lia3
            print(test3)
        if not (d3 in test3):
            self.find_element(*self.locator_dictionary['next_month']).click()

        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele3 in ele:
            if ele3.text == d3:
                print("enter in third if loop")
                print(ele3.text)
                time.sleep(1)
                ele3.click()
                break
        time.sleep(2)
        del b3, current_month4, current_month5, d3, ele, test3, lia3

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        e4 = (datetime.now() + timedelta(days=3)).strftime('%B')
        print(b4)
        print(e4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['calendar_program_end_date']).click()
        time.sleep(1)
        print("Click on fourth Calendar")
        current_month6 = self.find_element(*self.locator_dictionary['month'])
        current_month7 = current_month6.text
        print(current_month7)
        if (e4 != current_month7):
            self.find_element(*self.locator_dictionary['previous_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia4 = []
        for elem4 in ele:
            lia4.append(elem4.text)
            global test4
            test4 = lia4
            print(test4)
        if not (d4 in test4):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele4 in ele:
            if ele4.text == d4:
                print("enter in third if loop")
                print(ele4.text)
                time.sleep(1)
                ele4.click()
                break
        del b4, current_month6, current_month7, d4, ele, test4, lia4
        self.find_element(*self.locator_dictionary['continue_btn']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_grp']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['select_division']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_class']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['create_program_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_pending_program_to_open_enrollment(self,edit_program_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['program_name'])
        del page4
        self.find_element(*self.locator_dictionary['program_name']).clear()
        self.find_element(*self.locator_dictionary['program_name']).send_keys(edit_program_name)
        b1 = (datetime.now()).strftime('%d')
        e1 = (datetime.now()).strftime('%B')
        print(b1)
        print(e1)
        if b1[0] == "0":
            d1 = b1.replace("0", "")
            print(d1)
        else:
            d1 = b1
        self.find_element(*self.locator_dictionary['calendar_enroll_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        current_month = self.find_element(*self.locator_dictionary['month'])
        current_month1 = current_month.text
        print(current_month1)
        if (e1 != current_month1):
            self.find_element(*self.locator_dictionary['previous_month']).click()
        elen1 = self.find_elements(*self.locator_dictionary['choose_date'])
        lia = []
        for elem1 in elen1:
            lia.append(elem1.text)
            global test1
            test1 = lia
            print(test1)
        if not (d1 in test1):
            self.find_element(*self.locator_dictionary['next_month']).click()

        elen2 = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele1 in elen2:
            if ele1.text == d1:
                print("enter in first if loop")
                print(ele1.text)
                time.sleep(1)
                ele1.click()
                break
        time.sleep(2)
        del b1, current_month, current_month1, d1, elen1, elen2, test1, lia

        b2 = (datetime.now() + timedelta(days=1)).strftime('%d')
        e2 = (datetime.now() + timedelta(days=1)).strftime('%B')
        print(b2)
        print(e2)
        if b2[0] == "0":
            d2 = b2.replace("0", "")
            print(d2)
        else:
            d2 = b2
        self.find_element(*self.locator_dictionary['calendar_enroll_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
        current_month2 = self.find_element(*self.locator_dictionary['month'])
        current_month3 = current_month2.text
        print(current_month3)
        if (e2 != current_month3):
            self.find_element(*self.locator_dictionary['previous_month']).click()
        elen3 = self.find_elements(*self.locator_dictionary['choose_date'])
        lib1 = []
        for elem2 in elen3:
            lib1.append(elem2.text)
            global test2
            test2 = lib1
            print(test2)
        if not (d2 in test2):
            self.find_element(*self.locator_dictionary['next_month']).click()

        elen4 = self.find_elements(*self.locator_dictionary['choose_date'])

        print("get all the dates")
        for ele2 in elen4:
            if ele2.text == d2:
                print("enter in second if loop")
                print(ele2.text)
                time.sleep(1)
                ele2.click()
                break
        time.sleep(2)
        del b2, current_month2, current_month3, d2, elen3, elen4, test2, lib1

        b3 = (datetime.now() + timedelta(days=2)).strftime('%d')
        e3 = (datetime.now() + timedelta(days=2)).strftime('%B')
        print(b3)
        print(e3)
        if b3[0] == "0":
            d3 = b3.replace("0", "")
            print(d3)
        else:
            d3 = b3
        self.find_element(*self.locator_dictionary['calendar_program_start_date']).click()
        time.sleep(1)
        print("Click on third Calendar")
        current_month4 = self.find_element(*self.locator_dictionary['month'])
        current_month5 = current_month4.text
        print(current_month5)
        if (e3 != current_month5):
            self.find_element(*self.locator_dictionary['previous_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia3 = []
        for elem3 in ele:
            lia3.append(elem3.text)
            global test3
            test3 = lia3
            print(test3)
        if not (d3 in test3):
            self.find_element(*self.locator_dictionary['next_month']).click()

        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele3 in ele:
            if ele3.text == d3:
                print("enter in third if loop")
                print(ele3.text)
                time.sleep(1)
                ele3.click()
                break
        time.sleep(2)
        del b3, current_month4, current_month5, d3, ele, test3, lia3

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        e4 = (datetime.now() + timedelta(days=3)).strftime('%B')
        print(b4)
        print(e4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['calendar_program_end_date']).click()
        time.sleep(1)
        print("Click on fourth Calendar")
        current_month6 = self.find_element(*self.locator_dictionary['month'])
        current_month7 = current_month6.text
        print(current_month7)
        if (e4 != current_month7):
            self.find_element(*self.locator_dictionary['previous_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia4 = []
        for elem4 in ele:
            lia4.append(elem4.text)
            global test4
            test4 = lia4
            print(test4)
        if not (d4 in test4):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele4 in ele:
            if ele4.text == d4:
                print("enter in third if loop")
                print(ele4.text)
                time.sleep(1)
                ele4.click()
                break
        del b4, current_month6, current_month7, d4, ele, test4, lia4
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_open_enrollment_program(self,enroll_program_name,verify_enroll_program):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_program_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_program_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Open Enrollment Programs")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).send_keys(enroll_program_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_program'])
        link_2 = link_1.text
        link_3 = verify_enroll_program
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        link_1 = self.find_element(*self.locator_dictionary['active_state'])
        link_2 = link_1.text
        link_3 = "Active"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def deactivate_verify_program(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_program_ellipse'])
        del page4
        self.find_element(*self.locator_dictionary['edit_program_ellipse']).click()
        self.find_element(*self.locator_dictionary['deactivate_program_btn']).click()
        time.sleep(1)
        link_1 = self.find_element(*self.locator_dictionary['verify_deactivate_program_modal'])
        link_2 = link_1.text
        link_3 = "Yes, Deactivate"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        time.sleep(1)
        self.find_element(*self.locator_dictionary['click_deactivate_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_deactive_program(self,deactive_program_name,verify_deactive_program):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_program_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_program_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Deactive Programs")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).send_keys(deactive_program_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_program'])
        link_2 = link_1.text
        link_3 = verify_deactive_program
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        link_1 = self.find_element(*self.locator_dictionary['active_state'])
        link_2 = link_1.text
        link_3 = "Deactive"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def activate_verify_program(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_program_ellipse'])
        del page4
        self.find_element(*self.locator_dictionary['edit_program_ellipse']).click()
        self.find_element(*self.locator_dictionary['deactivate_program_btn']).click()
        time.sleep(1)
        link_1 = self.find_element(*self.locator_dictionary['verify_activate_program_modal'])
        link_2 = link_1.text
        link_3 = "Yes, Activate"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        self.find_element(*self.locator_dictionary['click_activate_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def activate_enroll_program_via_db(self):
        import psycopg2
        conn = psycopg2.connect(database=databse, user=user, password=password,host=host, port=port)
        cur = conn.cursor()
        print(cur)
        cur.execute("select id,enrollement_start_date,enrollement_end_date,effective_start_date,effective_end_date from program order by id desc limit 1")
        row = cur.fetchone()
        print(row)
        from datetime import timedelta
        p_id = row[0]
        dy1 = (row[1] + timedelta(days=-2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        dy2 = (row[2] + timedelta(days=-2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        print(dy1)
        print(dy2)
        cur.execute("update program set enrollement_start_date = %s,enrollement_end_date = %s where id = %s", (dy1, dy2, p_id,))
        conn.commit()
        cur.execute("select id,enrollement_start_date,enrollement_end_date,effective_start_date,effective_end_date from program order by id desc limit 1")
        row = cur.fetchone()
        print(row)
        conn.close()

    def verify_active_program(self,active_program_name,verify_active_program):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_program_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_program_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Active Programs")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).send_keys(active_program_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_program'])
        link_2 = link_1.text
        link_3 = verify_active_program
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        link_1 = self.find_element(*self.locator_dictionary['active_state'])
        link_2 = link_1.text
        link_3 = "Active"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def archive_active_program_via_db(self):
        import psycopg2
        conn = psycopg2.connect(database=databse, user=user, password=password,host=host, port=port)
        cur = conn.cursor()
        print(cur)
        cur.execute("select id,enrollement_start_date,enrollement_end_date,effective_start_date,effective_end_date from program order by id desc limit 1")
        row = cur.fetchone()
        print(row)
        from datetime import timedelta
        p_id = row[0]
        dy1 = (row[1] + timedelta(days=-2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        dy2 = (row[2] + timedelta(days=-2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        dy3 = (row[1] + timedelta(days=-4)).strftime("%Y-%m-%dT%H:%M:%SZ")
        dy4 = (row[2] + timedelta(days=-4)).strftime("%Y-%m-%dT%H:%M:%SZ")
        print(dy1)
        print(dy2)
        print(dy3)
        print(dy4)
        cur.execute("update program set enrollement_start_date = %s,enrollement_end_date = %s,effective_start_date = %s,effective_end_date = %s where id = %s", (dy1, dy2, dy3, dy4, p_id,))
        conn.commit()
        cur.execute("select id,enrollement_start_date,enrollement_end_date,effective_start_date,effective_end_date from program order by id desc limit 1")
        row = cur.fetchone()
        print(row)
        conn.close()

    def verify_archive_program(self,archive_program_name,verify_archive_program):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_program_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_program_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Archived Programs")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_program']).send_keys(archive_program_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((By.ID, "api-loader")))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_pending_program'])
        link_2 = link_1.text
        link_3 = verify_archive_program
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        link_1 = self.find_element(*self.locator_dictionary['active_state'])
        link_2 = link_1.text
        link_3 = "Active"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
