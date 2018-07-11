from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FogotPasswordPage(BasePage):
    locator_dictionary = {
        "ForgotPassword": (By.XPATH, "//*[text()='Forgot Password?']"),
        "Email": (By.XPATH, "//input[@name='email']"),
        "Send Link": (By.XPATH, "//button[@type='submit']"),
        "Login": (By.XPATH, "//a[text()='Login']"),
        "New_Password": (By.ID, "Password"),
        "Confirm_Password" : (By.ID, "Confirm Password"),
        "Reset_Password_btn": (By.XPATH, "//button[@type='submit']"),
        "loader": (By.ID, "api-loader"),
        "message":(By.ID, "toasty")
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def access_forgotpassword(self,email):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['Login'])
        del page4
        self.find_element(*self.locator_dictionary['Login']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ForgotPassword']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['Email']).send_keys(email)
        self.find_element(*self.locator_dictionary['Send Link']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_forgot_success_msg(self):
        wait = WebDriverWait(self.browser, 10)
        link_1 =  wait.until(EC.visibility_of_element_located((self.locator_dictionary['message'])))
        link_2 = str(link_1.text).strip()
        link_3 = "We have sent you reset password link, please use that link and reset your password"
        assert link_2 == link_3, "Visible forgot Password text message is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def access_reset_password(self,new_pwd,confirm_pwd):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['New_Password'])
        del page4
        self.find_element(*self.locator_dictionary['New_Password']).send_keys(new_pwd)
        self.find_element(*self.locator_dictionary['Confirm_Password']).send_keys(confirm_pwd)
        self.find_element(*self.locator_dictionary['Reset_Password_btn']).click()


    def verify_reset_success_msg(self):
        time.sleep(2)
        wait = WebDriverWait(self.browser, 10)
        link_1 =  wait.until(EC.visibility_of_element_located((self.locator_dictionary['message'])))
        link_2 = str(link_1.text).strip()
        link_3 = "Your password is reset successfully"
        assert link_2 == link_3, "Visible Reset Password text message is not as expected" \
                                                   " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3
