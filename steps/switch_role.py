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
from pages.create_admin import *
from pages.edit_admin import *
from pages.edit_organization import *
from environment import email_before_gmail_domain


orgs = Create_user.getOrgs()
first_name = str(calendar.timegm(time.gmtime())) + "Nainsi"
@when("I create Benemax admin with owner permission and he completes claim account process")
def create_admin_owner_permission(context):
    page = Create_user(context)
    page.create_benemax_admin_owner_permission(context)
    del page
    page = ClaimAccountPage(context)
    page.claim_account_invitation_link("12345678","12345678")
    del page

@when("Benemax admin with owner permission create new Benemax admin")
def create_new_benemax_admin(context):
    page = CreateAdminPage(context)
    page.click_create_administrator()
    del page
    page2 = CreateAdminPage(context)
    page2.verify_admin_modal()
    del page2
    global first_name
    showtime = calendar.timegm(time.gmtime())
    page3 = CreateAdminPage(context)
    email = email_before_gmail_domain+"+"+"32"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
    page3.create_admin_owner(first_name, "Jain", email)
    del page3


@then("Verify only Edit admin option should be displayed for pending state Benemax admin")
def verify_create_employee(context):
    page4 = SearchAdminPage(context)
    page4.search_with_pending_filter(first_name)
    page4.verify_searched_admin(first_name)
    del page4
    page = EditAdminPage(context)
    page.verify_edit_administrator()
    del page

@when("Benemax admin edit that pending state Benemax admin and change his name")
def access_create_employee(context):
    page = EditAdminPage(context)
    page.edit_admin_owner_pending("Nainsi$","Jain$")
    del page

@then("Verify name should be updated in table view")
def verify_employee_modal(context):
    page4 = SearchAdminPage(context)
    page4.search_with_pending_filter("Nainsi$")
    page4.verify_searched_admin("Nainsi$")
    del page4

@when("Benemax admin search himself and change his permission from owner to edit")
def admin_search_change_permission(context):
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(orgs['AdminFname'])
    del page4
    page = EditAdminPage(context)
    page.click_edit_administrator()
    page.edit_admin_edit_permission()
    del page

@then("Verify only Organization view should be displayed to Benemax admin")
def create_employee(context):
    page4 = LoginPage(context)
    page4.verify_org_text_afterlogin()
    del page4

@when("Benemax admin with Edit permission create new Organization and activate it")
def create_org(context):
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
    page5.enter_org_disp_name(orgs['org7'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs['org7'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_activate()
    page.search_with_active_filter(orgs['org7'])
    del page
    del page1

@when("Benemax admin make himslef Employee and Organization admin with Edit permission")
def admin_make_himself_orgadmin_employee(context):
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

    page = Create_employeePage(context)
    page.access_employee_tab()
    page.click_create_employee()
    page.create_employee_org_admin_himself("G2","D1","C1",orgs['AdminFname1'])
    del page

@then("Verify admin should show as in active state in table view")
def verify_admin_active_state(context):
    page4 = Create_employeePage(context)
    page4.verify_active_state_created_employee2(orgs['AdminFname1'],orgs['AdminFname1'])
    page4.verify_active_state_employee()
    del page4

@when("Benemax admin with Edit permission access switch role as Organization admin")
def switch_role_org_admin(context):
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    page4.click_orgadmin()
    del page4

@when("Organization admin Create new Organization admin and Employee for his Organization")
def create_org_admin_employee(context):
    page = Create_employeePage(context)
    page.click_people_org_admin()
    page.click_create_employee()
    page.create_employee_org_admin_pending("G2","D1","C1")
    del page

@then("Verify User should be displayed in pending state")
def verify_user_pending(context):
    page = Create_employeePage(context)
    page.verify_pending_state_created_employee1("Nainsi#")
    del page
    page3 = Create_employeePage(context)
    page3.verify_pending_state_employee()
    del page3

@when("Organization admin Edit him and change his permission as read for Organization admin")
def edit_orgadmin_employee(context):
    page = Create_employeePage(context)
    page.edit_employee_org_admin_pending()
    del page

@when("Organization admin search himself and change his permission from Edit to Read")
def org_admin_change_read_permission_himself(context):
    page4 = Create_employeePage(context)
    page4.edit_himself_org_admin(orgs['AdminFname1'])
    del page4

@then("Verify Only Read view should be displayed to Organization admin")
def verify_read_view(context):
    page = Create_employeePage(context)
    page.verify_employee_tab()
    del page

@when("another Benemax admin with Owner permission Login and change Benemax amdin permission to Read")
def benemax_admin_login(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page = LoginPage(context)
    page.login()
    del page
    page = EditAdminPage(context)
    page.click_admin_tab()
    del page
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(orgs['AdminFname1'])
    page4.verify_searched_admin(orgs['AdminFname1'])
    del page4
    page = EditAdminPage(context)
    page.click_edit_administrator()
    page.edit_admin_read_permission()
    del page

@when("Benemax admin with owner permission signout and Benemax admin with Read permission Login")
def admin_read_login(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page = LoginPage(context)
    page.dynamic_login_with_click_loginink(orgs['BenemaxAdminEmail'],"12345678")
    del page


@when("Organization admin access switch role and switch role as Benemax admin")
def orgadmin_switchrole_benemaxadmin(context):
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    page4.click_benemax_admin()
    del page4

@when("Benemax admin search same Organization")
def search_org(context):
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs['org7'])
    del page

@then("Verify only View Organization option should be displayed")
def verify_view_organization(context):
    page = EditOrganizationPage(context)
    page.verify_view_organization()
    del page

@when("Benemax admin with Edit permission access View Organization option")
def access_view_organization(context):
    page = EditOrganizationPage(context)
    page.click_view_organization()
    del page

@then("Verify correct modal should be displayed")
def verify_view_org_modal(context):
    page = EditOrganizationPage(context)
    page.verify_edit_org_Modal()
    page.close_view_org_modal()
    del page

@when("Benemax admin with Read Permission access switch role")
def admin_read_access_switch_role(context):
    page4 = Profile_dropdown_page(context)
    page4.open_switch_role()
    del page4

@when("Benemax admin access Employee role")
def admin_access_employee_role(context):
    page4 = Profile_dropdown_page(context)
    page4.click_employee()
    del page4

@then("Verify he should redirect to Employee Dashboard")
def verify_employee(context):
    page = Create_employeePage(context)
    page.verify_employee_dashboard()
    del page
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

# Login.feature Create_Organization.feature EditOrganization.feature Create_Admin.feature Edit_admin.feature Forgot_Reset_Password.feature CreateAndEdit_Group_Class_Division.feature Create_Employee_and_OrgAdmin.feature
# Account_details.feature ChangePassword.feature