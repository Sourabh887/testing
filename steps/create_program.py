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
from pages.create_program import *
import calendar
import time

orgs1 = {'org1': str(calendar.timegm(time.gmtime())) + "CapgeminiNew1"}
@when("Benemax admin with owner permission create an organization in pending state and access it")
def step_impl(context):
    page = Create_user(context)
    page.create_benemax_admin_owner_permission2(context)
    del page
    page = ClaimAccountPage(context)
    page.claim_account_invitation_link("12345678","12345678")
    del page
    page = LoginPage(context)
    page.verify_afterlogin()
    del page
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

@when("Benemax admin with owner permission create group, class and division for that pending state organization")
def create_grp_cls_dvsn(context):
    access_org_create_grp_class_division_(context)

@when("Benemax admin with owner permission access Program for that pending state organization")
def access_program(context):
    page1 = Create_employeePage(context)
    page1.click_programs()
    del page1

@when("Benemax admin with owner permission access Create Program for that pending state organization")
def admin_create_program(context):
    page = Create_ProgramPage(context)
    page.click_create_program()
    del page

@then("Verify correct create program modal should be open for Benemax admin with owner permission")
def verify_create_program_modal(context):
    page = Create_ProgramPage(context)
    page.verify_create_program_modal()
    del page

@when("Benemax admin with owner permission Create Pending state Program for that pending state organization")
def create_pending_program(context):
    page = Create_ProgramPage(context)
    page.create_program_pending("G2","D1","C1","P1")
    del page
    time.sleep(1)

@then("Verify success message should be displayed after Program creation for Benemax admin with owner permission")
def verify_success_program(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Successfully")
    del page

@then("Verify Program should be displayed in Pending state to Benemax admin with owner permission and it's status should be Active in table view")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_pending_program("P1","P1")
    del page

@when("Benemax admin with owner permission deactivate that Pending state Program")
def deactivate_pending_program(context):
    page = Create_ProgramPage(context)
    page.deactivate_verify_program()
    del page

@then("Verify Program should be displayed from pending state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view")
def verify_pending_to_deactive_program(context):
    page = Create_ProgramPage(context)
    page.verify_deactive_program("P1","P1")
    del page

@when("Benemax admin with owner permission activate Program from deactivate state which is previously in Pending state")
def activate_pending_to_deactive_program(context):
    page = Create_ProgramPage(context)
    page.activate_verify_program()
    del page

@then("Again Verify Program should be displayed in Pending state to Benemax admin with owner permission")
def verify_program_pending(context):
    page = Create_ProgramPage(context)
    page.verify_pending_program("P1", "P1")
    del page

@when("Benemax admin with owner permission edit that Pending state Program and assign it to open enrollment state")
def edit_pending_program(context):
    page = Create_ProgramPage(context)
    page.click_edit_program()
    page.edit_pending_program_to_open_enrollment("P2")
    del page

@then("Verify Program should be displayed in Open Enrollment state to Benemax admin with owner permission and it's status should be Active in table view")
def verify_enroll_program(context):
    page = Create_ProgramPage(context)
    page.verify_open_enrollment_program("P2","P2")
    del page

@when("Benemax admin with owner permission deactivate that Open enrollment state Program")
def deactivate_open_enroll_program(context):
    page = Create_ProgramPage(context)
    page.deactivate_verify_program()
    del page

@then("Verify Program should be displayed from Open enrollment state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view")
def verify_enroll_to_deactive_program(context):
    page = Create_ProgramPage(context)
    page.verify_deactive_program("P2","P2")
    del page

@when("Benemax admin with owner permission activate Program from deactivate state which is previously in Open Enrollment state")
def activate_enroll_to_deactive_program(context):
    page = Create_ProgramPage(context)
    page.activate_verify_program()
    del page

@then("Again Verify Program should be displayed in Open Enrollment state to Benemax admin with owner permission")
def verify_program_pending(context):
    page = Create_ProgramPage(context)
    page.verify_open_enrollment_program("P2", "P2")
    del page

@when("I open database and change Enrollment start date and Enrollment end date of recently edited Program")
def change_program_from_enroll_active(context):
    page = Create_ProgramPage(context)
    page.activate_enroll_program_via_db()
    del page

@then("Verify Program should be displayed in Active state to Benemax admin with owner permission and it's status should be Active in table view")
def verify_program_from_enroll_to_active(context):
    page = Create_ProgramPage(context)
    page.verify_active_program("P2","P2")
    del page

@when("Benemax admin with owner permission deactivate that Active state Program")
def deactivate_active_program(context):
    page = Create_ProgramPage(context)
    page.deactivate_verify_program()
    del page

@then("Verify Program should be displayed from Active to deactive state for Benemax admin with owner permission and it's status should be deactive in table view")
def verify_deactive_program(context):
    page = Create_ProgramPage(context)
    page.verify_deactive_program("P2","P2")
    del page

@when("Benemax admin with owner permission activate Program from deactivate state which is previously in Active state")
def activate_program_from_active_deactive(context):
    page = Create_ProgramPage(context)
    page.activate_verify_program()
    del page

@then("Again Verify Program should be displayed in Active state to Benemax admin with owner permission")
def verify_program_pending(context):
    page = Create_ProgramPage(context)
    page.verify_active_program("P2","P2")
    del page

@when("I open database and change All the dates of recently edited Program")
def archive_active_program(context):
    page = Create_ProgramPage(context)
    page.archive_active_program_via_db()
    del page

@then("Verify Program should be displayed in Archive state to Benemax admin with owner permission")
def verify_archive_program(context):
    page = Create_ProgramPage(context)
    page.verify_archive_program("P2","P2")
    del page

@then("Verify Program status should be show as Active in table view")
def verify_active_status_archive_program(context):
    pass

############################################################################################################################

@when("Benemax admin with owner permission change his permission from owner to Edit")
def admin_change_permission(context):
    page = Create_employeePage(context)
    page.click_back_to_admin()
    del page
    page = EditAdminPage(context)
    page.click_admin_tab()
    del page
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(orgs['AdminFname2'])
    del page4
    page = EditAdminPage(context)
    page.click_edit_administrator()
    page.edit_admin_edit_permission()
    del page

@when("Benemax admin with Edit permission access Program for that same pending state organization")
def admineditpermission_access_program(context):
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs1['org1'])
    del page
    page = Group_class_divisionPage(context)
    page.click_org()
    del page
    access_program(context)

