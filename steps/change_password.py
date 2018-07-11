from behave import *
from pages.login_page import *
from pages.create_user_api import *
from pages.profile_dropdown import *
from pages.signup_claim_account import *
from pages.change_password import *

@when("I create Benemax admin with owner permission and he completes claim account process to change password")
def step_impl(context):
    page = Create_user(context)
    page.create_benemax_admin_owner_permission1(context)
    del page
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@when("User access Change Password option")
def step_impl(context):
    page = Profile_dropdown_page(context)
    page.close_dropdown()
    del page
    page = Change_Password_Page(context)
    page.click_change_password()
    del page

@when("User enter valid data in all fields and update his Password")
def step_impl(context):
    page1 = Change_Password_Page(context)
    page1.change_password_admin()
    del page1

@then("Verify success message should be displayed to User when password updated successfully")
def verify(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Password changed successfully.")
    del page

@when("User wants to Login with old Password")
def login(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['BenemaxAdminEmail1'],"12345678")
    del page

@then("Verify error message should be displayed to User when he wants to Login with Old Password")
def verify_error_message(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("No account associated with this email or password")
    del page

@when("User wants to Login with newly updated Password")
def login_with_new_email(context):
    page = LoginPage(context)
    page.dynamic_login_without_click_loginink(orgs['BenemaxAdminEmail1'],"123456789")
    del page


@then("Verify User should be redirected on Admin dashboard")
def verify_dashboard(context):
    page = LoginPage(context)
    page.verify_afterlogin()
    del page
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

