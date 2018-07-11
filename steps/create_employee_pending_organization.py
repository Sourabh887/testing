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

orgs1 = {'org1': str(calendar.timegm(time.gmtime())) + "CapgeminiNew"}

@when("Benemax admin with owner permission create an organzation and search it in Pending filter")
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
    page5.enter_org_disp_name(orgs1['org1'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs1['org1'])
    del page


@when("Benemax admin with owner permission access same pending organization and create group class and division for that organization")
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


@then("Verify Create an Employee option should be visible for pending organization if admin access employee tab")
def verify_create_employee(context):
    page = Create_employeePage(context)
    page.access_employee_tab()
    page.verify_create_employee_btn()
    del page

@when("Benemax admin access create an employee option for pending organization")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an employee for pending organization")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin create an employee for pending organization")
def create_employee(context):
    page = Create_employeePage(context)
    page.create_employee2("G2","D1","C1")
    del page

@when("i search for same employee and select pending filter for pending organization")
def search_employee_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_employee("nainsi1")
    del page

@then("Veirfy employee should be displayed in table view and status should be Pending for pending organization")
def verify_employee_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_employee()
    del page3

# #############################################################################################################################

@when("Benemax admin access create an employee option to create organization admin for pending organization")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an organization admin for pending organization")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin with owner permission again create Organization admin for for pending organization")
def create_org_admin(context):
    page = Create_employeePage(context)
    page.create_org_admin1()
    del page
    time.sleep(2)

@when("i search for same organization admin and select pending filter for pending organization")
def search_orgadmin_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_orgadmin("nainsi3")
    del page

@then("Veirfy organization admin should be displayed in table view and status should be Pending for pending organization")
def verify_orgadmin_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_orgadmin()
    del page3

# ##########################################################################################################

@when("Benemax admin access create an employee option to create organization admin and Employee for pending organization")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an employee and organization admin for pending organization")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin with owner permission again create Organization admin and Employee for for pending organization")
def create_org_admin_employee(context):
    page = Create_employeePage(context)
    page.create_org_admin_employee1("G2","D1","C1")
    del page

@when("i search for same organization admin and employee and select pending filter for pending organization")
def search_orgadmin_employee_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_orgadmin_employee("nainsi5")
    del page

@then("Veirfy organization admin and admin should be displayed in table view and status should be Pending for pending organization")
def verify_orgadmin_employee_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_orgadmin_employee()
    del page3
    time.sleep(2)

# ############################################################################################################


@when("Benemax admin access Edit employee option to Edit organization admin and Employee for pending organization")
def edit_employee(context):
    page = Create_employeePage(context)
    page.click_edit_employee()
    del page

@then("Verify correct modal should be displayed to Edit employee and organization admin for pending organization")
def verify_deactivate_employee(context):
    page4 = Create_employeePage(context)
    page4.verify_employee_edit_employee_modal()
    del page4


@when("Benemax admin with owner permission Edit User and give up his permission from Organization admin for pending organization")
def create_second_orgadmin_employee(context):
    page = Create_employeePage(context)
    page.edit_employee_remove_org_admin_make_employee1()
    del page

@then("Verify Employee status should be displayed in pending in table view for Pending Organization")
def verify_orgadmin_employee_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_orgadmin_employee()
    del page3
########################################################################################

@when("Benemax admin go back and search same Organization and activate it")
def go_back(context):
    page = Create_employeePage(context)
    page.click_back_to_admin()
    del page
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs1['org1'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_activate()
    page.search_with_active_filter(orgs1['org1'])
    del page
    del page1

@when("Benemax admin search Organization in active filter and deactivate it and access it")
def deactivate_org(context):
    page = SearchOrganization(context)
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_deactivate()
    page.search_with_inactive_filter(orgs1['org1'])
    del page
    del page1

@then("Verify Create an Employee option should be visible for deactivate Organization if admin access employee tab")
def verify_create_employee(context):
    page = Group_class_divisionPage(context)
    page.click_org()
    del page
    page = Create_employeePage(context)
    page.access_employee_tab()
    page.verify_create_employee_btn()
    del page

@when("Benemax admin access create an employee option for deactivate Organization")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an employee for deactivate Organization")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin create an employee for deactivate Organization")
def create_employee(context):
    page = Create_employeePage(context)
    page.create_employee3("G2","D1","C1")
    del page

@when("i search for same employee and select pending filter for deactivate Organization")
def search_employee_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_employee2("nainsi2")
    del page

@then("Veirfy employee should be displayed in table view and status should be Pending for deactivate Organization")
def verify_employee_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_employee()
    del page3

#############################################################################################

@when("Benemax admin access create an employee option to create organization admin for deactivate Organization")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an organization admin for deactivate Organization")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin with owner permission again create Organization admin for for deactivate Organization")
def create_org_admin(context):
    page = Create_employeePage(context)
    page.create_org_admin2()
    del page


@when("i search for same organization admin and select pending filter for deactivate Organization")
def search_orgadmin_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_orgadmin1("nainsi4")
    del page

@then("Veirfy organization admin should be displayed in table view and status should be Pending for deactivate Organization")
def verify_orgadmin_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_orgadmin()
    del page3

#########################################################################################################

@when("Benemax admin access create an employee option to create organization admin and Employee for deactivate Organization")
def access_create_employee(context):
    page = Create_employeePage(context)
    page.click_create_employee()
    del page

@then("Verify correct modal should be displayed to create an employee and organization admin for deactivate Organization")
def verify_employee_modal(context):
    page = Create_employeePage(context)
    page.verify_create_employee_modal()
    del page

@when("Benemax admin with owner permission again create Organization admin and Employee for for deactivate Organization")
def create_org_admin_employee(context):
    page = Create_employeePage(context)
    page.create_org_admin_employee2("G2","D1","C1")
    del page

@when("i search for same organization admin and employee and select pending filter for deactivate Organization")
def search_orgadmin_employee_pending(context) :
    page = Create_employeePage(context)
    page.verify_pending_state_created_orgadmin_employee1("nainsi6")
    del page

@then("Veirfy organization admin and admin should be displayed in table view and status should be Pending for deactivate Organization")
def verify_orgadmin_employee_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_orgadmin_employee()
    del page3


#############################################################################################################

@when("Benemax admin access Edit employee option to Edit organization admin and Employee for deactivate Organization")
def edit_employee(context):
    page = Create_employeePage(context)
    page.click_edit_employee()
    del page

@then("Verify correct modal should be displayed to Edit employee and organization admin for deactivate Organization")
def verify_deactivate_employee(context):
    page4 = Create_employeePage(context)
    page4.verify_employee_edit_employee_modal()
    del page4


@when("Benemax admin with owner permission Edit User and give up his permission from Organization admin for deactivate Organization")
def create_second_orgadmin_employee(context):
    page = Create_employeePage(context)
    page.edit_employee_remove_org_admin_make_employee1()
    del page

@then("Verify Employee status should be displayed in pending in table view for deactivate Organization")
def verify_orgadmin_employee_status_pending(context):
    page3 = Create_employeePage(context)
    page3.verify_pending_state_orgadmin_employee()
    del page3







