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
from pages.benefit import *

orgs1 = {'org1': str(calendar.timegm(time.gmtime())) + "CapgeminiNew2"}
@when("Benemax admin with owner permission create an organization in pending state to create Benefit and access it")
def step_impl(context):
    page = Create_user(context)
    page.create_benemax_admin_owner_permission3(context)
    del page
    page = ClaimAccountPage(context)
    page.claim_account_invitation_link("12345678","12345678")
    del page
    # page = LoginPage(context)
    # page.login()
    # page.verify_afterlogin()
    # del page
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

@when("Benemax admin with owner permission create group, class and division to create Benefit for that pending state organization")
def create_grp_cls_dvsn(context):
    access_org_create_grp_class_division_(context)

@when("Benemax admin with owner permission access Program for that pending state organization to create Benefit")
def access_program(context):
    page1 = Create_employeePage(context)
    page1.click_programs()
    del page1

@when("Benemax admin with owner permission access Create Program for that pending state organization to create Benefit")
def admin_create_program(context):
    page = Create_ProgramPage(context)
    page.click_create_program()
    del page

@then("Verify correct create program modal should be open for Benemax admin with owner permission to create Benefit")
def verify_create_program_modal(context):
    page = Create_ProgramPage(context)
    page.verify_create_program_modal()
    del page

@when("Benemax admin with owner permission Create Pending state Program for that pending state organization to create Benefit")
def create_pending_program(context):
    page = Create_ProgramPage(context)
    page.create_program_pending("G2","D1","C1","P1")
    del page
    time.sleep(1)