@when("Benemax admin with Edit permission access Create Program for that pending state organization")
def admineditpermission_access_createprogram(context):
    admin_create_program(context)

@then("Verify correct create program modal should be open for Benemax admin with Edit permission")
def verify(context):
    verify_create_program_modal(context)

@when("Benemax admin with Edit permission Create Pending state Program for that pending state organization")
def admin_editpermission_create_pending_program(context):
    page = Create_ProgramPage(context)
    page.create_program_pending("G2", "D1", "C1", "P3")
    del page
    time.sleep(1)

@then("Verify success message should be displayed after Program creation for Benemax admin with Edit permission")
def verify(context):
    verify_success_program(context)

@then("Verify Program should be displayed in Pending state to Benemax admin with Edit permission and it's status should be Active in table view")
def verify_pending_program_admin_edit_permission(context):
    page = Create_ProgramPage(context)
    page.verify_pending_program("P3", "P3")
    del page

@when("Benemax admin with Edit permission deactivate that Pending state Program")
def admin_deactivate_program(context):
    deactivate_pending_program(context)

@then("Verify Program should be displayed from pending state to deactive state for Benemax admin with Edit permission and it's status should be deactive in table view")
def verify_program_deactive_state(context):
    page = Create_ProgramPage(context)
    page.verify_deactive_program("P3", "P3")
    del page

@when("Benemax admin with Edit permission activate Program from deactivate state which is previously in Pending state")
def admin_activate_pending_program(context):
    activate_pending_to_deactive_program(context)

@then("Again Verify Program should be displayed in Pending state to Benemax admin with Edit permission")
def verify_program_in_pending(context):
    page = Create_ProgramPage(context)
    page.verify_pending_program("P3", "P3")
    del page

@when("Benemax admin with Edit permission edit that Pending state Program and assign it to open enrollment state")
def admin_edit_permission_edit_pending_program(context):
    page = Create_ProgramPage(context)
    page.click_edit_program()
    page.edit_pending_program_to_open_enrollment("P4")
    del page

@then("Verify Program should be displayed in Open Enrollment state to Benemax admin with Edit permission and it's status should be Active in table view")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_open_enrollment_program("P4", "P4")
    del page

@when("Benemax admin with Edit permission deactivate that Open enrollment state Program")
def admin_deactivate_enroll_program(context):
    deactivate_open_enroll_program(context)

@then("Verify Program should be displayed from Open enrollment state to deactive state for Benemax admin with Edit permission and it's status should be deactive in table view")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_deactive_program("P4", "P4")
    del page

@when("Benemax admin with Edit permission activate Program from deactivate state which is previously in Open Enrollment state")
def admin_activate_program(context):
    activate_program_from_active_deactive(context)

@then("Again Verify Program should be displayed in Open Enrollment state to Benemax admin with Edit permission")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_open_enrollment_program("P4", "P4")
    del page

@when("Benemax admin with Edit permission open database and change Enrollment start date and Enrollment end date of recently edited Program")
def admin_active_program(context):
    change_program_from_enroll_active(context)

@then("Verify Program should be displayed in Active state to Benemax admin with Edit permission and it's status should be Active in table view")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_active_program("P4", "P4")
    del page

@when("Benemax admin with Edit permission deactivate that Active state Program")
def active_program(context):
    deactivate_active_program(context)

@then("Verify Program should be displayed from Active to deactive state for Benemax admin with Edit permission and it's status should be deactive in table view")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_deactive_program("P4", "P4")
    del page

@when("Benemax admin with Edit permission activate Program from deactivate state which is previously in Active state")
def activate_program(context):
    activate_program_from_active_deactive(context)

@then("Again Verify Program should be displayed in Active state to Benemax admin with Edit permission")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_active_program("P4", "P4")
    del page

@when("Benemax admin with Edit permission open database and change All the dates of recently edited Program")
def archive_program_admin_edit_permission(context):
    archive_active_program(context)

@then("Verify Program should be displayed in Archive state to Benemax admin with Edit permission")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_archive_program("P4", "P4")
    del page

@then("Verify Program status should be show as Active in table view for Benemax admin with Edit permission")
def verify(context):
    verify_active_status_archive_program(context)