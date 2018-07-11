from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import calendar
from selenium.webdriver.support.select import Select
from environment import *
from datetime import datetime
from datetime import timedelta
from pages.signup_claim_account import *
# from tkinter import filedialog
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class Create_BenefitPage(BasePage):
    locator_dictionary = {
        "access_program": (By.XPATH, "(//table/tbody/tr[2]/td[1])[1]"),
        "create_a_benefit":(By.XPATH,"//a//span[text()='Create a Benefit']"),
        "verify_create_benefit_modal": (By.XPATH, "//h4[text()='Create Benefit ']"),
        "select_carrier":(By.NAME,"carrier"),
        "select_loc": (By.NAME, "loc"),
        "select_plan_type": (By.NAME, "plan_type"),
        "carrier_plan_name":(By.NAME,"plan_name"),
        "display_name":(By.NAME,"display_name"),
        "benefit_start_date":(By.NAME,"start_date"),
        "benefit_end_date": (By.NAME, "end_date"),
        "benefit_renewel_date":(By.NAME,"renewal_date"),
        "choose_date": (By.XPATH,"//table[@role='grid']/tbody//tr//td[@role='gridcell']//span[not(@class='disabled') and not(@class ='disabled is-other-month') and not(@class='is-other-month')]"),
        "choose_date1": (By.XPATH,"(//table[@role='grid']/tbody//tr//td[@role='gridcell']//span[not(@class='disabled') and not(@class ='disabled is-other-month') and not(@class='is-other-month')])[1]"),
        "direct_id":(By.NAME,"direct_id"),
        "popup": (By.XPATH, "//div[@class='close-button']"),
        "close_edit_benefit":(By.XPATH,"//a[@class='close-modal']"),
        "terms_condition":(By.XPATH,"//label[@for='checkboxG2']"),
        "next_month": (By.XPATH, "//button[@class='next']"),

        "mi_primary_care_physician":(By.NAME,"PCP"),
        "mi_hsa_qualified1":(By.NAME,"HSAB"),
        "mi_hsa_qualified2": (By.NAME, "HSAW"),
        "mi_co_pay": (By.NAME, "co_pay"),
        "mi_deductible":(By.NAME,"deductible"),
        "mi_rx_coverage": (By.NAME, "rx_coverage"),

        "fsa_maximum_contribution":(By.NAME, "max_contribution"),
        "fsa_pay_period":(By.NAME,"pay_period"),
        "edit_fsa_maximum_contribution":(By.NAME, "maximum_contribution"),
        "edit_fsa_pay_period": (By.NAME, "contribution_interval"),

        "continue":(By.XPATH,"//footer//button"),
        "text_editor": (By.XPATH, "(//div[@dir='auto'])[2]"),
        "text_editor1": (By.XPATH, "(//div[@dir='auto'])[4]"),
        "link_name":(By.XPATH,"//input[@placeholder='Link Name']"),
        "url":(By.XPATH,"//input[@placeholder='URL']"),
        "url_close_btn":(By.XPATH,"(//button[@class='check-button check-remove'])[1]"),
        "url_open_btn":(By.XPATH,"(//button[@class='check-button'])[1]"),
        "doc_close_btn":(By.XPATH,"(//button[@class='check-button check-remove'])[1]"),
        "upload_file":(By.XPATH,"//div[@class='drop-container']//label[@class='upload-button']//input[@type='file']"),
        "upload_file1": (By.XPATH, "(//div[@class='drop-container']//label[@class='upload-button']//input[@type='file'])[1]"),
        "upload_button":(By.XPATH,"//label[@class='upload-button']"),
        "continue2":(By.XPATH,"(//footer//button)[2]"),

        "select_group": (By.XPATH, "//label[@for='checkboxG0']"),
        "grp_id":(By.XPATH,"//input[@placeholder='Group ID']"),
        "select_dvsn": (By.XPATH, "//label[@for='checkboxGs0']"),
        "select_cls": (By.XPATH, "//label[@for='checkboxse0']"),
        "continue3": (By.XPATH, "(//footer//button)[2]"),

        "employee":(By.XPATH,"(//article[@class='card-body']/section//input)[1]"),
        "employee_spouse": (By.XPATH, "(//article[@class='card-body']/section//input)[2]"),
        "employee_child": (By.XPATH, "(//article[@class='card-body']/section//input)[3]"),
        "employee_children": (By.XPATH, "(//article[@class='card-body']/section//input)[4]"),
        "family": (By.XPATH, "(//article[@class='card-body']/section//input)[5]"),
        "create_benefit_btn":(By.XPATH,"//button[@type='submit']"),

        "select_benefit":(By.XPATH,"(//div[@class='row']//select)[1]"),
        "verify_benefit_name":(By.XPATH,"(//table/tbody/tr[2]/td[1])[1]"),
        "verify_benefit_loc":(By.XPATH,"(//table/tbody/tr[2]/td[1])[1]"),
        "verify_benefit_status":(By.XPATH,"(//table/tbody/tr[2]/td[4])[1]"),
        "search_benefit":(By.NAME,"search"),

        "edit_benefit_btn":(By.XPATH,"(//div[@class='btn-more-options'])[1]"),
        "edit_benefit_optn":(By.XPATH,"(//ul//li[@role='menuitem']//a)[1]"),
        "activate_deactivate_benefit":(By.XPATH,"(//ul//li[@role='menuitem']//a)[2]"),
        "verify_deactivate_modal":(By.XPATH,"//span[text()='Yes, Deactivate']"),
        "verify_activate_modal": (By.XPATH, "//span[text()='Yes, Activate']"),
        "benefit_second_slide":(By.XPATH,"//span[text()='Details']"),
        "benefit_third_slide":(By.XPATH,"//span[text()='Availability']"),
        "benefit_fourth_slide": (By.XPATH, "//span[text()='Rates']"),

        "verify_edit_benefit_modal": (By.XPATH, "//h4[text()='Edit Benefit']"),
        "save_changes":(By.XPATH,"//button[text()='Save Changes']"),
        "click_deactivate_btn":(By.XPATH,"//footer/button[2]"),
        "click_activate_btn": (By.XPATH, "//footer/button[2]"),
        "loader": (By.ID, "api-loader"),

        "edit_mi_primary_care_physician":(By.NAME,"primary_care_physician"),
        "edit_mi_hsa_qualified1": (By.NAME, "hsa_qualified_base_plan"),
        "edit_mi_hsa_qualified2": (By.NAME, "hsa_qualified_wrap_plan"),
        "edit_mi_co_pay": (By.NAME, "co_pay"),
        "edit_mi_deductible": (By.NAME, "deductible"),
        "edit_mi_rx_coverage": (By.NAME, "rx_coverage"),
        "voluntary":(By.XPATH,"//section//form//select[@disabled]/option"),
        "voluntary1": (By.XPATH, "(//section//form//select[@disabled]//option)[12]"),
        "verify_loc_mi":(By.XPATH,"(//section//form//select[@disabled]//option)[2]"),
        "verify_loc_di": (By.XPATH, "(//section//form//select[@disabled]//option)[3]"),
        "verify_loc_vi": (By.XPATH, "(//section//form//select[@disabled]//option)[4]"),
        "verify_loc_ai": (By.XPATH, "(//section//form//select[@disabled]//option)[5]"),
        "verify_loc_fsa": (By.XPATH, "(//section//form//select[@disabled]//option)[6]"),
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def verify_benefit_dashboard(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_a_benefit'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['create_a_benefit'])
        link_2 = link_1.text
        link_3 = "Create a Benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def click_program(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_program'])
        del page4
        self.find_element(*self.locator_dictionary['access_program']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_create_benefit(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['create_a_benefit'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['create_a_benefit'])))
        del wait
        self.find_element(*self.locator_dictionary['create_a_benefit']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_create_benefit_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_create_benefit_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_create_benefit_modal'])
        link_2 = link_1.text
        link_3 = "Create Benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def create_medical_insurance_benefit(self,group_name,division_name,class_name,benefit_display_name,carrier_plan_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        select_loc = self.find_element(*self.locator_dictionary['select_loc'])
        select = Select(select_loc)
        select.select_by_visible_text("Medical Insurance")
        del select
        select_carrier = self.find_element(*self.locator_dictionary['select_plan_type'])
        select = Select(select_carrier)
        select.select_by_value("HMO")
        del select
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(benefit_display_name)
        # element = self.find_element(*self.locator_dictionary['direct_id'])
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        # del element
        time.sleep(1)
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()

        b4 = (datetime.now() + timedelta(days=4)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on third Calendar")
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

        del b4, d4, ele, test4, lia4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        # self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi")
        select_mi_primary_care = self.find_element(*self.locator_dictionary['mi_primary_care_physician'])
        select = Select(select_mi_primary_care)
        select.select_by_value("yes")
        del select
        select_mi_hsa1 = self.find_element(*self.locator_dictionary['mi_hsa_qualified1'])
        select = Select(select_mi_hsa1)
        select.select_by_value("yes")
        del select
        select_mi_hsa2 = self.find_element(*self.locator_dictionary['mi_hsa_qualified2'])
        select = Select(select_mi_hsa2)
        select.select_by_value("yes")
        del select
        # self.find_element(*self.locator_dictionary['mi_co_pay']).clear()
        self.find_element(*self.locator_dictionary['mi_co_pay']).send_keys("nainsi1")
        # self.find_element(*self.locator_dictionary['mi_deductible']).clear()
        self.find_element(*self.locator_dictionary['mi_deductible']).send_keys("nainsi2")
        # self.find_element(*self.locator_dictionary['mi_rx_coverage']).clear()
        self.find_element(*self.locator_dictionary['mi_rx_coverage']).send_keys("nainsi3")

        self.find_element(*self.locator_dictionary['continue']).click()
        time.sleep(1)
        # self.find_element(*self.locator_dictionary['text_editor']).clear()
        self.find_element(*self.locator_dictionary['text_editor']).click()
        self.find_element(*self.locator_dictionary['text_editor']).send_keys("Hey! Creating new Benefit.Please check to enroll in it.")
        self.find_element(*self.locator_dictionary['text_editor']).send_keys("Hey! Creating new Benefit.Please check to enroll in it.")
        # self.find_element(*self.locator_dictionary['link_name']).clear()
        self.find_element(*self.locator_dictionary['link_name']).send_keys("benemax")
        # self.find_element(*self.locator_dictionary['url']).clear()
        self.find_element(*self.locator_dictionary['url']).send_keys("http://benemax.com")
        time.sleep(1)
        try:
            element = self.find_element(*self.locator_dictionary['url_open_btn'])
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
            del element
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            wait = WebDriverWait(self.browser, 15)
            wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
            del wait
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            time.sleep(1)
            page = ClaimAccountPage(context=self)
            page.verify_error_msg("Attachment with this name already exists")
            del page
        except:
            print("unable to upload file")
        self.find_element(*self.locator_dictionary['continue2']).click()
        time.sleep(1)

        self.find_element(*self.locator_dictionary['select_group']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        # self.find_element(*self.locator_dictionary['grp_id']).clear()
        self.find_element(*self.locator_dictionary['grp_id']).send_keys("nainsi4")
        self.find_element(*self.locator_dictionary['select_dvsn']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_cls']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['continue3']).click()
        time.sleep(1)

        # self.find_element(*self.locator_dictionary['employee']).clear()
        self.find_element(*self.locator_dictionary['employee']).send_keys("10")
        # self.find_element(*self.locator_dictionary['employee_spouse']).clear()
        self.find_element(*self.locator_dictionary['employee_spouse']).send_keys("20")
        # self.find_element(*self.locator_dictionary['employee_child']).clear()
        self.find_element(*self.locator_dictionary['employee_child']).send_keys("30")
        # self.find_element(*self.locator_dictionary['employee_children']).clear()
        self.find_element(*self.locator_dictionary['employee_children']).send_keys("40")
        # self.find_element(*self.locator_dictionary['family']).clear()
        self.find_element(*self.locator_dictionary['family']).send_keys("50")

        self.find_element(*self.locator_dictionary['create_benefit_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_dental_insurance_benefit(self,group_name,division_name,class_name,benefit_display_name,carrier_plan_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        select_loc = self.find_element(*self.locator_dictionary['select_loc'])
        select = Select(select_loc)
        select.select_by_visible_text("Dental Insurance")
        del select
        select_carrier = self.find_element(*self.locator_dictionary['select_plan_type'])
        select = Select(select_carrier)
        select.select_by_value("STD")
        del select
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(benefit_display_name)
        # element = self.find_element(*self.locator_dictionary['direct_id'])
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        # del element
        time.sleep(1)
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on third Calendar")
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

        del b4, d4, ele, test4, lia4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        # self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi")

        self.find_element(*self.locator_dictionary['continue']).click()
        time.sleep(1)
        # self.find_element(*self.locator_dictionary['text_editor']).clear()
        self.find_element(*self.locator_dictionary['text_editor']).click()
        self.find_element(*self.locator_dictionary['text_editor']).send_keys("Hey! Creating new Benefit.Please check to enroll in it.")
        # self.find_element(*self.locator_dictionary['link_name']).clear()
        self.find_element(*self.locator_dictionary['link_name']).send_keys("benemax")
        # self.find_element(*self.locator_dictionary['url']).clear()
        self.find_element(*self.locator_dictionary['url']).send_keys("http://benemax.com")
        time.sleep(1)
        try:
            element = self.find_element(*self.locator_dictionary['url_open_btn'])
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
            del element
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            wait = WebDriverWait(self.browser, 15)
            wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
            del wait
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            time.sleep(1)
            page = ClaimAccountPage(context=self)
            page.verify_error_msg("Attachment with this name already exists")
            del page
        except:
            print("unable to upload file")
        self.find_element(*self.locator_dictionary['continue2']).click()
        time.sleep(1)

        self.find_element(*self.locator_dictionary['select_group']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        # self.find_element(*self.locator_dictionary['grp_id']).clear()
        self.find_element(*self.locator_dictionary['grp_id']).send_keys("nainsi4")
        self.find_element(*self.locator_dictionary['select_dvsn']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_cls']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['continue3']).click()
        time.sleep(1)

        # self.find_element(*self.locator_dictionary['employee']).clear()
        self.find_element(*self.locator_dictionary['employee']).send_keys("10")
        # self.find_element(*self.locator_dictionary['employee_spouse']).clear()
        self.find_element(*self.locator_dictionary['employee_spouse']).send_keys("20")
        # self.find_element(*self.locator_dictionary['employee_child']).clear()
        self.find_element(*self.locator_dictionary['employee_child']).send_keys("30")
        # self.find_element(*self.locator_dictionary['employee_children']).clear()
        self.find_element(*self.locator_dictionary['employee_children']).send_keys("40")
        # self.find_element(*self.locator_dictionary['family']).clear()
        self.find_element(*self.locator_dictionary['family']).send_keys("50")

        self.find_element(*self.locator_dictionary['create_benefit_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_vision_insurance_benefit(self,group_name,division_name,class_name,benefit_display_name,carrier_plan_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        select_loc = self.find_element(*self.locator_dictionary['select_loc'])
        select = Select(select_loc)
        select.select_by_visible_text("Vision Insurance")
        del select
        select_carrier = self.find_element(*self.locator_dictionary['select_plan_type'])
        select = Select(select_carrier)
        select.select_by_value("STD")
        del select
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(benefit_display_name)
        # element = self.find_element(*self.locator_dictionary['direct_id'])
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        # del element
        time.sleep(1)
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on third Calendar")
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

        del b4, d4, ele, test4, lia4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        # self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi")

        self.find_element(*self.locator_dictionary['continue']).click()
        time.sleep(1)
        # self.find_element(*self.locator_dictionary['text_editor']).clear()
        self.find_element(*self.locator_dictionary['text_editor']).click()
        self.find_element(*self.locator_dictionary['text_editor']).send_keys("Hey! Creating new Benefit.Please check to enroll in it.")
        # self.find_element(*self.locator_dictionary['link_name']).clear()
        self.find_element(*self.locator_dictionary['link_name']).send_keys("benemax")
        # self.find_element(*self.locator_dictionary['url']).clear()
        self.find_element(*self.locator_dictionary['url']).send_keys("http://benemax.com")
        time.sleep(1)
        try:
            element = self.find_element(*self.locator_dictionary['url_open_btn'])
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
            del element
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            wait = WebDriverWait(self.browser, 15)
            wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
            del wait
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            time.sleep(1)
            page = ClaimAccountPage(context=self)
            page.verify_error_msg("Attachment with this name already exists")
            del page
        except:
            print("unable to upload file")
        self.find_element(*self.locator_dictionary['continue2']).click()
        time.sleep(1)

        self.find_element(*self.locator_dictionary['select_group']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        # self.find_element(*self.locator_dictionary['grp_id']).clear()
        self.find_element(*self.locator_dictionary['grp_id']).send_keys("nainsi4")
        self.find_element(*self.locator_dictionary['select_dvsn']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_cls']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['continue3']).click()
        time.sleep(1)

        # self.find_element(*self.locator_dictionary['employee']).clear()
        self.find_element(*self.locator_dictionary['employee']).send_keys("10")
        # self.find_element(*self.locator_dictionary['employee_spouse']).clear()
        self.find_element(*self.locator_dictionary['employee_spouse']).send_keys("20")
        # self.find_element(*self.locator_dictionary['employee_child']).clear()
        self.find_element(*self.locator_dictionary['employee_child']).send_keys("30")
        # self.find_element(*self.locator_dictionary['employee_children']).clear()
        self.find_element(*self.locator_dictionary['employee_children']).send_keys("40")
        # self.find_element(*self.locator_dictionary['family']).clear()
        self.find_element(*self.locator_dictionary['family']).send_keys("50")

        self.find_element(*self.locator_dictionary['create_benefit_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_ancillary_insurance_benefit(self,group_name,division_name,class_name,benefit_display_name,carrier_plan_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        select_loc = self.find_element(*self.locator_dictionary['select_loc'])
        select = Select(select_loc)
        select.select_by_visible_text("Ancillary Insurance")
        del select
        select_carrier = self.find_element(*self.locator_dictionary['select_plan_type'])
        select = Select(select_carrier)
        select.select_by_value("STD")
        del select
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(benefit_display_name)
        # element = self.find_element(*self.locator_dictionary['direct_id'])
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        # del element
        time.sleep(1)
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on third Calendar")
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

        del b4, d4, ele, test4, lia4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        # self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi")
        link_1 = self.find_element(*self.locator_dictionary['voluntary'])
        link_2 = link_1.text
        link_3 = "Yes"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3
        self.find_element(*self.locator_dictionary['continue']).click()
        time.sleep(1)
        # self.find_element(*self.locator_dictionary['text_editor']).clear()
        self.find_element(*self.locator_dictionary['text_editor']).click()
        self.find_element(*self.locator_dictionary['text_editor']).send_keys("Hey! Creating new Benefit.Please check to enroll in it.")
        self.find_element(*self.locator_dictionary['terms_condition']).click()
        self.find_element(*self.locator_dictionary['text_editor1']).click()
        self.find_element(*self.locator_dictionary['text_editor1']).send_keys("Hey! Creating new Benefit.Please check to enroll in it.")
        # self.find_element(*self.locator_dictionary['link_name']).clear()
        self.find_element(*self.locator_dictionary['link_name']).send_keys("benemax")
        # self.find_element(*self.locator_dictionary['url']).clear()
        self.find_element(*self.locator_dictionary['url']).send_keys("http://benemax.com")
        time.sleep(1)
        try:
            element = self.find_element(*self.locator_dictionary['url_open_btn'])
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
            del element
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            wait = WebDriverWait(self.browser, 15)
            wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
            del wait
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            time.sleep(1)
            page = ClaimAccountPage(context=self)
            page.verify_error_msg("Attachment with this name already exists")
            del page
        except:
            print("unable to upload file")
        self.find_element(*self.locator_dictionary['continue2']).click()
        time.sleep(1)

        self.find_element(*self.locator_dictionary['select_group']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        # self.find_element(*self.locator_dictionary['grp_id']).clear()
        self.find_element(*self.locator_dictionary['grp_id']).send_keys("nainsi4")
        self.find_element(*self.locator_dictionary['select_dvsn']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_cls']).click()
        time.sleep(1)

        self.find_element(*self.locator_dictionary['create_benefit_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def create_fsa_insurance_benefit(self,group_name,division_name,class_name,benefit_display_name,carrier_plan_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        select_loc = self.find_element(*self.locator_dictionary['select_loc'])
        select = Select(select_loc)
        select.select_by_visible_text("Flexible Spending Account")
        del select
        select_carrier = self.find_element(*self.locator_dictionary['select_plan_type'])
        select = Select(select_carrier)
        select.select_by_value("HFSA")
        del select
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(benefit_display_name)
        # element = self.find_element(*self.locator_dictionary['direct_id'])
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        # del element
        time.sleep(1)
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
        self.find_element(*self.locator_dictionary['choose_date1']).click()

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on third Calendar")
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

        del b4, d4, ele, test4, lia4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        # self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi")
        # self.find_element(*self.locator_dictionary['fsa_maximum_contribution']).clear()
        self.find_element(*self.locator_dictionary['fsa_maximum_contribution']).send_keys("123")
        select_benefit = self.find_element(*self.locator_dictionary['fsa_pay_period'])
        select = Select(select_benefit)
        select.select_by_visible_text("Month")
        del select
        self.find_element(*self.locator_dictionary['continue']).click()
        time.sleep(1)
        # self.find_element(*self.locator_dictionary['text_editor']).clear()
        self.find_element(*self.locator_dictionary['text_editor']).click()
        self.find_element(*self.locator_dictionary['text_editor']).send_keys("Hey! Creating new Benefit.Please check to enroll in it.")
        self.find_element(*self.locator_dictionary['terms_condition']).click()
        self.find_element(*self.locator_dictionary['text_editor1']).click()
        self.find_element(*self.locator_dictionary['text_editor1']).send_keys("Hey! Creating new Benefit.Please check to enroll in it.")
        # self.find_element(*self.locator_dictionary['link_name']).clear()
        self.find_element(*self.locator_dictionary['link_name']).send_keys("benemax")
        # self.find_element(*self.locator_dictionary['url']).clear()
        self.find_element(*self.locator_dictionary['url']).send_keys("http://benemax.com")
        time.sleep(1)
        try:
            element = self.find_element(*self.locator_dictionary['url_open_btn'])
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
            del element
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            wait = WebDriverWait(self.browser, 15)
            wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
            del wait
            time.sleep(1)
            self.find_element(*self.locator_dictionary['upload_file']).send_keys(os.getcwd() + "/benemax_doc.txt")
            time.sleep(1)
            page = ClaimAccountPage(context=self)
            page.verify_error_msg("Attachment with this name already exists")
            del page
        except:
            print("unable to upload file")
        self.find_element(*self.locator_dictionary['continue2']).click()
        time.sleep(1)

        self.find_element(*self.locator_dictionary['select_group']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        # self.find_element(*self.locator_dictionary['grp_id']).clear()
        self.find_element(*self.locator_dictionary['grp_id']).send_keys("nainsi4")
        self.find_element(*self.locator_dictionary['select_dvsn']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['select_cls']).click()
        time.sleep(1)

        self.find_element(*self.locator_dictionary['create_benefit_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_pending_benefit(self,pending_benefit_name,verify_pending_benefit):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_benefit'])
        del page4
        select_benefit = self.find_element(*self.locator_dictionary['select_benefit'])
        select = Select(select_benefit)
        select.select_by_visible_text("Upcoming Benefits")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).send_keys(pending_benefit_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_name'])
        link_2 = link_1.text
        link_3 = verify_pending_benefit
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_status'])
        link_2 = link_1.text
        link_3 = "Active"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3



    def verify_medical_benefit(self,medical_benefit_name,verify_medical_benefit):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_benefit'])
        del page4
        select_benefit = self.find_element(*self.locator_dictionary['select_benefit'])
        select = Select(select_benefit)
        select.select_by_visible_text("Medical Insurance")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).send_keys(medical_benefit_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_name'])
        link_2 = link_1.text
        link_3 = verify_medical_benefit
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3

    def verify_dental_benefit(self,dental_benefit_name,verify_dental_benefit):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_benefit'])
        del page4
        select_benefit = self.find_element(*self.locator_dictionary['select_benefit'])
        select = Select(select_benefit)
        select.select_by_visible_text("Dental Insurance")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).send_keys(dental_benefit_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_name'])
        link_2 = link_1.text
        link_3 = verify_dental_benefit
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_vision_benefit(self,vision_benefit_name,verify_vision_benefit):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_benefit'])
        del page4
        select_benefit = self.find_element(*self.locator_dictionary['select_benefit'])
        select = Select(select_benefit)
        select.select_by_visible_text("Vision Insurance")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).send_keys(vision_benefit_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_name'])
        link_2 = link_1.text
        link_3 = verify_vision_benefit
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_ancillary_benefit(self,ancillary_benefit_name,verify_ancillary_benefit):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_benefit'])
        del page4
        select_benefit = self.find_element(*self.locator_dictionary['select_benefit'])
        select = Select(select_benefit)
        select.select_by_visible_text("Ancillary Insurance")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).send_keys(ancillary_benefit_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_name'])
        link_2 = link_1.text
        link_3 = verify_ancillary_benefit
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_fsa_benefit(self,fsa_benefit_name,verify_fsa_benefit):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_benefit'])
        del page4
        select_benefit = self.find_element(*self.locator_dictionary['select_benefit'])
        select = Select(select_benefit)
        select.select_by_visible_text("Flexible Spending Accounts")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).send_keys(fsa_benefit_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_name'])
        link_2 = link_1.text
        link_3 = verify_fsa_benefit
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_benefit_loc(self,benefit_loc_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_benefit_loc'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_loc'])
        link_2 = link_1.text
        link_3 = benefit_loc_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3

    def click_edit_benefit(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_benefit_btn'])
        del page4
        self.find_element(*self.locator_dictionary['edit_benefit_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['edit_benefit_optn'])))
        del wait
        self.find_element(*self.locator_dictionary['edit_benefit_optn']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_edit_benefit_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edit_benefit_modal'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edit_benefit_modal'])
        link_2 = link_1.text
        link_3 = "Edit Benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def edit_benefit_firstslide_mi(self,carrier_plan_name,edit_benefit_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        link_1 = self.find_element(*self.locator_dictionary['verify_loc_mi'])
        link_2 = link_1.text
        link_3 = "Medical Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(edit_benefit_name)
        element = self.find_element(*self.locator_dictionary['direct_id'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        b3 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b3)
        if b3[0] == "0":
            d3 = b3.replace("0", "")
            print(d3)
        else:
            d3 = b3
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
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
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
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
            if ele4.text == d4:
                print("enter in third if loop")
                print(ele4.text)
                time.sleep(1)
                ele4.click()
                break

        del b4, d4, ele, test4, lia4
        b5 = (datetime.now() + timedelta(days=5)).strftime('%d')
        print(b5)
        if b5[0] == "0":
            d5 = b5.replace("0", "")
            print(d5)
        else:
            d5 = b5
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia5 = []
        for elem5 in ele:
            lia5.append(elem5.text)
            global test5
            test5 = lia5
            print(test5)
        if not (d5 in test5):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele5 in ele:
            if ele5.text == d5:
                print("enter in third if loop")
                print(ele5.text)
                time.sleep(1)
                ele5.click()
                break
        time.sleep(2)
        del b5, d5, ele, test5, lia5
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi_d1")
        select_mi_primary_care = self.find_element(*self.locator_dictionary['edit_mi_primary_care_physician'])
        select = Select(select_mi_primary_care)
        select.select_by_value("false")
        del select
        select_mi_hsa1 = self.find_element(*self.locator_dictionary['edit_mi_hsa_qualified1'])
        select = Select(select_mi_hsa1)
        select.select_by_value("false")
        del select
        select_mi_hsa2 = self.find_element(*self.locator_dictionary['edit_mi_hsa_qualified2'])
        select = Select(select_mi_hsa2)
        select.select_by_value("false")
        del select
        self.find_element(*self.locator_dictionary['edit_mi_co_pay']).clear()
        self.find_element(*self.locator_dictionary['edit_mi_co_pay']).send_keys("nainsi_co1")
        self.find_element(*self.locator_dictionary['edit_mi_deductible']).clear()
        self.find_element(*self.locator_dictionary['edit_mi_deductible']).send_keys("nainsi_de2")
        self.find_element(*self.locator_dictionary['edit_mi_rx_coverage']).clear()
        self.find_element(*self.locator_dictionary['edit_mi_rx_coverage']).send_keys("nainsi_rx3")

        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_benefit_firstslide_di(self,carrier_plan_name,edit_benefit_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        link_1 = self.find_element(*self.locator_dictionary['verify_loc_di'])
        link_2 = link_1.text
        link_3 = "Dental Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(edit_benefit_name)
        element = self.find_element(*self.locator_dictionary['direct_id'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        b3 = (datetime.now() + timedelta(days=2)).strftime('%d')
        print(b3)
        if b3[0] == "0":
            d3 = b3.replace("0", "")
            print(d3)
        else:
            d3 = b3
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
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

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
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
        del b4, d4, ele, test4, lia4
        b5 = (datetime.now() + timedelta(days=4)).strftime('%d')
        print(b5)
        if b5[0] == "0":
            d5 = b5.replace("0", "")
            print(d5)
        else:
            d5 = b5
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia5 = []
        for elem5 in ele:
            lia5.append(elem5.text)
            global test5
            test5 = lia5
            print(test5)
        if not (d5 in test5):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele5 in ele:
            if ele5.text == d5:
                print("enter in third if loop")
                print(ele5.text)
                time.sleep(1)
                ele5.click()
                break
        time.sleep(2)
        del b5, d5, ele, test5, lia5
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi_d1")

        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_benefit_firstslide_vi(self,carrier_plan_name,edit_benefit_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        link_1 = self.find_element(*self.locator_dictionary['verify_loc_vi'])
        link_2 = link_1.text
        link_3 = "Vision Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(edit_benefit_name)
        element = self.find_element(*self.locator_dictionary['direct_id'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        b3 = (datetime.now() + timedelta(days=2)).strftime('%d')
        print(b3)
        if b3[0] == "0":
            d3 = b3.replace("0", "")
            print(d3)
        else:
            d3 = b3
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
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

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
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
        del b4, d4, ele, test4, lia4
        b5 = (datetime.now() + timedelta(days=4)).strftime('%d')
        print(b5)
        if b5[0] == "0":
            d5 = b5.replace("0", "")
            print(d5)
        else:
            d5 = b5
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia5 = []
        for elem5 in ele:
            lia5.append(elem5.text)
            global test5
            test5 = lia5
            print(test5)
        if not (d5 in test5):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele5 in ele:
            if ele5.text == d5:
                print("enter in third if loop")
                print(ele5.text)
                time.sleep(1)
                ele5.click()
                break
        time.sleep(2)
        del b5, d5, ele, test5, lia5
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi_d1")

        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_benefit_firstslide_ai(self,carrier_plan_name,edit_benefit_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        link_1 = self.find_element(*self.locator_dictionary['verify_loc_ai'])
        link_2 = link_1.text
        link_3 = "Ancillary Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(edit_benefit_name)
        element = self.find_element(*self.locator_dictionary['direct_id'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        b3 = (datetime.now() + timedelta(days=2)).strftime('%d')
        print(b3)
        if b3[0] == "0":
            d3 = b3.replace("0", "")
            print(d3)
        else:
            d3 = b3
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
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

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
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
        del b4, d4, ele, test4, lia4
        b5 = (datetime.now() + timedelta(days=4)).strftime('%d')
        print(b5)
        if b5[0] == "0":
            d5 = b5.replace("0", "")
            print(d5)
        else:
            d5 = b5
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia5 = []
        for elem5 in ele:
            lia5.append(elem5.text)
            global test5
            test5 = lia5
            print(test5)
        if not (d5 in test5):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele5 in ele:
            if ele5.text == d5:
                print("enter in third if loop")
                print(ele5.text)
                time.sleep(1)
                ele5.click()
                break
        time.sleep(2)
        del b5, d5, ele, test5, lia5
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi_d1")
        link_1 = self.find_element(*self.locator_dictionary['voluntary1'])
        link_2 = link_1.text
        link_3 = "Yes"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def edit_benefit_firstslide_fsa(self,carrier_plan_name,edit_benefit_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['carrier_plan_name'])
        del page4
        select_carrier = self.find_element(*self.locator_dictionary['select_carrier'])
        select = Select(select_carrier)
        select.select_by_value("1")
        del select
        link_1 = self.find_element(*self.locator_dictionary['verify_loc_fsa'])
        link_2 = link_1.text
        link_3 = "Flexible Spending Account"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        self.find_element(*self.locator_dictionary['carrier_plan_name']).clear()
        self.find_element(*self.locator_dictionary['carrier_plan_name']).send_keys(carrier_plan_name)
        self.find_element(*self.locator_dictionary['display_name']).clear()
        self.find_element(*self.locator_dictionary['display_name']).send_keys(edit_benefit_name)
        element = self.find_element(*self.locator_dictionary['direct_id'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        b3 = (datetime.now() + timedelta(days=2)).strftime('%d')
        print(b3)
        if b3[0] == "0":
            d3 = b3.replace("0", "")
            print(d3)
        else:
            d3 = b3
        self.find_element(*self.locator_dictionary['benefit_start_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
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

        b4 = (datetime.now() + timedelta(days=3)).strftime('%d')
        print(b4)
        if b4[0] == "0":
            d4 = b4.replace("0", "")
            print(d4)
        else:
            d4 = b4
        self.find_element(*self.locator_dictionary['benefit_end_date']).click()
        time.sleep(1)
        print("Click on second Calendar")
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
        del b4, d4, ele, test4, lia4
        b5 = (datetime.now() + timedelta(days=4)).strftime('%d')
        print(b5)
        if b5[0] == "0":
            d5 = b5.replace("0", "")
            print(d5)
        else:
            d5 = b5
        self.find_element(*self.locator_dictionary['benefit_renewel_date']).click()
        time.sleep(1)
        print("Click on first Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        lia5 = []
        for elem5 in ele:
            lia5.append(elem5.text)
            global test5
            test5 = lia5
            print(test5)
        if not (d5 in test5):
            self.find_element(*self.locator_dictionary['next_month']).click()
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        print("get all the dates")
        for ele5 in ele:
            if ele5.text == d5:
                print("enter in third if loop")
                print(ele5.text)
                time.sleep(1)
                ele5.click()
                break
        time.sleep(2)
        del b5, d5, ele, test5, lia5
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['direct_id'])))
        del wait
        self.find_element(*self.locator_dictionary['direct_id']).clear()
        self.find_element(*self.locator_dictionary['direct_id']).send_keys("nainsi_d1")
        # self.find_element(*self.locator_dictionary['fsa_maximum_contribution']).clear()
        self.find_element(*self.locator_dictionary['edit_fsa_maximum_contribution']).send_keys("1234")
        select_benefit = self.find_element(*self.locator_dictionary['edit_fsa_pay_period'])
        select = Select(select_benefit)
        select.select_by_visible_text("Year")
        del select
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_benefit_second_slide(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['benefit_second_slide'])
        del page4
        self.find_element(*self.locator_dictionary['benefit_second_slide']).click()
        self.find_element(*self.locator_dictionary['text_editor']).clear()
        self.find_element(*self.locator_dictionary['text_editor']).click()
        self.find_element(*self.locator_dictionary['text_editor']).send_keys("Hey! Updating new Benefit.Please check to enroll in it.")
        self.find_element(*self.locator_dictionary['url_open_btn']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['url_close_btn']).click()
        self.find_element(*self.locator_dictionary['link_name']).clear()
        self.find_element(*self.locator_dictionary['link_name']).send_keys("benemax1")
        self.find_element(*self.locator_dictionary['url']).clear()
        self.find_element(*self.locator_dictionary['url']).send_keys("http://benemax1.com")
        time.sleep(1)
        element = self.find_element(*self.locator_dictionary['url_open_btn'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        print("scroll is performing")
        wait = WebDriverWait(self.browser, 20)
        doc_close_btn = wait.until(EC.visibility_of_element_located((self.locator_dictionary['doc_close_btn'])))
        doc_close_btn.click()
        del wait
        # self.find_element(*self.locator_dictionary['doc_close_btn']).click()
        print("click on doc close button")
        try :
         time.sleep(1)
         wait = WebDriverWait(self.browser, 10)
         wait.until(EC.alert_is_present(), 'Timed out waiting for alert to be present ' +
                       'confirmation popup to appear.')
         del wait
         alert = self.browser.switch_to.alert
         alert.accept()
         print("alert accepted")
        except:
            print("unable to switch on alert")
        a1 = os.getcwd()
        print(a1)
        a2 = self.find_element(*self.locator_dictionary['upload_file'])
        a2.send_keys(a1 + "/benemax_doc1.txt")
        del a1,a2
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        element1 = self.find_element(*self.locator_dictionary['doc_close_btn'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element1)
        del element1
        time.sleep(1)
        print("second scroll is performing")

        a5 = os.getcwd()
        print(a5)
        wait = WebDriverWait(self.browser, 10)
        a6 = wait.until(EC.presence_of_element_located((self.locator_dictionary['upload_file'])))
        del wait
        a6.send_keys(a5 + "/benemax_doc2.txt")
        del a5, a6
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)

        a3 = os.getcwd()
        print(a3)
        wait = WebDriverWait(self.browser, 10)
        a4 = wait.until(EC.presence_of_element_located((self.locator_dictionary['upload_file'])))
        del wait
        a4.send_keys(a3 + "/benemax_doc1.txt")
        del a3, a4
        time.sleep(1)
        page = ClaimAccountPage(context=self)
        page.verify_error_msg("Attachment with this name already exists")
        del page
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_benefit_third_slide(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['benefit_third_slide'])
        del page4
        self.find_element(*self.locator_dictionary['benefit_third_slide']).click()
        self.find_element(*self.locator_dictionary['grp_id']).clear()
        self.find_element(*self.locator_dictionary['grp_id']).send_keys("nainsi4_updating")
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_benefit_fourth_slide(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['benefit_fourth_slide'])
        del page4
        self.find_element(*self.locator_dictionary['benefit_fourth_slide']).click()
        self.find_element(*self.locator_dictionary['employee']).clear()
        self.find_element(*self.locator_dictionary['employee']).send_keys("50")
        self.find_element(*self.locator_dictionary['employee_spouse']).clear()
        self.find_element(*self.locator_dictionary['employee_spouse']).send_keys("40")
        self.find_element(*self.locator_dictionary['employee_child']).clear()
        self.find_element(*self.locator_dictionary['employee_child']).send_keys("30")
        self.find_element(*self.locator_dictionary['employee_children']).clear()
        self.find_element(*self.locator_dictionary['employee_children']).send_keys("20")
        self.find_element(*self.locator_dictionary['family']).clear()
        self.find_element(*self.locator_dictionary['family']).send_keys("10")
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def close_edit_benefit(self):
        try:
            wait = WebDriverWait(self.browser, 15)
            a = wait.until(EC.visibility_of_element_located((self.locator_dictionary['popup'])))
            del wait
            a.click()
        except:
            print("close button is not displayed")

        wait = WebDriverWait(self.browser, 15)
        b = wait.until(EC.visibility_of_element_located((self.locator_dictionary['close_edit_benefit'])))
        del wait
        b.click()

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

    def deactivate_verify_benefit(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_benefit_btn'])
        del page4
        self.find_element(*self.locator_dictionary['edit_benefit_btn']).click()
        self.find_element(*self.locator_dictionary['activate_deactivate_benefit']).click()
        time.sleep(1)
        link_1 = self.find_element(*self.locator_dictionary['verify_deactivate_modal'])
        link_2 = link_1.text
        link_3 = "Yes, Deactivate"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3
        time.sleep(1)
        self.find_element(*self.locator_dictionary['click_deactivate_btn']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_deactive_benefit(self,deactive_benefit_name,verify_deactive_benefit):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_benefit'])
        del page4
        select_benefit = self.find_element(*self.locator_dictionary['select_benefit'])
        select = Select(select_benefit)
        select.select_by_visible_text("Deactive Benefits")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).clear()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['search_benefit']).send_keys(deactive_benefit_name)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_name'])
        link_2 = link_1.text
        link_3 = verify_deactive_benefit
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
        link_1 = self.find_element(*self.locator_dictionary['verify_benefit_status'])
        link_2 = link_1.text
        link_3 = "Deactive"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def activate_verify_benefit(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['edit_benefit_btn'])
        del page4
        self.find_element(*self.locator_dictionary['edit_benefit_btn']).click()
        self.find_element(*self.locator_dictionary['activate_deactivate_benefit']).click()
        time.sleep(1)
        link_1 = self.find_element(*self.locator_dictionary['verify_activate_modal'])
        link_2 = link_1.text
        link_3 = "Yes, Activate"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        time.sleep(1)
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
