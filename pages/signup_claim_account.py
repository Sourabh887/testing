from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ClaimAccountPage(BasePage):
    locator_dictionary = {
        "First_name": (By.XPATH,"//input[@name='first_name']"),
        "Last_name": (By.XPATH, "//input[@name='last_name']"),
        "email": (By.XPATH, "//input[@name='email']"),
        "password": (By.XPATH, "//input[@name='password']"),
        "Confirm_Password":(By.XPATH, "//input[@name='confirm_password']"),
        "claim_Account": (By.XPATH, "//button[@type='submit']"),
        "sign_out_dropdown": (By.XPATH, "//button[@type='button']"),
        "sign_out": (By.XPATH, "//a[text()='Sign Out']"),
        "message":(By.ID, "toasty"),
        "loader": (By.ID, "api-loader"),
        "popup":(By.XPATH, "//div[@class='close-button']")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def visit_signup(self,url):
        self.browser.get(url)
        time.sleep(5)

    def signup(self,fname,lname,email,pwd,confirmPwd):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['First_name'])
        del page4
        self.find_element(*self.locator_dictionary['First_name']).send_keys(fname)
        self.find_element(*self.locator_dictionary['Last_name']).send_keys(lname)
        self.find_element(*self.locator_dictionary['email']).send_keys(email)
        self.find_element(*self.locator_dictionary['password']).send_keys(pwd)
        self.find_element(*self.locator_dictionary['Confirm_Password']).send_keys(confirmPwd)
        self.find_element(*self.locator_dictionary['claim_Account']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_success_msg(self,link_3):
        wait = WebDriverWait(self.browser, 10)
        link_1 = wait.until(EC.visibility_of_element_located((self.locator_dictionary['message'])))
        link_2 = str(link_1.text).strip()
        assert link_2 == link_3, "Visible Text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_error_msg(self,link_3):
        wait = WebDriverWait(self.browser, 10)
        link_1 = wait.until(EC.visibility_of_element_located((self.locator_dictionary['message'])))
        link_2 = str(link_1.text).strip()
        assert link_2 == link_3, "Visible Text is not as expected." \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3



    def claim_account_invitation_link(self,pwd,confirmPwd):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['password'])
        del page4
        self.find_element(*self.locator_dictionary['password']).send_keys(pwd)
        self.find_element(*self.locator_dictionary['Confirm_Password']).send_keys(confirmPwd)
        self.find_element(*self.locator_dictionary['claim_Account']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def click_signuot(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        try:
            # wait = WebDriverWait(self.browser, 15)
            # wait.until(EC.visibility_of_element_located((self.locator_dictionary['message'])))
            # del wait
            # a = self.find_element(*self.locator_dictionary["popup"])
            # if a.is_displayed() and a.is_enabled():
            #     a.click()
            time.sleep(1)
            wait = WebDriverWait(self.browser, 15)
            a = wait.until(EC.visibility_of_element_located((self.locator_dictionary['popup'])))
            a.click()
            del wait,a
            time.sleep(1)
        except:
            print("pop up is not visible")
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['sign_out_dropdown'])
        del page4
        time.sleep(1)
        self.find_element(*self.locator_dictionary['sign_out_dropdown']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['sign_out'])))
        del wait
        self.find_element(*self.locator_dictionary['sign_out']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def close_popup(self):
        try:
            # wait = WebDriverWait(self.browser, 15)
            # wait.until(EC.visibility_of_element_located((self.locator_dictionary['message'])))
            # del wait
            # a = self.find_element(*self.locator_dictionary["popup"])
            # if a.is_displayed() and a.is_enabled():
            #     a.click()
            wait = WebDriverWait(self.browser, 15)
            a = wait.until(EC.visibility_of_element_located((self.locator_dictionary['popup'])))
            del wait
            a.click()
            time.sleep(1)
        except:
            print("pop up is not visible")







