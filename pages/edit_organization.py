from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class EditOrganizationPage(BasePage):
    locator_dictionary = {
        "Open_EditOrganization": (By.CLASS_NAME, "ellipse"),
        "Edit_Organization": (By.XPATH,"//table//tr[2]/td[8]//ul/li[1]/a"),
        "View_Organization":(By.XPATH,"//table//tr[2]/td[8]//ul/li[1]/a"),
        "verify_org_tab": (By.XPATH,"//h4[text()='Organization Details']"),
        "Legal_name": (By.XPATH, "//input[@name='legal_name']"),
        "dba": (By.XPATH, "//input[@name='dba']"),
        "select_corporation_type": (By.XPATH, "//form/tabset//div[3]/select"),
        "tax_id": (By.XPATH, "//input[@name='tax_id']"),
        "sic_code": (By.XPATH, "//input[@name='sic_code']"),
        "select_payroll_company": (By.XPATH, "//form/tabset//div[6]/select"),
        "phone": (By.XPATH, "//input[@name='phone']"),
        "fax": (By.XPATH, "//input[@name='fax']"),
        "website": (By.XPATH, "//input[@name='website']"),
        "business_address_1": (By.XPATH, "//input[@name='business_address_1']"),
        "business_address_2": (By.XPATH, "//input[@name='business_address_2']"),
        "business_city": (By.XPATH, "//input[@name='business_city']"),
        "select__business_state": (By.NAME, "business_state"),
        "business_zip": (By.XPATH, "//input[@name='business_zip']"),
        "mailing_address_1": (By.XPATH, "//input[@name='mailing_address_1']"),
        "mailing_address_2": (By.XPATH, "//input[@name='mailing_address_2']"),
        "mailing_city": (By.XPATH, "//input[@name='mailing_city']"),
        "select_mailing_state": (By.NAME, "mailing_state"),
        "mailing_zip": (By.XPATH, "//input[@name='mailing_zip']"),
        "checkbox": (By.XPATH, "//label[@class='css-label']"),
        "Appearance": (By.XPATH, "//span[text()='Appearance']"),
        "org_disp_name": (By.XPATH, "//input[@name='display_name']"),
        "administration": (By.XPATH, "//span[text()='Administration']"),
        "ase": (By.XPATH, "//input[@name='ASE']"),
        "ase_name": (By.XPATH, "//form//button[1]/p"),
        "ima": (By.XPATH, "//input[@name='IMA']"),
        "ima_name": (By.XPATH, "//form//button[1]/p"),
        "cp": (By.XPATH, "//input[@name='CP']"),
        "cp_name": (By.XPATH, "//form//button[1]/p"),
        "ec": (By.XPATH, "//input[@name='EC']"),
        "ec_name": (By.XPATH, "//form//button[1]/p"),
        "producer": (By.XPATH, "//input[@name='Producer']"),
        "producer_name": (By.XPATH, "//form//button[1]/p"),
        "direct_id": (By.XPATH, "//input[@name='direct_id']"),
        "select_administration": (By.NAME, "cobra"),
        "save_changes": (By.XPATH, "//button[text()='Save Changes']"),
        "close_modal": (By.XPATH, "//a[@class='close-modal']"),
        "verify_edited_organization":(By.XPATH, "//table//tr[2]/td[1]"),
        "click_close_modal":(By.XPATH,"//a[@class='close-modal']"),
        "popup": (By.XPATH, "//div[@class='close-button']"),
        "loader": (By.ID, "api-loader"),
        "message": (By.ID, "toasty")

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def click_edit_organization(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Open_EditOrganization'])
        del page4
        self.find_element(*self.locator_dictionary['Open_EditOrganization']).click()
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Edit_Organization'])
        del page4
        self.find_element(*self.locator_dictionary['Edit_Organization']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 20)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_view_organization(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['View_Organization'])
        del page4
        self.find_element(*self.locator_dictionary['View_Organization']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 20)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def close_view_org_modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['click_close_modal'])
        del page4
        self.find_element(*self.locator_dictionary['click_close_modal']).click()
        time.sleep(1)

    def verify_view_organization(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Open_EditOrganization'])
        del page4
        self.find_element(*self.locator_dictionary['Open_EditOrganization']).click()
        time.sleep(1)
        link_1 = self.find_element(*self.locator_dictionary['View_Organization'])
        link_2 = link_1.text
        link_3 = "View Organization"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_edit_org_Modal(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_org_tab'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_org_tab'])
        link_2 = link_1.text
        link_3 = "Organization Details"
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3



    def click_save_changes(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['save_changes'])
        del page4
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def edit_organization(self,Legal_name,dba,tax_id,sic_code,phone,fax,website,business_address_1,business_address_2,business_city,business_zip,mailing_address_1,mailing_address_2,mailing_city,mailing_zip):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Legal_name'])
        del page4
        self.find_element(*self.locator_dictionary['Legal_name']).clear()
        self.find_element(*self.locator_dictionary['Legal_name']).send_keys(Legal_name)
        self.find_element(*self.locator_dictionary['dba']).clear()
        self.find_element(*self.locator_dictionary['dba']).send_keys(dba)
        select_corporation_type = self.find_element(*self.locator_dictionary['select_corporation_type'])
        select = Select(select_corporation_type)
        select.select_by_value("LLC")
        self.find_element(*self.locator_dictionary['tax_id']).clear()
        self.find_element(*self.locator_dictionary['tax_id']).send_keys(tax_id)
        self.find_element(*self.locator_dictionary['sic_code']).clear()
        self.find_element(*self.locator_dictionary['sic_code']).send_keys(sic_code)
        select_payroll_company = self.find_element(*self.locator_dictionary['select_payroll_company'])
        select = Select(select_payroll_company)
        select.select_by_value("Paychex")
        self.find_element(*self.locator_dictionary['phone']).clear()
        self.find_element(*self.locator_dictionary['phone']).send_keys(phone)
        self.find_element(*self.locator_dictionary['fax']).clear()
        self.find_element(*self.locator_dictionary['fax']).send_keys(fax)
        self.find_element(*self.locator_dictionary['website']).clear()
        self.find_element(*self.locator_dictionary['website']).send_keys(website)
        self.find_element(*self.locator_dictionary['business_address_1']).clear()
        self.find_element(*self.locator_dictionary['business_address_1']).send_keys(business_address_1)
        self.find_element(*self.locator_dictionary['business_address_2']).clear()
        self.find_element(*self.locator_dictionary['business_address_2']).send_keys(business_address_2)
        self.find_element(*self.locator_dictionary['business_city']).clear()
        self.find_element(*self.locator_dictionary['business_city']).send_keys(business_city)
        select_state = self.find_element(*self.locator_dictionary['select__business_state'])
        select = Select(select_state)
        select.select_by_value("9")
        self.find_element(*self.locator_dictionary['business_zip']).clear()
        self.find_element(*self.locator_dictionary['business_zip']).send_keys(business_zip)
        self.find_element(*self.locator_dictionary['checkbox']).click()
        self.find_element(*self.locator_dictionary['mailing_address_1']).clear()
        self.find_element(*self.locator_dictionary['mailing_address_1']).send_keys(mailing_address_1)
        self.find_element(*self.locator_dictionary['mailing_address_2']).clear()
        self.find_element(*self.locator_dictionary['mailing_address_2']).send_keys(mailing_address_2)
        self.find_element(*self.locator_dictionary['mailing_city']).clear()
        self.find_element(*self.locator_dictionary['mailing_city']).send_keys(mailing_city)
        select_state = self.find_element(*self.locator_dictionary['select_mailing_state'])
        select = Select(select_state)
        select.select_by_value("5")
        self.find_element(*self.locator_dictionary['mailing_zip']).clear()
        self.find_element(*self.locator_dictionary['mailing_zip']).send_keys(mailing_zip)
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['Appearance']).click()
        del select



    def enter_org_disp_name_go_third_section(self,disp_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['org_disp_name'])
        del page4
        self.find_element(*self.locator_dictionary['org_disp_name']).clear()
        self.find_element(*self.locator_dictionary['org_disp_name']).send_keys(disp_name)
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['administration']).click()


    def edit_organization_third_section(self,ase,ima,cp,ec,producer,direct_id):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['ase'])
        del page4
        # self.find_element(*self.locator_dictionary['ase']).click()
        self.find_element(*self.locator_dictionary['ase']).clear()
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
        self.find_element(*self.locator_dictionary['ima']).clear()
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
        self.find_element(*self.locator_dictionary['cp']).clear()
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
        self.find_element(*self.locator_dictionary['ec']).clear()
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
        self.find_element(*self.locator_dictionary['producer']).clear()
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
        time.sleep(1)
        self.find_element(*self.locator_dictionary['save_changes']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        try:
            wait = WebDriverWait(self.browser, 15)
            wait.until(EC.visibility_of_element_located((self.locator_dictionary['message'])))
            del wait
            a = self.find_element(*self.locator_dictionary["popup"])
            if a.is_displayed() and a.is_enabled():
                a.click()
        except:
            print("pop up is not visible")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['close_modal']).click()



    def verify_organization_edited(self,link_3 ):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_edited_organization'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_edited_organization'])
        link_2 = link_1.text
        assert link_2 == link_3, "Visible Text is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3