from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os


class CreateOrganizationPage(BasePage):
    locator_dictionary = {
        "Organization_AfterLogin": (By.XPATH, "//span[text()='Create Organization']"),
        "Legal_name": (By.XPATH,"//input[@name='legal_name']"),
        "Appearance": (By.XPATH,"//h3[text()='Appearance']"),
        "dba": (By.XPATH, "//input[@name='dba']"),
        "select_corporation_type": (By.XPATH, "//*[@id='org-slide1']//div[4]/select"),
        "tax_id": (By.XPATH, "//input[@name='tax_id']"),
        "sic_code":(By.XPATH, "//input[@name='sic_code']"),
        "select_payroll_company": (By.XPATH, "//*[@id='org-slide1']//div[7]/select"),
        "phone": (By.XPATH, "//input[@name='phone']"),
        "fax" : (By.XPATH, "//input[@name='fax']"),
        "website": (By.XPATH, "//input[@name='website']"),
        "business_address_1" : (By.XPATH,"//input[@name='business_address_1']"),
        "business_address_2": (By.XPATH, "//input[@name='business_address_2']"),
        "business_city": (By.XPATH, "//input[@name='business_city']"),
        "select_state": (By.XPATH, "//*[@id='org-slide1']//div[14]/select"),
        "business_zip": (By.XPATH, "//input[@name='business_zip']"),
        "mailing_address_1": (By.XPATH, "//input[@name='mailing_address_1']"),
        "mailing_address_2": (By.XPATH, "//input[@name='mailing_address_2']"),
        "mailing_city": (By.XPATH, "//input[@name='mailing_city']"),
        "select_city": (By.XPATH, "//*[@id='org-slide1']//div[20]/select"),
        "mailing_zip": (By.XPATH, "//input[@name='mailing_zip']"),
        "checkbox": (By.XPATH, "//label[@class='css-label']"),
        "continue_button": (By.XPATH, "//button[text()='Continue']"),
        "org_disp_name":(By.XPATH, "//input[@name='display_name']"),
        "image_logo":(By.XPATH,"//div[@class='drop-container uploadimage-step1']/input"),
        "continue_button_2": (By.XPATH, "//form/footer//button[2]"),
        "administration":(By.XPATH,"//h3[text()='Administration']"),
        "ase": (By.XPATH, "//input[@name='ASE']"),
        "ase_name": (By.XPATH, "//*[@id='org-slide3']//button[1]/p"),
        "ima": (By.XPATH, "//input[@name='IMA']"),
        "ima_name": (By.XPATH, "//*[@id='org-slide3']//button[1]/p"),
        "cp": (By.XPATH, "//input[@name='CP']"),
        "cp_name": (By.XPATH, "//*[@id='org-slide3']//button[1]/p"),
        "ec": (By.XPATH, "//input[@name='EC']"),
        "ec_name": (By.XPATH, "//*[@id='org-slide3']//button[1]/p"),
        "producer": (By.XPATH, "//input[@name='Producer']"),
        "producer_name": (By.XPATH, "//*[@id='org-slide3']//button[1]/p"),
        "direct_id": (By.XPATH, "//input[@name='direct_id']"),
        "select_administration": (By.XPATH, "//*[@id='org-slide3']//select"),
        "finish": (By.XPATH, "//footer//button[@type='submit']"),
        "verify_created_organization":(By.XPATH, "//table//tr[2]/td[1]"),
        "loader": (By.ID, "api-loader")

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def click_create_organization(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Organization_AfterLogin'])
        del page4
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['Organization_AfterLogin'])))
        del wait
        try:
            self.find_element(*self.locator_dictionary['Organization_AfterLogin']).click()
        except:
            self.find_element(*self.locator_dictionary['Organization_AfterLogin']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    # def click_continue(self):
    #     self.find_element(*self.locator_dictionary['continue_button']).click()
    #     time.sleep(2)

    def create_organization(self,Legal_name,dba,tax_id,sic_code,phone,fax,website,business_address_1,business_address_2,business_city,business_zip,mailing_address_1,mailing_address_2,mailing_city,mailing_zip):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Legal_name'])
        del page4
        self.find_element(*self.locator_dictionary['Legal_name']).send_keys(Legal_name)
        self.find_element(*self.locator_dictionary['dba']).send_keys(dba)
        select_corporation_type = self.find_element(*self.locator_dictionary['select_corporation_type'])
        select = Select(select_corporation_type)
        select.select_by_value("LLP")
        self.find_element(*self.locator_dictionary['tax_id']).send_keys(tax_id)
        self.find_element(*self.locator_dictionary['sic_code']).send_keys(sic_code)
        select_payroll_company = self.find_element(*self.locator_dictionary['select_payroll_company'])
        select = Select(select_payroll_company)
        select.select_by_value("ADP")
        self.find_element(*self.locator_dictionary['phone']).send_keys(phone)
        self.find_element(*self.locator_dictionary['fax']).send_keys(fax)
        self.find_element(*self.locator_dictionary['website']).send_keys(website)
        self.find_element(*self.locator_dictionary['business_address_1']).send_keys(business_address_1)
        self.find_element(*self.locator_dictionary['business_address_2']).send_keys(business_address_2)
        self.find_element(*self.locator_dictionary['business_city']).send_keys(business_city)
        select_state = self.find_element(*self.locator_dictionary['select_state'])
        select = Select(select_state)
        select.select_by_value("9")
        self.find_element(*self.locator_dictionary['business_zip']).send_keys(business_zip)
        self.find_element(*self.locator_dictionary['mailing_address_1']).send_keys(mailing_address_1)
        self.find_element(*self.locator_dictionary['mailing_address_2']).send_keys(mailing_address_2)
        self.find_element(*self.locator_dictionary['mailing_city']).send_keys(mailing_city)
        select_city = self.find_element(*self.locator_dictionary['select_city'])
        select = Select(select_city)
        select.select_by_value("5")
        del select
        self.find_element(*self.locator_dictionary['mailing_zip']).send_keys(mailing_zip)
        self.find_element(*self.locator_dictionary['checkbox']).click()
        self.find_element(*self.locator_dictionary['continue_button']).click()


    def verify_create_organization_first_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Organization_AfterLogin'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['Organization_AfterLogin'])
        link_2 = link_1.text
        link_3 = "Create Organization"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_create_organization_second_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Appearance'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['Appearance'])
        link_2 = link_1.text
        link_3 = "Appearance"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    # def image_upload(self):
    #     self.find_element(*self.locator_dictionary['image_logo']).send_keys("//download.jpg")
    #     time.sleep(2)

    def image_upload(self):
        try:
            time.sleep(1)
            self.find_element(*self.locator_dictionary['image_logo']).send_keys(os.getcwd()+"/image.jpg")
            time.sleep(3)
        except:
            print("unable to upload image file")


    def enter_org_disp_name(self,disp_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['org_disp_name'])
        del page4
        self.find_element(*self.locator_dictionary['org_disp_name']).send_keys(disp_name)
        self.find_element(*self.locator_dictionary['continue_button_2']).click()
        time.sleep(1)

    def verify_create_organization_third_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['administration'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['administration'])
        link_2 = link_1.text
        link_3 = "Administration"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def create_organization_third_section(self,ase,ima,cp,ec,producer,direct_id):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['ase'])
        del page4
        # self.find_element(*self.locator_dictionary['ase']).click()
        self.find_element(*self.locator_dictionary['ase']).send_keys(ase)
        try:
            page4 = BasePage(self)
            page4.wait_for_ele_visibility(*self.locator_dictionary['ase_name'])
            del page4
            self.find_element(*self.locator_dictionary['ase_name']).click()
        except:
            time.sleep(5)
            self.find_element(*self.locator_dictionary['ase']).clear()
            self.find_element(*self.locator_dictionary['ase']).send_keys(ase)
            page4 = BasePage(self)
            page4.wait_for_ele_visibility(*self.locator_dictionary['ase_name'])
            del page4
            self.find_element(*self.locator_dictionary['ase_name']).click()


        # self.find_element(*self.locator_dictionary['ase_name']).click()
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['ima'])
        del page4
        self.find_element(*self.locator_dictionary['ima']).send_keys(ima)
        try:
          page4 = BasePage(self)
          page4.wait_for_ele_visibility(*self.locator_dictionary['ima_name'])
          del page4
          self.find_element(*self.locator_dictionary['ima_name']).click()
        except:
            time.sleep(5)
            self.find_element(*self.locator_dictionary['ima']).clear()
            self.find_element(*self.locator_dictionary['ima']).send_keys(ima)
            page4 = BasePage(self)
            page4.wait_for_ele_visibility(*self.locator_dictionary['ima_name'])
            del page4
            self.find_element(*self.locator_dictionary['ima_name']).click()
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['cp'])
        del page4
        self.find_element(*self.locator_dictionary['cp']).send_keys(cp)
        try:
          page4 = BasePage(self)
          page4.wait_for_ele_visibility(*self.locator_dictionary['cp_name'])
          del page4
          self.find_element(*self.locator_dictionary['cp_name']).click()
        except:
          time.sleep(5)
          self.find_element(*self.locator_dictionary['cp']).clear()
          self.find_element(*self.locator_dictionary['cp']).send_keys(cp)
          page4 = BasePage(self)
          page4.wait_for_ele_visibility(*self.locator_dictionary['cp_name'])
          del page4
          self.find_element(*self.locator_dictionary['cp_name']).click()

        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['ec'])
        del page4
        self.find_element(*self.locator_dictionary['ec']).send_keys(ec)
        try:
          page4 = BasePage(self)
          page4.wait_for_ele_visibility(*self.locator_dictionary['ec_name'])
          del page4
          self.find_element(*self.locator_dictionary['ec_name']).click()
        except:
            time.sleep(5)
            self.find_element(*self.locator_dictionary['ec']).clear()
            self.find_element(*self.locator_dictionary['ec']).send_keys(ec)
            page4 = BasePage(self)
            page4.wait_for_ele_visibility(*self.locator_dictionary['ec_name'])
            del page4
            self.find_element(*self.locator_dictionary['ec_name']).click()

        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['producer'])
        del page4
        self.find_element(*self.locator_dictionary['producer']).send_keys(producer)
        try:
          page4 = BasePage(self)
          page4.wait_for_ele_visibility(*self.locator_dictionary['producer_name'])
          del page4
          self.find_element(*self.locator_dictionary['producer_name']).click()
        except:
          time.sleep(5)
          self.find_element(*self.locator_dictionary['producer']).clear()
          self.find_element(*self.locator_dictionary['producer']).send_keys(ec)
          page4 = BasePage(self)
          page4.wait_for_ele_visibility(*self.locator_dictionary['producer_name'])
          del page4
          self.find_element(*self.locator_dictionary['producer_name']).click()
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['direct_id'])
        del page4
        self.find_element(*self.locator_dictionary['direct_id']).send_keys(direct_id)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['select_administration'])
        del page4
        select_admin = self.find_element(*self.locator_dictionary['select_administration'])
        select = Select(select_admin)
        select.select_by_value("true")
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['finish'])
        del page4
        self.find_element(*self.locator_dictionary['finish']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_organization_created(self,link_3 ):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_created_organization'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_created_organization'])
        link_2 = link_1.text
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


