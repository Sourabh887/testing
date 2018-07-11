from behave import *
from pages.login_page import *
from pages.signup_claim_account import *
from pages.create_user_api import *
from pages.create_organization import *
from pages.search_organization import *
from pages.active_deactive_org import *
from pages.group_class_division import *
from steps.group_class_division import *
from pages.create_employee import *
from pages.profile_dropdown import *

orgs = Create_user.getOrgs()
@when("Benemax admin with owner permission create an organzation and activate it")
def step_impl(context):
    page1 = LoginPage(context)
    page1.login()
    page1.verify_afterlogin()
    del page1
    page1 = CreateOrganizationPage(context)
    page1.click_create_organization()
    del page1
    page2 = CreateOrganizationPage(context)
    page2.verify_create_organization_first_modal()
    del page2
    page3 = CreateOrganizationPage(context)
    page3.create_organization("Org1", "Nainsi", "12345", "1234", "1234567890", "1234567890", "http://org.com","7 rue de la ", "rotisseriel", "Paris", "12345", "5 rue de la", "rotisseriel", "Paris","12345")
    time.sleep(1)
    del page3
    page4 = CreateOrganizationPage(context)
    page4.verify_create_organization_second_modal()
    del page4
    page5 = CreateOrganizationPage(context)
    page5.enter_org_disp_name(orgs['org3'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs['org3'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_activate()
    page.search_with_active_filter(orgs['org3'])
    del page
    del page1

@when("Benemax admin with owner permission access same organization and create group class and division for that organization")
def access_org_create_grp_class_division_(context):
     access_group(context)
     verify_create_group(context)
     verify_create_group_modal(context)
     open_create_group(context)
     verify_msg_group(context)
     verify_created_group(context)
     access_edit_group(context)
     verify_edit_group_modal(context)
     edit_group(context)
     verify_success_msg_edit_group(context)
     verify_updatedgroup(context)

    ############################################
     access_division(context)
     verify_create_division(context)
     verify_create_division_modal(context)
     open_create_division(context)
     verify_msg_createddivision(context)
     verify_created_division(context)

    ###################################################
     access_class(context)
     verify_create_class(context)
     verify_create_class_modal(context)
     open_create_class(context)
     verify_msg_createdclass(context)
     verify_created_class(context)


@then("Verify Create an Employee option should be visible if admin access employee tab")
def verify_create_employee(context):
    page = Create_employeePage(context)
    page.access_employee_tab()
    page.verify_create_employee_btn()
    del page

@when("Benemax admin access create an employee option")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an employee")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin create an employee")
def create_employee(context):
    page = Create_employeePage(context)
    page.create_employee("G2","D1","C1")
    del page

@when("i search for same employee and select pending filter")
def search_employee_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_employee("nainsi1")
    del page

@then("Veirfy employee should be displayed in table view and status should be Pending")
def verify_employee_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_employee()
    del page3
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@then("that created employee completed claim account process")
def created_employee_complete_claim_account(context):
    page = Create_user(context)
    page.create_employee(context)
    del page
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@then("Employee access switch role and verify Employee role should be visible")
def verify_employee_role(context):
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    page4.verify_employee_role()
    page4.close_dropdown()
    del page4

@when("Employee signout from existing account and Benemax admin with owner permission again login")
def employee_signout_benemax_admin_login(context) :
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['benemaxadmin_email'],"12345678")
    del page

@then("Benemax admin with owner permission again access same active organization for Employee")
def admin_access_org(context):
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs['org3'])
    del page
    page1 = Group_class_divisionPage(context)
    page1.click_org()
    del page1

@then("Verify Employee status should be show as Active")
def verify_employee_active(context):
    page4 = Create_employeePage(context)
    page4.verify_active_state_created_employee("Nainsi2")
    page4.verify_active_state_employee()
    del page4

#############################################################################################################################

