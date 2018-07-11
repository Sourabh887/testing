from behave import *
from pages.login_page import *
from pages.create_user_api import *
from pages.profile_dropdown import *
from pages.account_details import *
from pages.signup_claim_account import *
from pages.create_organization import *
from pages.search_organization import *
from pages.active_deactive_org import *
from steps.create_employee import *

@when("I create new Benemax admin and he completes claim account process")
def step_impl(context):
    page = Create_user(context)
    page.create_benemax_admin_editpermission_gettoken1(context)
    del page
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@when("Benemax admin access account details option from dropdown")
def access_account_details(context):
    page = Profile_dropdown_page(context)
    page.close_dropdown()
    del page
    page = AccountdetailsPage(context)
    page.click_account_details()
    del page

@then("verify correct modal should be open to Benemax admin")
def verify(context):
    page1 = AccountdetailsPage(context)
    page1.verify_account_details_modal()
    del page1

@when("Benemax admin enter valid details in all fields and change his email and update his details")
def update_account_details(context):
    page = AccountdetailsPage(context)
    page.change_account_details_admin()
    del page
    page = ClaimAccountPage(context)
    page.verify_success_msg("Account details updated successfully.")
    del page

@then("verify Username should be updated on header for benemax admin")
def verify(context):
    page = AccountdetailsPage(context)
    page.verify_name_header()
    del page

@when("Benemax admin signout from existing account and wants to Login with old email")
def login(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['AdminEmail'],"12345678")
    del page

@then("verify error message should be displayed for Benemax admin")
def verify_error_message(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("No account associated with this email or password")
    del page

@when("Benemax admin wants to Login with newly updated Email")
def again_login(context):
    page = LoginPage(context)
    page.dynamic_login_without_click_loginink(orgs['EditEmployeeEmail1'],"12345678")
    del page

@then("veriy Benemax admin should be able to Login with newly updated Email")
def verify(context):
    page = LoginPage(context)
    page.verify_org_text_afterlogin()
    del page

#########################################################################################################

@when("I create new Organization admin and he completes claim account process")
def step_impl(context):
    page1 = CreateOrganizationPage(context)
    page1.click_create_organization()
    del page1
    page2 = CreateOrganizationPage(context)
    page2.verify_create_organization_first_modal()
    del page2
    page3 = CreateOrganizationPage(context)
    page3.create_organization("Org1", "Nainsi", "12345", "1234", "1234567890", "1234567890", "http://org.com",
                              "7 rue de la ", "rotisseriel", "Paris", "12345", "5 rue de la", "rotisseriel", "Paris",
                              "12345")
    time.sleep(3)
    del page3
    page4 = CreateOrganizationPage(context)
    page4.verify_create_organization_second_modal()
    del page4
    page5 = CreateOrganizationPage(context)
    page5.enter_org_disp_name(orgs['org5'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs['org5'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_activate()
    page.search_with_active_filter(orgs['org5'])
    del page
    del page1
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page = Create_user(context)
    page.create_org_admin_with_edit_permission2(context)
    del page
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@when("Organization admin access account details option from dropdown")
def access_account_details(context):
    page = Profile_dropdown_page(context)
    page.close_dropdown()
    del page
    page = AccountdetailsPage(context)
    page.click_account_details()
    del page

@then("verify correct modal should be open to Organization admin")
def verify(context):
    page1 = AccountdetailsPage(context)
    page1.verify_account_details_modal()
    del page1

@when("Organization admin enter valid details in all fields and change his email and update his details")
def update_account_details(context):
    page = AccountdetailsPage(context)
    page.change_account_details_org_admin()
    del page

@then("verify Username should be updated on header for Organization admin")
def verify(context):
    page = AccountdetailsPage(context)
    page.verify_name_header()
    del page

@when("Organization admin signout from existing account and wants to Login with old email")
def login(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['OrgAdminEmail'],"12345678")
    del page

@then("verify error message should be displayed for Organization admin")
def verify_error_message(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("No account associated with this email or password")
    del page

@when("Organization admin wants to Login with newly updated Email")
def again_login(context):
    page = LoginPage(context)
    page.dynamic_login_without_click_loginink(orgs['OrgAdminEmail1'],"12345678")
    del page

@then("veriy Organization admin should be able to Login with newly updated Email")
def verify(context):
    page = Profile_dropdown_page(context)
    page.open_switch_role()
    page.verify_orgadmin_role()
    page.close_dropdown()
    del page
    page = ClaimAccountPage(context)
    page.click_signuot()
    page = LoginPage(context)
    page.login()
    del page

#############################################################################################################

@when("I create new Employee and he completes claim account process")
def step_impl(context):
    page1 = CreateOrganizationPage(context)
    page1.click_create_organization()
    del page1
    page2 = CreateOrganizationPage(context)
    page2.verify_create_organization_first_modal()
    del page2
    page3 = CreateOrganizationPage(context)
    page3.create_organization("Org1", "Nainsi", "12345", "1234", "1234567890", "1234567890", "http://org.com",
                              "7 rue de la ", "rotisseriel", "Paris", "12345", "5 rue de la", "rotisseriel", "Paris",
                              "12345")
    time.sleep(1)
    del page3
    page4 = CreateOrganizationPage(context)
    page4.verify_create_organization_second_modal()
    del page4
    page5 = CreateOrganizationPage(context)
    page5.enter_org_disp_name(orgs['org6'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs['org6'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_activate()
    page.search_with_active_filter(orgs['org6'])
    del page
    del page1
    access_org_create_grp_class_division_(context)
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page = Create_user(context)
    page.create_employee1(context)
    del page
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@when("Employee access account details option from dropdown")
def access_account_details(context):
    page = Profile_dropdown_page(context)
    page.close_dropdown()
    del page
    page = AccountdetailsPage(context)
    page.click_account_details()
    del page

@then("verify correct modal should be open to Employee")
def verify(context):
    page1 = AccountdetailsPage(context)
    page1.verify_account_details_modal()
    del page1

@when("Employee enter valid details in all fields and change his email and update his details")
def update_account_details(context):
    page = AccountdetailsPage(context)
    page.change_account_details_employee()
    del page

@then("verify Username should be updated on header for Employee")
def verify(context):
    page = AccountdetailsPage(context)
    page.verify_name_header()
    del page

@when("Employee signout from existing account and wants to Login with old email")
def login(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['EmployeeEmail'],"12345678")
    del page

@then("verify error message should be displayed for Employee")
def verify_error_message(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("No account associated with this email or password")
    del page

@when("Employee wants to Login with newly updated Email")
def again_login(context):
    page = LoginPage(context)
    page.dynamic_login_without_click_loginink(orgs['EmployeeEmail1'],"12345678")
    del page

@then("veriy Employee should be able to Login with newly updated Email")
def verify(context):
    page = Profile_dropdown_page(context)
    page.open_switch_role()
    page.verify_employee_role()
    page.close_dropdown()
    del page
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
