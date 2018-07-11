from behave import *
from pages.forgot_reset_password import *
from pages.create_user_api import *
from pages.signup_claim_account import *
from pages.login_page import *


@when("I Create an user and complete claim account process")
def create_user(context) :
    page = Create_user(context)
    page.create_user_gettoken()
    del page
    page1 = ClaimAccountPage(context)
    page1.claim_account_invitation_link("12345678","12345678")
    del page1
    

@then("I access Login and want to access forgot Password link")
def access_forgot_password(context) :
   page = ClaimAccountPage(context)
   page.click_signuot()

@when("I enter registered email to get reset password link on provided email")
def step_impl(context):
    page = FogotPasswordPage(context)
    page.access_forgotpassword(dict1["api_email"])
    del page


@then("Success message should be displayed and link is sent on provided email")
def verify(context):
    page1 = FogotPasswordPage(context)
    page1.verify_forgot_success_msg()
    del page1

@when("User access reset Password link sent on his email")
def access_forgot_link(context) :
    page = Create_user(context)
    page.login_with_created_user_get_token()
    del page

@then("User should be able to reset his Password")
def reset_password(context):
    page1 = FogotPasswordPage(context)
    page1.access_reset_password("123456789","123456789")
    del page1
    

@then("Verify success message should be displayed")
def verify(context):
    page2 = FogotPasswordPage(context)
    page2.verify_reset_success_msg()
    del page2

@when("User want to Login with old Password")
def login_with_old_pwd(context) :
    time.sleep(1)
    page2 =LoginPage(context)
    page2.dynamic_login_with_click_loginink(dict1["api_email"],dict1["password"])
    del page2

@then("Verify error message should be displayed and User is not able to Login")
def verify_error_message(context) :
    page = ClaimAccountPage(context)
    page.verify_error_msg("No account associated with this email or password")
    del page

@when("User want to Login with newly updated password")
def login_with_new_password(context):
    page2 = LoginPage(context)
    page2.dynamic_login_without_click_loginink(dict1["api_email"], "123456789")
    del page2

@then("Verify User should be able to Login and redirected on dashboard")
def verify_user_after_login(context) :
    page3 = LoginPage(context)
    page3.verify_afterlogin()