@when("Benemax admin access create an employee option to create organization admin")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an organization admin")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin with owner permission again create Organization admin for same active organization")
def create_org_admin(context):
    page = Create_employeePage(context)
    page.create_org_admin()
    del page


@when("i search for same organization admin and select pending filter")
def search_orgadmin_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_orgadmin("nainsi3")
    del page

@then("Veirfy organization admin should be displayed in table view and status should be Pending")
def verify_orgadmin_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_orgadmin()
    del page3
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@then("that created organization admin completed claim account process")
def created_orgadmin_complete_claim_account(context):
    page = Create_user(context)
    page.create_org_admin_with_edit_permission1(context)
    del page
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@then("Organization admin access switch role and verify Organization admin role should be visible")
def verify_employee_role(context):
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    page4.verify_orgadmin_role()
    page4.close_dropdown()
    del page4

@when("Organization admin signout from existing account and Benemax admin with owner permission again login")
def orgadmin_signout_benemax_admin_login(context) :
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['benemaxadmin_email'],"12345678")
    del page

@then("Benemax admin with owner permission again access same active organization for Organization admin")
def admin_access_org(context):
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs['org3'])
    del page
    page = Group_class_divisionPage(context)
    page.click_org()
    del page

@then("Verify Organization admin status should be show as Active")
def verify_employee_active(context):
    page4 = Create_employeePage(context)
    page4.verify_active_state_created_org_admin("Nainsi4")
    page4.verify_active_state_employee()
    del page4

##########################################################################################################

@when("Benemax admin access create an employee option to create organization admin and Employee")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an employee and organization admin")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin with owner permission again create Organization admin and Employee for same active organization")
def create_org_admin_employee(context):
    page = Create_employeePage(context)
    page.create_org_admin_employee("G2","D1","C1")
    del page

@when("i search for same organization admin and employee and select pending filter")
def search_orgadmin_employee_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_orgadmin_employee("nainsi5")
    del page

@then("Veirfy organization admin and admin should be displayed in table view and status should be Pending")
def verify_orgadmin_employee_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_orgadmin_employee()
    del page3
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@then("that created organization admin and Employee completed claim account process")
def created_orgadmin_employee_complete_claim_account(context):
    page = Create_user(context)
    page.create_orgadmin_and_employee(context)
    del page
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@then("Organization admin and Employee access switch role and verify Organization admin and employee both role should be visible")
def verify_employee_orgadmin_role(context):
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    page4.verify_employee_orgadmin_role()
    page4.close_dropdown()
    del page4

@when("Organization admin and Employee signout from existing account and Benemax admin with owner permission again login")
def orgadmin_signout_benemax_admin_login(context) :
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['benemaxadmin_email'],"12345678")
    del page

@then("Benemax admin with owner permission again access same active organization for organization admin and Employee")
def admin_access_org(context):
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs['org3'])
    del page
    page = Group_class_divisionPage(context)
    page.click_org()
    del page

@then("Verify Organization admin and Employee status should be show as Active")
def verify_employee_active(context):
    page4 = Create_employeePage(context)
    page4.verify_active_state_created_org_admin_employee("Nainsi6")
    page4.verify_active_state_orgadmin_employee()
    del page4

############################################################################################################


@when("Benemax admin with owner permission Edit that Employee and give up his permission from Organization admin and make him only as Employee")
def edit_employee(context):
    page = Create_employeePage(context)
    page.edit_employee_remove_org_admin_make_employee("G2","D1","C1")
    del page
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@when("Benemax admin with owner permission logout and edited employee Login and verify his role in switch role")
def edited_employee_login(context):
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['EditEmployeeEmail'],"12345678")
    del page
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    page4.verify_employee_role()
    page4.close_dropdown()
    del page4
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@when("Benemax admin with owner permission deactivate that Edited Employee")
def deactivate_employee(context):
    page1 = LoginPage(context)
    page1.login()
    page1.verify_afterlogin()
    del page1
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs['org3'])
    del page
    page = Group_class_divisionPage(context)
    page.click_org()
    del page
    page = Create_employeePage(context)
    page.search_employee_deactivate_him("Nainsi4")
    del page