@then("Verify success message should be displayed after Program creation for Benemax admin with owner permission to create Benefit")
def verify_success_program(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Successfully")
    del page

@then("Verify Program should be displayed in Pending state to Benemax admin with owner permission and it's status should be Active in table view to create Benefit")
def verify(context):
    page = Create_ProgramPage(context)
    page.verify_pending_program("P1","P1")
    del page

@when("Benemax admin with owner permission access that Pending state Program to create Benefit")
def access_pending_program(context):
    page = Create_BenefitPage(context)
    page.click_program()
    del page

@then("Verify Benemax admin with owner permission should redirect to Benefit Dashboard")
def verify_benefit_dashboard(context):
    page = Create_BenefitPage(context)
    page.verify_benefit_dashboard()
    del page

@when("Benemax admin with owner permission access create a benefit option")
def access_create_benefit(context):
    page = Create_BenefitPage(context)
    page.click_create_benefit()
    del page

@then("Verify correct create a benefit modal should be open for Benemax admin with owner permission")
def verify_benefit_modal(context):
    page = Create_BenefitPage(context)
    page.verify_create_benefit_modal()
    del page

@when("Benemax admin with owner permission create benefit in which line of coverage type is medical")
def create_medical_benefit(context):
    page = Create_BenefitPage(context)
    page.create_medical_insurance_benefit("G2","D1","C1","medical_benefit","carrier_benefit")
    del page

@then("Verify success message should be displayed after Benefit creation in which loc type is medical for Benemax admin with owner permission")
def verify_enroll_program(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit created successfully.")
    del page

@then("Verify Benefit in which loc type is medical should be displayed in Pending state to Benemax admin with owner permission and it's status should be Active in table view and loc should be medical insurance")
def verify_benefit_mi(context):
    page = Create_BenefitPage(context)
    page.verify_pending_benefit("medical_benefit","medical_benefit")
    del page

@when("Benemax admin with owner permission deactivate that Pending state Benefit in which loc type is medical")
def deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.deactivate_verify_benefit()
    del page

@then("Verify Benefit in which loc type is medical should be displayed from pending state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view")
def verify_deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.verify_deactive_benefit("medical_benefit", "medical_benefit")
    del page

@when("Benemax admin with owner permission activate Benefit in which loc type is medical from deactivate state which is previously in Pending state")
def activate_benefit(context):
    page = Create_BenefitPage(context)
    page.activate_verify_benefit()
    del page

@then("Again Verify Benefit in which loc type is medical should be displayed in Pending state and medical insurance type benefit to Benemax admin with owner permission")
def verify_benefit_pending(context):
    page = Create_BenefitPage(context)
    page.verify_pending_benefit("medical_benefit", "medical_benefit")
    page.verify_medical_benefit("medical_benefit", "medical_benefit")
    del page

@when("Benemax admin with owner permission access Edit Benefit option for the Benefit in which loc type is medical")
def access_edit_benefit(context):
    page = Create_BenefitPage(context)
    page.click_edit_benefit()
    del page

@then("Verify correct edit benefit modal should be open for Benemax admin with owner permission in which loc type is medical")
def verify_edit_benefit_modal(context):
    page = Create_BenefitPage(context)
    page.verify_edit_benefit_modal()
    del page

@when("Benemax admin with owner permission edit Benefit on first slide in which loc type is medical")
def edit_benefit_firstslide_mi(context):
    page = Create_BenefitPage(context)
    page.edit_benefit_firstslide_mi("nainsi_c1","nainsi_b1")
    del page

@then("Verify success message should be displayed on first slide for Benefit in which loc type is medical")
def verify_edit_benefit_success_msg1(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit updated successfully.")
    del page

@when("Benemax admin with owner permission edit Benefit on second slide in which loc type is medical")
def edit_benefit_second_slide(context):
    page = Create_BenefitPage(context)
    page.edit_benefit_second_slide()
    del page

@then("Verify success message should be displayed on second slide for Benefit in which loc type is medical")
def verify_edit_benefit_success_msg2(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission edit Benefit on third slide in which loc type is medical")
def edit_benefit_third_slide(context):
    page = Create_BenefitPage(context)
    page.edit_benefit_third_slide()
    del page

@then("Verify success message should be displayed on third slide for Benefit in which loc type is medical")
def verify_edit_benefit_success_msg3(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission edit Benefit on fourth slide in which loc type is medical")
def edit_benefit_fourth_slide(context):
    page = Create_BenefitPage(context)
    page.edit_benefit_fourth_slide()
    del page

@then("Verify success message should be displayed on fourth slide for Benefit in which loc type is medical")
def verify_edit_benefit_success_msg3(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission close Edit Benefit modal for medical insurance type of Benefit")
def close_benefit_modal(context):
    page = Create_BenefitPage(context)
    page.close_edit_benefit()
    del page
    time.sleep(1)


# ############################################################################################################################
#
@when("Benemax admin with owner permission edit that Pending state Program and assign it to open enrollment state to create Benefit")
def edit_program(context):
    page1 = Create_employeePage(context)
    page1.click_programs()
    del page1
    page = Create_ProgramPage(context)
    page.click_edit_program()
    page.edit_pending_program_to_open_enrollment("P2")
    del page
    page = ClaimAccountPage(context)
    page.verify_error_msg("Program effective dates cannot exceed Benefit effective dates.")
    del page
    close_benefit_modal(context)
    page = Create_ProgramPage(context)
    page.click_create_program()
    page.create_program_to_open_enrollment("G2","D1","C1","P2")
    del page


@then("Verify Program should be displayed in Open Enrollment state to Benemax admin with owner permission and it's status should be Active in table view to create Benefit")
def verify_open_enroll_program(context):
    page = Create_ProgramPage(context)
    page.verify_open_enrollment_program("P2","P2")
    del page

@when("Benemax admin with owner permission access that open enrollment state Program to create Benefit")
def access_program(context):
    page = Create_BenefitPage(context)
    page.click_program()
    del page

@then("Verify Benemax admin with owner permission should redirect to Benefit Dashboard to create Dental Insurance type of Benefit")
def verify_benefit_dashboard(context):
    page = Create_BenefitPage(context)
    page.verify_benefit_dashboard()
    del page

@when("Benemax admin with owner permission access create a benefit option to create Dental Insurance type of Benefit")
def access_create_benefit_for_dental(context):
    access_create_benefit(context)

@then("Verify correct create a benefit modal should be open for Benemax admin with owner permission to create Dental Insurance type of Benefit")
def verify_benefit_modal_for_dental(context):
    verify_benefit_modal(context)

@when("Benemax admin with owner permission create benefit in which line of coverage type is Dental")
def create_dental_benefit(context):
    page = Create_BenefitPage(context)
    page.create_dental_insurance_benefit("G2", "D1", "C1", "dental_benefit", "carrier_benefit")
    del page

@then("Verify success message should be displayed after Benefit creation in which loc type is Dental for Benemax admin with owner permission")
def verify_msg_for_dental_benefit(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit created successfully.")
    del page

@then("Verify Benefit in which loc type is Dental should be displayed in Dental Insurance state to Benemax admin with owner permission and it's status should be Active in table view")
def verify_benefit_di(context):
    page = Create_BenefitPage(context)
    page.verify_dental_benefit("dental_benefit", "dental_benefit")
    del page

@when("Benemax admin with owner permission deactivate that Dental Insurance state Benefit in which loc type is Dental")
def deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.deactivate_verify_benefit()
    del page

@then("Verify Benefit in which loc type is Dental should be displayed Dental Insurance state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view")
def verify_deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.verify_deactive_benefit("dental_benefit", "dental_benefit")
    del page

@when("Benemax admin with owner permission activate Benefit in which loc type is Dental from deactivate state")
def activate_benefit(context):
    page = Create_BenefitPage(context)
    page.activate_verify_benefit()
    del page

@then("Again Verify Benefit in which loc type is Dental should be displayed in Dental insurance type benefit to Benemax admin with owner permission")
def verify_benefit_dental(context):
    page = Create_BenefitPage(context)
    page.verify_dental_benefit("dental_benefit", "dental_benefit")
    del page

@when("Benemax admin with owner permission access Edit Benefit option for the Benefit in which loc type is Dental")
def access_edit_benefit_for_dental(context):
    access_edit_benefit(context)

@then("Verify correct edit benefit modal should be open for Benemax admin with owner permission in which loc type is Dental")
def verify_edit_benefit_modal_for_dental(context):
    verify_edit_benefit_modal(context)

@when("Benemax admin with owner permission edit Benefit on first slide in which loc type is Dental")
def edit_benefit_firstslide_di(context):
    page = Create_BenefitPage(context)
    page.edit_benefit_firstslide_di("nainsi_c2", "nainsi_b2")
    del page

@then("Verify success message should be displayed on first slide for Benefit in which loc type is Dental")
def verify_edit_benefit_success_msg1(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit updated successfully.")
    del page

@when("Benemax admin with owner permission edit Benefit on second slide in which loc type is Dental")
def edit_benefit_second_slide_for_dental(context):
    edit_benefit_second_slide(context)

@then("Verify success message should be displayed on second slide for Benefit in which loc type is Dental")
def verify_edit_benefit_success_msg3(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission edit Benefit on third slide in which loc type is Dental")
def edit_benefit_third_slide_for_dental(context):
    edit_benefit_third_slide(context)

@then("Verify success message should be displayed on third slide for Benefit in which loc type is Dental")
def verify_edit_benefit_success_msg4(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission edit Benefit on fourth slide in which loc type is Dental")
def edit_benefit_fourth_slide_for_dental(context):
    edit_benefit_fourth_slide(context)

@then("Verify success message should be displayed on fourth slide for Benefit in which loc type is Dental")
def verify_edit_benefit_success_msg5(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission close Edit Benefit modal for Dental insurance type of Benefit")
def close_benefit_modal_for_dental(context):
    close_benefit_modal(context)
    time.sleep(1)

###################################################################################################################################

@when("Benemax admin with owner permission edit that Open enrollment state Program and assign it to Active state to create Benefit")
def edit_program(context):
    page1 = Create_employeePage(context)
    page1.click_programs()
    del page1
    page = Create_ProgramPage(context)
    page.click_create_program()
    page.create_program_to_open_enrollment("G2","D1","C1","P3")
    page.activate_enroll_program_via_db()
    del page


@then("Verify Program should be displayed in Active state to Benemax admin with owner permission and it's status should be Active in table view to create Benefit")
def verify_open_enroll_program(context):
    page = Create_ProgramPage(context)
    page.verify_active_program("P3","P3")
    del page

@when("Benemax admin with owner permission access that Active state Program to create Benefit")
def access_program(context):
    page = Create_BenefitPage(context)
    page.click_program()
    del page

@then("Verify Benemax admin with owner permission should redirect to Benefit Dashboard to create Vision Insurance type of Benefit")
def verify_benefit_dashboard(context):
    page = Create_BenefitPage(context)
    page.verify_benefit_dashboard()
    del page

@when("Benemax admin with owner permission access create a benefit option to create Vision Insurance type of Benefit")
def access_create_benefit_for_vision(context):
    access_create_benefit(context)

@then("Verify correct create a benefit modal should be open for Benemax admin with owner permission to create Vision Insurance type of Benefit")
def verify_benefit_modal_for_vision(context):
    verify_benefit_modal(context)

@when("Benemax admin with owner permission create benefit in which line of coverage type is Vision")
def create_vision_benefit(context):
    page = Create_BenefitPage(context)
    page.create_vision_insurance_benefit("G2", "D1", "C1", "vision_benefit", "carrier_benefit")
    del page

@then("Verify success message should be displayed after Benefit creation in which loc type is Vision for Benemax admin with owner permission")
def verify_msg_for_vision_benefit(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit created successfully.")
    del page

@then("Verify Benefit in which loc type is Vision should be displayed in Vision Insurance state to Benemax admin with owner permission and it's status should be Active in table view")
def verify_benefit_vi(context):
    page = Create_BenefitPage(context)
    page.verify_vision_benefit("vision_benefit", "vision_benefit")
    del page

@when("Benemax admin with owner permission deactivate that Vision Insurance state Benefit in which loc type is Vision")
def deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.deactivate_verify_benefit()
    del page

@then("Verify Benefit in which loc type is Vision should be displayed Vision Insurance state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view")
def verify_deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.verify_deactive_benefit("vision_benefit", "vision_benefit")
    del page

@when("Benemax admin with owner permission activate Benefit in which loc type is Vision from deactivate state")
def activate_benefit(context):
    page = Create_BenefitPage(context)
    page.activate_verify_benefit()
    del page

@then("Again Verify Benefit in which loc type is Vision should be displayed in Vision insurance type benefit to Benemax admin with owner permission")
def verify_benefit_vision(context):
    page = Create_BenefitPage(context)
    page.verify_vision_benefit("vision_benefit", "vision_benefit")
    del page

@when("Benemax admin with owner permission access Edit Benefit option for the Benefit in which loc type is Vision")
def access_edit_benefit_for_vision(context):
    access_edit_benefit(context)

@then("Verify correct edit benefit modal should be open for Benemax admin with owner permission in which loc type is Vision")
def verify_edit_benefit_modal_for_vision(context):
    verify_edit_benefit_modal(context)

@when("Benemax admin with owner permission edit Benefit on first slide in which loc type is Vision")
def edit_benefit_firstslide_vi(context):
    page = Create_BenefitPage(context)
    page.edit_benefit_firstslide_vi("nainsi_c2", "nainsi_b2")
    del page

@then("Verify success message should be displayed on first slide for Benefit in which loc type is Vision")
def verify_edit_benefit_success_msg1(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit updated successfully.")
    del page

@when("Benemax admin with owner permission edit Benefit on second slide in which loc type is Vision")
def edit_benefit_second_slide_for_vision(context):
    edit_benefit_second_slide(context)

@then("Verify success message should be displayed on second slide for Benefit in which loc type is Vision")
def verify_edit_benefit_success_msg3(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission edit Benefit on third slide in which loc type is Vision")
def edit_benefit_third_slide_for_vision(context):
    edit_benefit_third_slide(context)

@then("Verify success message should be displayed on third slide for Benefit in which loc type is Vision")
def verify_edit_benefit_success_msg4(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission edit Benefit on fourth slide in which loc type is Vision")
def edit_benefit_fourth_slide_for_vision(context):
    edit_benefit_fourth_slide(context)

@then("Verify success message should be displayed on fourth slide for Benefit in which loc type is Vision")
def verify_edit_benefit_success_msg5(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission close Edit Benefit modal for Vision insurance type of Benefit")
def close_benefit_modal_for_vision(context):
    close_benefit_modal(context)
    time.sleep(1)

##########################################################################################################################


@when("Benemax admin with owner permission edit that Open enrollment state Program and assign it to Active state to create Ancillary Benefit")
def edit_program(context):
    page1 = Create_employeePage(context)
    page1.click_programs()
    del page1
    page = Create_ProgramPage(context)
    page.click_create_program()
    page.create_program_to_open_enrollment("G2","D1","C1","P4")
    page.activate_enroll_program_via_db()
    del page


@then("Verify Program should be displayed in Active state to Benemax admin with owner permission and it's status should be Active in table view to create Ancillary Benefit")
def verify_open_enroll_program(context):
    page = Create_ProgramPage(context)
    page.verify_active_program("P4","P4")
    del page

@when("Benemax admin with owner permission access that Active state Program to create Ancillary Benefit")
def access_program(context):
    page = Create_BenefitPage(context)
    page.click_program()
    del page

@then("Verify Benemax admin with owner permission should redirect to Benefit Dashboard to create Ancillary Insurance type of Benefit")
def verify_benefit_dashboard(context):
    page = Create_BenefitPage(context)
    page.verify_benefit_dashboard()
    del page

@when("Benemax admin with owner permission access create a benefit option to create Ancillary Insurance type of Benefit")
def access_create_benefit_for_ancillary(context):
    access_create_benefit(context)

@then("Verify correct create a benefit modal should be open for Benemax admin with owner permission to create Ancillary Insurance type of Benefit")
def verify_benefit_modal_for_ancillary(context):
    verify_benefit_modal(context)

@when("Benemax admin with owner permission create benefit in which line of coverage type is Ancillary")
def create_ancillary_benefit(context):
    page = Create_BenefitPage(context)
    page.create_ancillary_insurance_benefit("G2", "D1", "C1", "ancillary_benefit", "carrier_benefit")
    del page

@then("Verify success message should be displayed after Benefit creation in which loc type is Ancillary for Benemax admin with owner permission")
def verify_msg_for_vision_benefit(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit created successfully.")
    del page

@then("Verify Benefit in which loc type is Ancillary should be displayed in Ancillary Insurance state to Benemax admin with owner permission and it's status should be Active in table view")
def verify_benefit_ai(context):
    page = Create_BenefitPage(context)
    page.verify_ancillary_benefit("ancillary_benefit", "ancillary_benefit")
    del page

@when("Benemax admin with owner permission deactivate that Ancillary Insurance state Benefit in which loc type is Ancillary")
def deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.deactivate_verify_benefit()
    del page

@then("Verify Benefit in which loc type is Ancillary should be displayed in Ancillary Insurance state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view")
def verify_deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.verify_deactive_benefit("ancillary_benefit", "ancillary_benefit")
    del page

@when("Benemax admin with owner permission activate Benefit in which loc type is Ancillary from deactivate state")
def activate_benefit(context):
    page = Create_BenefitPage(context)
    page.activate_verify_benefit()
    del page

@then("Again Verify Benefit in which loc type is Ancillary should be displayed in Ancillary insurance type benefit to Benemax admin with owner permission")
def verify_benefit_ancillary(context):
    page = Create_BenefitPage(context)
    page.verify_ancillary_benefit("ancillary_benefit", "ancillary_benefit")
    del page

@when("Benemax admin with owner permission access Edit Benefit option for the Benefit in which loc type is Ancillary")
def access_edit_benefit_for_ancillary(context):
    access_edit_benefit(context)

@then("Verify correct edit benefit modal should be open for Benemax admin with owner permission in which loc type is Ancillary")
def verify_edit_benefit_modal_for_ancillary(context):
    verify_edit_benefit_modal(context)

@when("Benemax admin with owner permission edit Benefit on first slide in which loc type is Ancillary")
def edit_benefit_firstslide_ai(context):
    page = Create_BenefitPage(context)
    page.edit_benefit_firstslide_ai("nainsi_c2", "nainsi_b2")
    del page

@then("Verify success message should be displayed on first slide for Benefit in which loc type is Ancillary")
def verify_edit_benefit_success_msg1(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit updated successfully.")
    del page

@when("Benemax admin with owner permission edit Benefit on second slide in which loc type is Ancillary")
def edit_benefit_second_slide_for_ancillary(context):
    edit_benefit_second_slide(context)

@then("Verify success message should be displayed on second slide for Benefit in which loc type is Ancillary")
def verify_edit_benefit_success_msg3(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission edit Benefit on third slide in which loc type is Ancillary")
def edit_benefit_third_slide_for_ancillary(context):
    edit_benefit_third_slide(context)

@then("Verify success message should be displayed on third slide for Benefit in which loc type is Ancillary")
def verify_edit_benefit_success_msg4(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission close Edit Benefit modal for Ancillary insurance type of Benefit")
def close_benefit_modal_for_ancillary(context):
    close_benefit_modal(context)
    time.sleep(1)

###########################################################################################################################

@when("Benemax admin with edit permission edit that Open enrollment state Program and assign it to Active state to create fsa Benefit")
def edit_program(context):
    page = Create_employeePage(context)
    page.click_back_to_admin()
    del page
    page = EditAdminPage(context)
    page.click_admin_tab()
    del page
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(orgs['AdminFname3'])
    del page4
    page = EditAdminPage(context)
    page.click_edit_administrator()
    page.edit_admin_edit_permission()
    del page
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs1['org1'])
    del page
    page = Group_class_divisionPage(context)
    page.click_org()
    del page
    page1 = Create_employeePage(context)
    page1.click_programs()
    del page1
    page = Create_ProgramPage(context)
    page.click_create_program()
    page.create_program_to_open_enrollment("G2","D1","C1","P5")
    page.activate_enroll_program_via_db()
    del page


@then("Verify Program should be displayed in Active state to Benemax admin with edit permission and it's status should be Active in table view to create Ancillary Benefit")
def verify_open_enroll_program(context):
    page = Create_ProgramPage(context)
    page.verify_active_program("P5","P5")
    del page

@when("Benemax admin with edit permission access that Active state Program to create fsa Benefit")
def access_program(context):
    page = Create_BenefitPage(context)
    page.click_program()
    del page

@then("Verify Benemax admin with owner permission should redirect to Benefit Dashboard to create fsa Insurance type of Benefit")
def verify_benefit_dashboard(context):
    page = Create_BenefitPage(context)
    page.verify_benefit_dashboard()
    del page

@when("Benemax admin with edit permission access create a benefit option to create fsa Insurance type of Benefit")
def access_create_benefit_for_fsa(context):
    access_create_benefit(context)

@then("Verify correct create a benefit modal should be open for Benemax admin with edit permission to create fsa Insurance type of Benefit")
def verify_benefit_modal_for_fsa(context):
    verify_benefit_modal(context)

@when("Benemax admin with edit permission create benefit in which line of coverage type is fsa")
def create_fsa_benefit(context):
    page = Create_BenefitPage(context)
    page.create_fsa_insurance_benefit("G2", "D1", "C1", "fsa_benefit", "carrier_benefit")
    del page

@then("Verify success message should be displayed after Benefit creation in which loc type is fsa for Benemax admin with edit permission")
def verify_msg_for_fsa_benefit(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit created successfully.")
    del page

@then("Verify Benefit in which loc type is fsa should be displayed in fsa Insurance state to Benemax admin with edit permission and it's status should be Active in table view")
def verify_benefit_fsa(context):
    page = Create_BenefitPage(context)
    page.verify_fsa_benefit("fsa_benefit", "fsa_benefit")
    del page

@when("Benemax admin with edit permission deactivate that fsa Insurance state Benefit in which loc type is fsa")
def deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.deactivate_verify_benefit()
    del page

@then("Verify Benefit in which loc type is fsa should be displayed fsa Insurance state to deactive state for Benemax admin with edit permission and it's status should be deactive in table view")
def verify_deactive_benefit(context):
    page = Create_BenefitPage(context)
    page.verify_deactive_benefit("fsa_benefit", "fsa_benefit")
    del page

@when("Benemax admin with edit permission activate Benefit in which loc type is fsa from deactivate state")
def activate_benefit(context):
    page = Create_BenefitPage(context)
    page.activate_verify_benefit()
    del page

@then("Again Verify Benefit in which loc type is fsa should be displayed in fsa insurance type benefit to Benemax admin with edit permission")
def verify_benefit_fsa(context):
    page = Create_BenefitPage(context)
    page.verify_fsa_benefit("fsa_benefit", "fsa_benefit")
    del page

@when("Benemax admin with edit permission access Edit Benefit option for the Benefit in which loc type is fsa")
def access_edit_benefit_for_fsa(context):
    access_edit_benefit(context)

@then("Verify correct edit benefit modal should be open for Benemax admin with edit permission in which loc type is fsa")
def verify_edit_benefit_modal_for_ancillary(context):
    verify_edit_benefit_modal(context)

@when("Benemax admin with edit permission edit Benefit on first slide in which loc type is fsa")
def edit_benefit_firstslide_fsa(context):
    page = Create_BenefitPage(context)
    page.edit_benefit_firstslide_fsa("nainsi_c2", "nainsi_b2")
    del page

@then("Verify success message should be displayed on first slide for Benefit in which loc type is fsa")
def verify_edit_benefit_success_msg1(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Benefit updated successfully.")
    del page

@when("Benemax admin with owner permission edit Benefit on second slide in which loc type is fsa")
def edit_benefit_second_slide_for_ancillary(context):
    edit_benefit_second_slide(context)

@then("Verify success message should be displayed on second slide for Benefit in which loc type is fsa")
def verify_edit_benefit_success_msg3(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with owner permission edit Benefit on third slide in which loc type is fsa")
def edit_benefit_third_slide_for_fsa(context):
    edit_benefit_third_slide(context)

@then("Verify success message should be displayed on third slide for Benefit in which loc type is fsa")
def verify_edit_benefit_success_msg4(context):
    verify_edit_benefit_success_msg1(context)

@when("Benemax admin with edit permission close Edit Benefit modal for fsa insurance type of Benefit")
def close_benefit_modal_for_fsa(context):
    close_benefit_modal(context)
    time.sleep(1)