@then("Verify employee should show in deactivate state")
def verify_deactivate_employee(context):
    page4 = Create_employeePage(context)
    page4.verify_deactive_state_edited__employee("Nainsi4")
    page4.verify_deactive_state_employee()
    del page4

@when("Benemax admin with owner permission Create new Organization and activate it and signout from existing account")
def create_new_org(context):
    page = Create_employeePage(context)
    page.click_back_to_admin()
    page1 = CreateOrganizationPage(context)
    page1.click_create_organization()
    del page1
    page2 = CreateOrganizationPage(context)
    page2.verify_create_organization_first_modal()
    del page2
    page3 = CreateOrganizationPage(context)
    page3.create_organization("Org1", "Nainsi", "12345", "1234", "1234567890", "1234567890", "http://org.com","7 rue de la ", "rotisseriel", "Paris", "12345", "5 rue de la", "rotisseriel", "Paris","12345")
    time.sleep(1)
    del page3
    page4 = CreateOrganizationPage(context)
    page4.verify_create_organization_second_modal()
    del page4
    page5 = CreateOrganizationPage(context)
    page5.enter_org_disp_name(orgs['org4'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs['org4'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_activate()
    page.search_with_active_filter(orgs['org4'])
    del page
    del page1
    access_org_create_grp_class_division_(context)
    verify_create_employee(context)
    access_create_employee(context)


@when("Benemax admin with owner permission create same Employee to Organization admin and Employee for an active organization")
def create_second_orgadmin_employee(context):
    page = Create_employeePage(context)
    page.create_employee_org_admin("G2","D1","C1")
    del page
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@when("Created employee and Organization admin switch role and verify Organization name in header")
def verify_employee_role_for_first_organization(context):
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['EditEmployeeEmail'], "12345678")
    del page
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    page4.verify_employee_orgadmin_role()
    page4.click_employee_org_admin()
    page4.verify_organization_in_header(orgs['org4'])
    del page4
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@when("Benemax admin with owner permission again Login and activate employee for previous organization and verify his status as active")
def activate_employee_deactivate_organization(context):
    page1 = LoginPage(context)
    page1.login()
    page1.verify_afterlogin()
    del page1
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs['org3'])
    del page
    page = Group_class_divisionPage(context)
    page.click_org()
    del page
    page = Create_employeePage(context)
    page.search_employee_activate_him("Nainsi4")
    del page
    page4 = Create_employeePage(context)
    page4.verify_active_state_created_employee1("Nainsi4")
    page4.verify_active_state_employee()
    del page4

@when("Benemax admin with owner permission go back and deactivate second organization in which user is associated")
def deactivate_second_organization(context):
    page = Create_employeePage(context)
    page.click_back_to_admin()
    del page
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs['org4'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_deactivate()
    del page
    del page1
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@then("Edited Employee Login and access switch role,Verify only Employee role should be visible and in header correct organization should be visible")
def employee_again_login_access_switchrole(context):
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['EditEmployeeEmail'], "12345678")
    del page
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    page4.verify_employee_role()
    page4.click_employee()
    page4.verify_organization_in_header(orgs['org3'])
    del page4
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@when("Benemax admin with owner permission deactivate previous organization")
def deactive_org(context):
    page1 = LoginPage(context)
    page1.login()
    page1.verify_afterlogin()
    del page1
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs['org3'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_deactivate()
    del page
    del page1
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@when("Employee try to Login for the condition in which both the organizations are deactivated")
def employee_login_deactivate_organization(context):
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['EditEmployeeEmail'], "12345678")
    del page

@then("verify error message should be displayed and employee should not be able to Login")
def verify_employee_unable_to_login(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("This account is not assigned to any active organizations")
    del page