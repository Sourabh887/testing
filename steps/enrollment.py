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
from pages.create_employee import *
from pages.create_program import *
from steps.create_program import *
from steps.benefit import *
import calendar
import time
from pages.benefit import *
from pages.enrollment import *
from datetime import timedelta
from datetime import datetime

orgs = Create_user.getOrgs()
orgs2 = {'org2': str(calendar.timegm(time.gmtime())) + "CapgeminiNew3"}
@when("I Create Benemax admin with owner permission and he logged in and create organization and activate it")
def step_impl(context):
    page = Create_user(context)
    page.create_benemax_admin_owner_permission4(context)
    del page
    page = ClaimAccountPage(context)
    page.claim_account_invitation_link("12345678","12345678")
    del page
    page = LoginPage(context)
    # page.login()
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
    page5.enter_org_disp_name(orgs2['org2'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs2['org2'])
    del page
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_activate()
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs2['org2'])
    del page
    del page1

@when("Benemax admin associate himself in that active Organization")
def admin_associate_himslef_as_employee(context):
    access_org_create_grp_class_division_(context)
    verify_create_employee(context)
    access_create_employee(context)
    verify_employee_modal(context)
    page = Create_employeePage(context)
    page.create_enroll_employee("G2","D1","C1")
    del page


@then("Verify Benemax admin as an employee should be show in active state for that active Organization")
def verify_active_admin(context):
    page = Create_employeePage(context)
    page.verify_active_state_created_employee3("nainsi_enroll","nainsi_enroll")
    del page

@when("Benemax admin switch his role as Employee")
def admin_switchrole_asemployee(context):
    page = Profile_dropdown_page(context)
    page.open_switch_role()
    page.click_employee()

@then("Verify default message should be display when there is no Program on Dashboard")
def verify_no_program_view_on_employee_dashboard(context):
    page = Enrollment_Page(context)
    page.verify_no_program_view()
    del page

@when("Employee switch his role back as Benemax admin")
def employee_switchrole_as_admin(context):
    page = Profile_dropdown_page(context)
    page.open_switch_role()
    page.click_benemax_admin()
    del page

@When("Benemax admin access same Organization to Create open Enrollment Program in it")
def admin_access_org(context):
    page = SearchOrganization(context)
    page.search_with_active_filter(orgs2['org2'])
    del page
    page = Group_class_divisionPage(context)
    page.click_org()
    del page

@when("Benemax admin with owner permission create Program for open enrollment state")
def create_open_enroll_program(context):
    page1 = Create_employeePage(context)
    page1.click_programs()
    del page1
    admin_create_program(context)
    create_pending_program(context)
    verify_success_program(context)
    edit_pending_program(context)
    verify_success_program(context)

@when("Benemax admin with owner permission create all types of Benefits in that Program")
def access_pending_program(context):
    page = Create_BenefitPage(context)
    page.click_program()
    del page
    verify_benefit_dashboard(context)
    access_create_benefit(context)
    verify_benefit_modal(context)
    create_medical_benefit(context)
    verify_enroll_program(context)
# # ############################################################################################################################
    access_create_benefit_for_dental(context)
    verify_benefit_modal_for_dental(context)
    create_dental_benefit(context)
    verify_msg_for_dental_benefit(context)
# ###################################################################################################################################
    access_create_benefit_for_vision(context)
    verify_benefit_modal_for_vision(context)
    verify_benefit_modal(context)
    create_vision_benefit(context)
    verify_msg_for_vision_benefit(context)
# ##########################################################################################################################
    access_create_benefit_for_ancillary(context)
    verify_benefit_modal_for_ancillary(context)
    create_ancillary_benefit(context)
    verify_msg_for_vision_benefit(context)
# ###########################################################################################################################
    access_create_benefit_for_fsa(context)
    verify_benefit_modal_for_fsa(context)
    create_fsa_benefit(context)
    verify_msg_for_fsa_benefit(context)

@then("Verify all types of Benefits should be displayed in that Program")
def verify_all_benefits(context):
    verify_benefit_mi(context)
    verify_benefit_di(context)
    verify_benefit_vi(context)
    verify_benefit_ai(context)
    verify_benefit_fsa(context)

@when("Benemax admin with Owner permission access switch role")
def admin_switch_role_employee(context):
    page = Profile_dropdown_page(context)
    page.open_switch_role()
    del page

@when("Benemax admin switch his role as an employee")
def admin_siwtch_role_employee(context):
    page = Profile_dropdown_page(context)
    page.click_employee()
    del page

@then("Verify Program should be displayed on Dashboard")
def verify_prog_on_dashboard(context):
    page = Enrollment_Page(context)
    page.verify_prog_on_emp_dashboard()
    del page

@when("Benemax admin as an employee access that particular Program")
def emp_access_prog(context):
    page = Enrollment_Page(context)
    page.emp_access_prog()
    del page

@then("Verify he should reidrected Program start screen")
def verify_prog_start_page(context):
    page = Enrollment_Page(context)
    page.verify_prog_start_screen()
    del page

@when("Benemax admin as an employee access get started option for open enrollment Program")
def employee_access_get_started(context):
    page = Enrollment_Page(context)
    page.emp_access_prog_first_screen()
    del page

@then("Veirfy he should redircted to members screen")
def verify_members_screen(context):
    page = Enrollment_Page(context)
    page.verify_members_start_screen()
    del page

@when("Benemax admin as an employee access start option on members start screen")
def employee_access_start(context):
    page = Enrollment_Page(context)
    page.employee_access_start()
    del page

@then("Verify he should redirected to Employee and dependents screen")
def verify_employee_and_dependents_screen(context):
    page = Enrollment_Page(context)
    page.verify_employee_and_dependents_screen()
    del page

@then("Verify already prefilled data should be displayed to employee in Primary section")
def verify_employee_already_filled_details(context):
    page = Enrollment_Page(context)
    page1 = Create_user(context)
    a = page1.benemaxadmin_email1
    page.verify_already_filled_primary("nainsi_enroll","j","jain",a)
    del page,page1,a

@when("employee fill valid data in all fields provided and access update option")
def employee_update_primary_details(context):
    page = Enrollment_Page(context)
    page.employee_update_primary_details()
    del page

@then("verify success message should be displayed when we update primary")
def verify_primary_update(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Primary updated successfully.")
    del page

@when("Benemax admin as an employee access add dependent option")
def access_add_dependent(context):
    page = Enrollment_Page(context)
    page.access_add_dependent()
    del page

@then("Verify he should be able to see add dependent page")
def verify_dependent_page(context):
    page = Enrollment_Page(context)
    page.verify_dependent_page()
    del page

@when("employee fill valid data in all fields provided and access add dependent option")
def add_dependent(context):
    page = Enrollment_Page(context)
    page.add_dependent("Spouse","nainsi_enroll2","j","jain2","Junior","nainsi@gmail.com")
    page1 = ClaimAccountPage(context)
    page1.close_popup()
    del page1
    page.access_add_dependent()
    page.add_dependent("Dependent (Under 26)","nainsi_enroll3","j","jain3","Senior","nainsi1@gmail.com")
    page1 = ClaimAccountPage(context)
    page1.close_popup()
    del page1
    page.access_add_dependent()
    page2 = Enrollment_Page(context)
    page2.scroll_to_dob()

    page.add_dependent("Disabled Dependent","nainsi_enroll4","j","jain4","II","nainsi2@gmail.com")
    page1 = ClaimAccountPage(context)
    page1.close_popup()
    del page1
    page.access_add_dependent()
    page2 = Enrollment_Page(context)
    page2.scroll_to_dob()

    page.add_dependent("Domestic Partner","nainsi_enroll5","j","jain5","III","nainsi3@gmail.com")
    page1 = ClaimAccountPage(context)
    page1.close_popup()
    del page1
    page.access_add_dependent()
    page2 = Enrollment_Page(context)
    page2.scroll_to_dob()

    page.add_dependent("Ex-Spouse","nainsi_enroll6","j","jain6","IV","nainsi4@gmail.com")
    page1 = ClaimAccountPage(context)
    page1.close_popup()
    del page1
    page.access_add_dependent()
    page.add_dependent("Dependent of a Dependent","nainsi_enroll7","j","jain7","V","nainsi5@gmail.com")
    del page
    del page2

@then("verify success message should be displayed when we add dependents")
def verify_succcess_message_add_dependent(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Dependent created successfully.")
    del page
    page1 = ClaimAccountPage(context)
    page1.close_popup()
    del page1
    time.sleep(1)

@when("employee access cancel option and access yes option on popup showing for the last added dependent")
def emp_access_cancel(context):
    page = Enrollment_Page(context)
    page.click_cancel_yes_on_popup()
    del page

@when("employee again filled valid data in all fields provided to update dependent")
def emp_update_dependent(context):
    page = Enrollment_Page(context)
    page.emp_update_dependent("Dependent of a Dependent","nainsi_enroll7","j7","jain7","V","nainsi5@gmail.com")
    del page

@then("verify scuccess message should be displayed when employee update dependent")
def verify_success_msg_dependent(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Dependent updated successfully.")
    del page
    page1 = ClaimAccountPage(context)
    page1.close_popup()
    del page1
    time.sleep(1)

@when("Benemax admin as an employee remove particular dependent")
def remove_dependent(context):
    page = Enrollment_Page(context)
    page.remove_dependent()
    del page

@then("Verify success message should be displayed when dependent deleted successfully")
def verify_remove_dependent_success(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Dependent has been deleted successfully")
    del page
    page1 = ClaimAccountPage(context)
    page1.close_popup()
    del page1

@when("Benemax admin as an employee try to add same dependent again")
def again_add_removed_dependent(context):
    page = Enrollment_Page(context)
    page.access_add_dependent()
    page.add_dependent("Dependent of a Dependent", "nainsi_enroll7", "j7", "jain7", "V", "nainsi5@gmail.com")
    page1 = ClaimAccountPage(context)
    page1.verify_success_msg("Dependent created successfully.")
    del page1
    page.emp_update_dependent1("Dependent of a Dependent", "nainsi_enroll7", "j7", "jain7", "V", "nainsi5@gmail.com")
    del page

@then("Verify success message should be displayed when employee added same dependent again")
def verify_success_msg(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Dependent updated successfully.")
    del page

@when("Employee access save and continue option after adding dependents")
def emp_access_save_continue(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page

@then("Verify employee should redirect to medical insurance start screen")
def verify_medical_start_screen(context):
    page = Enrollment_Page(context)
    page.verify_medical_start_screen()
    del page

@when("employee access start option on medical insurance start screen")
def emp_access_start_on_medical_first_screen(context):
    page = Enrollment_Page(context)
    page.emp_access_start_on_medical_first_screen()
    del page

@then("Verify he should redirect to medical insurance screen")
def verify_medical_2_screen(context):
    page = Enrollment_Page(context)
    page.verify_medical_2_screen()
    del page

@when("employee choose no option for the first question of Medical Benefit")
def choose_no_on_medical(context):
    page = Enrollment_Page(context)
    page.choose_no_on_medical()
    del page

@then("Verify he should be able to see second question of Medical Benefit")
def verify_second_question_on_medical(context):
    page = Enrollment_Page(context)
    page.verify_second_question_on_medical()
    del page

@when("employee firstly choose any option apart from other for second question of medical Benefit")
def choose_option_on_medical(context):
    page = Enrollment_Page(context)
    page.emp_choose_option_on_medical()
    del page


@when("employee hit save and continue option for medical insurance screen")
def emp_hit_save_and_continue_on_medical(context):
    emp_access_save_continue(context)

@then("Verify he should redirect to Dental insurance first screen")
def verify_dental_first_screen(context):
    page = Enrollment_Page(context)
    page.verify_dental_first_screen()
    del page

@when("employee access start option on dental insurance start screen")
def emp_access_start_on_dental_screen(context):
    page = Enrollment_Page(context)
    page.emp_access_start_on_dental_first_screen()
    del page

@then("Verify he should redirect to dental insurance screen")
def verify_dental_2_screen(context):
    page = Enrollment_Page(context)
    page.verify_dental_2_screen()
    del page

@when("employee choose no option for the first question of Dental Benefit")
def emp_choose_no_on_dental(context):
    page = Enrollment_Page(context)
    page.choose_no_on_dental()
    del page

@when("employee hit save and continue option and again come back on same medical insurance screen")
def hit_save_and_continue_again_come_back_on_medical(context):
    page = Enrollment_Page(context)
    page.hit_save_and_continue_again_come_back_on_medical()
    del page

@then("Verify correct selected option should be displayed to employee for medical insurance")
def verify_selected_option_on_medical(context):
    page = Enrollment_Page(context)
    page.verify_selected_option_on_medical()
    del page

@when("employee choose other option for second question on medical Benefit")
def emp_choose_other_on_medical(context):
    page = Enrollment_Page(context)
    page.emp_choose_other_on_medical()
    del page

@when("employee fill valid data in other option for medical insurance")
def emp_fill_valid_data_in_other_for_medical(context):
    page = Enrollment_Page(context)
    page.emp_fill_valid_data_in_other_for_medical()
    del page

@when("employee access save and continue option on medical screen and again come back on same screen")
def emp_access_save_and_continue_come_back_on_medical(context):
    hit_save_and_continue_again_come_back_on_medical(context)

@then("verify already filled data should be displayed in other option for medical insurance second question")
def verify_other_data_for_medical(context):
    page = Enrollment_Page(context)
    page.verify_other_data_for_medical()
    del page

@when("employee hit save and continue on medical insurance screen to go on dental screen")
def emp_hit_save_and_continue_on_medical_and_go_on_dental(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page

@when("employee hit save and continue option for dental insurance screen")
def emp_hit_save_and_continue_on_dental(context):
    emp_access_save_continue(context)

@then("Verify he should redirect to Vision insurance first screen")
def verify_vision_first_screen(context):
    page = Enrollment_Page(context)
    page.verify_vision_first_screen()
    del page

@when("employee access start option on Vision insurance start screen")
def emp_access_start_on_vision_screen(context):
    page = Enrollment_Page(context)
    page.emp_access_start_on_vision_first_screen()
    del page

@then("Verify he should redirect to Vision insurance screen")
def verify_vision_2_screen(context):
    page = Enrollment_Page(context)
    page.verify_vision_2_screen()
    del page

@when("employee choose no option for the first question of Vision Benefit")
def emp_choose_no_on_dental(context):
    page = Enrollment_Page(context)
    page.choose_no_on_vision()
    del page

@when("employee hit save and continue option and again come back on same dental insurance screen")
def emp_hit_save_and_continue_again_come_back_on_dental(context):
    page = Enrollment_Page(context)
    page.hit_save_and_continue_again_come_back_on_dental()
    del page

@then("Verify correct selected option should be displayed to employee for dental insurance")
def verify_no_option_on_dental(context):
    page = Enrollment_Page(context)
    page.verify_no_option_on_dental()
    del page

@when("employee hit save and continue on dental insurance screen to go on vision screen")
def emp_hit_save_and_continue_on_dental_and_go_on_vision(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page

@when("employee hit save and continue option for Vision insurance screen")
def emp_hit_save_and_continue_on_vision(context):
    emp_access_save_continue(context)

@then("Verify he should redirect to Ancillary insurance first screen")
def verify_ancillary_first_screen(context):
    page = Enrollment_Page(context)
    page.verify_ancillary_first_screen()
    del page

@when("employee access start option on Ancillary insurance start screen")
def emp_access_start_on_ancillary_screen(context):
    page = Enrollment_Page(context)
    page.emp_access_start_on_ancillary_first_screen()
    del page

@then("Verify he should redirect to Ancillary insurance screen")
def verify_ancillary_2_screen(context):
    page = Enrollment_Page(context)
    page.verify_ancillary_2_screen()
    del page

@when("employee choose no option for the first question of Ancillary Benefit")
def emp_choose_no_on_ancillary(context):
    page = Enrollment_Page(context)
    page.choose_no_on_ancillary()
    del page

@when("employee hit save and continue option and again come back on same Vision insurance screen")
def emp_hit_save_and_continue_again_come_back_on_vision(context):
    page = Enrollment_Page(context)
    page.hit_save_and_continue_again_come_back_on_vision()
    del page


@then("Verify correct selected option should be displayed to employee for Vision insurance")
def verify_no_option_on_vision(context):
    page = Enrollment_Page(context)
    page.verify_no_option_on_vision()
    del page

@when("employee hit save and continue on vision insurance screen to go on ancillary screen")
def emp_hit_save_and_continue_on_vision_and_go_on_ancillary(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page

@when("employee hit save and continue option for Ancillary insurance screen")
def emp_hit_save_and_continue_on_ancillary(context):
    emp_access_save_continue(context)

@then("Verify he should redirect to FSA insurance first screen")
def verify_fsa_first_screen(context):
    page = Enrollment_Page(context)
    page.verify_fsa_first_screen()
    del page

@when("employee access start option on FSA insurance start screen")
def emp_access_start_on_fsa_screen(context):
    page = Enrollment_Page(context)
    page.emp_access_start_on_fsa_first_screen()
    del page

@then("Verify he should redirect to FSA insurance screen")
def verify_fsa_2_screen(context):
    page = Enrollment_Page(context)
    page.verify_fsa_2_screen()
    del page

@when("employee choose no option for the first question of FSA Benefit")
def emp_choose_no_on_fsa(context):
    page = Enrollment_Page(context)
    page.choose_no_on_fsa()
    del page


@when("employee hit save and continue option and again come back on same Ancillary insurance screen")
def emp_hit_save_and_continue_again_come_back_on_ancillary(context):
    page = Enrollment_Page(context)
    page.hit_save_and_continue_again_come_back_on_ancillary()
    del page

@then("Verify correct selected option should be displayed to employee for Ancillary insurance")
def verify_no_option_on_ancillary(context):
    page = Enrollment_Page(context)
    page.verify_no_option_on_ancillary()
    del page

@when("employee hit save and continue option for FSA insurance screen")
def emp_hit_save_and_continue_on_fsa(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    page.emp_access_save_continue()
    del page

@then("Verify he should redirect to review and submit enrollment screen")
def verify_review_and_submit_screen(context):
    page = Enrollment_Page(context)
    page.verify_review_and_submit_screen()
    del page


@then("Verify correct selected option should be displayed to employee for FSA insurance")
def verify_no_option_on_fsa(context):
    page = Enrollment_Page(context)
    page.hit_save_and_continue_again_come_back_on_fsa()
    page.verify_no_option_on_fsa()
    del page

@when("employee hit save and continue on fsa insurance screen to go on review screen")
def emp_hit_save_and_continue_on_dental_and_go_on_vision(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page

@when("employee verify primary details on review and submit enrollment screen")
def verify_primary_on_review_screen(context):
    page = Enrollment_Page(context)
    page.verify_primary_on_review_screen()
    del page

@then("Verify correct primary details should be displayed to employee")
def verify_primary_details_on_review_screen(context):
    page = Enrollment_Page(context)
    page.verify_primary_details_on_review_screen1(0,"nainsi_enroll1")
    page.verify_primary_details_on_review_screen1(1, "a")
    page.verify_primary_details_on_review_screen1(2, "jain1")
    page.verify_primary_details_on_review_screen1(3, "Senior")
    page.verify_primary_details_on_review_screen1(4, datetime.now().strftime('%m/%d/%Y'))
    page.verify_primary_details_on_review_screen1(5, "female")
    time.sleep(1)
    page.verify_primary_details_on_review_screen1(6, "XXX-XX-1111")
    page.verify_primary_details_on_review_screen1(7, "(123) 456 7890")
    page.verify_primary_details_on_review_screen1(8, orgs['benemaxadmin_email1'])
    page.verify_primary_details_on_review_screen1(9, "No")
    page.verify_primary_details_on_review_screen1(10, "7,rue de la")
    page.verify_primary_details_on_review_screen1(11, "Rotisseriel")
    page.verify_primary_details_on_review_screen1(12, "Paris")
    page.verify_primary_details_on_review_screen1(13, "Florida")
    page.verify_primary_details_on_review_screen1(14, "11111")
    del page

@when("employee verify all the dependents details on review and submit enrollment screen")
def verify_dependents_details_on_review_screen(context):
    page = Enrollment_Page(context)
    page.verify_first_dependent_on_review_screen("nainsi_enroll2 jain2")
    page.verify_second_dependent_on_review_screen("nainsi_enroll3 jain3")
    page.verify_third_dependent_on_review_screen("nainsi_enroll4 jain4")
    page.verify_fourth_dependent_on_review_screen("nainsi_enroll5 jain5")
    page.verify_fifth_dependent_on_review_screen("nainsi_enroll6 jain6")
    page.verify_sixth_dependent_on_review_screen("nainsi_enroll7 jain7")
    del page

@then("Verify correct dependent details should be displayed to employee")
def verify_correct_dependent_details(context):
    page = Enrollment_Page(context)
    page.access_first_dependent_on_review()
    page.verify_primary_details_on_review_screen1(0, "nainsi_enroll2")
    page.verify_primary_details_on_review_screen1(1, "j")
    page.verify_primary_details_on_review_screen1(2, "jain2")
    page.verify_primary_details_on_review_screen1(3, "Junior")
    page.verify_primary_details_on_review_screen1(4, datetime.now().strftime('%m/%d/%Y'))
    page.verify_primary_details_on_review_screen1(5, "female")
    page.verify_primary_details_on_review_screen1(6, "XXX-XX-1111")
    page.verify_primary_details_on_review_screen1(7, "(123) 456 7890")
    page.verify_primary_details_on_review_screen1(8, "nainsi@gmail.com")
    page.verify_primary_details_on_review_screen1(9, "Spouse")
    page.verify_primary_details_on_review_screen1(10, "No")
    page.verify_primary_details_on_review_screen1(11, "7,rue de la1")
    page.verify_primary_details_on_review_screen1(12, "Rotisseriel1")
    page.verify_primary_details_on_review_screen1(13, "Paris1")
    page.verify_primary_details_on_review_screen1(14, "California")
    page.verify_primary_details_on_review_screen1(15, "11111")

    page.access_second_dependent_on_review()
    page.verify_primary_details_on_review_screen1(0, "nainsi_enroll3")
    page.verify_primary_details_on_review_screen1(1, "j")
    page.verify_primary_details_on_review_screen1(2, "jain3")
    page.verify_primary_details_on_review_screen1(3, "Senior")
    page.verify_primary_details_on_review_screen1(4, datetime.now().strftime('%m/%d/%Y'))
    page.verify_primary_details_on_review_screen1(5, "female")
    page.verify_primary_details_on_review_screen1(6, "XXX-XX-1111")
    page.verify_primary_details_on_review_screen1(7, "(123) 456 7890")
    page.verify_primary_details_on_review_screen1(8, "nainsi1@gmail.com")
    page.verify_primary_details_on_review_screen1(9, "Dependent (Under 26)")
    page.verify_primary_details_on_review_screen1(10, "No")
    page.verify_primary_details_on_review_screen1(11, "7,rue de la1")
    page.verify_primary_details_on_review_screen1(12, "Rotisseriel1")
    page.verify_primary_details_on_review_screen1(13, "Paris1")
    page.verify_primary_details_on_review_screen1(14, "California")
    page.verify_primary_details_on_review_screen1(15, "11111")

    page.access_third_dependent_on_review()
    page.verify_primary_details_on_review_screen1(0, "nainsi_enroll4")
    page.verify_primary_details_on_review_screen1(1, "j")
    page.verify_primary_details_on_review_screen1(2, "jain4")
    page.verify_primary_details_on_review_screen1(3, "II")
    page.verify_primary_details_on_review_screen1(4, datetime.now().strftime('%m/%d/%Y'))
    page.verify_primary_details_on_review_screen1(5, "female")
    page.verify_primary_details_on_review_screen1(6, "XXX-XX-1111")
    page.verify_primary_details_on_review_screen1(7, "(123) 456 7890")
    page.verify_primary_details_on_review_screen1(8, "nainsi2@gmail.com")
    page.verify_primary_details_on_review_screen1(9, "Disabled Dependent")
    page.verify_primary_details_on_review_screen1(10, "No")
    page.verify_primary_details_on_review_screen1(11, "7,rue de la1")
    page.verify_primary_details_on_review_screen1(12, "Rotisseriel1")
    page.verify_primary_details_on_review_screen1(13, "Paris1")
    page.verify_primary_details_on_review_screen1(14, "California")
    page.verify_primary_details_on_review_screen1(15, "11111")

    page.access_fourth_dependent_on_review()
    page.verify_primary_details_on_review_screen1(0, "nainsi_enroll5")
    page.verify_primary_details_on_review_screen1(1, "j")
    page.verify_primary_details_on_review_screen1(2, "jain5")
    page.verify_primary_details_on_review_screen1(3, "III")
    page.verify_primary_details_on_review_screen1(4, datetime.now().strftime('%m/%d/%Y'))
    page.verify_primary_details_on_review_screen1(5, "female")
    page.verify_primary_details_on_review_screen1(6, "XXX-XX-1111")
    page.verify_primary_details_on_review_screen1(7, "(123) 456 7890")
    page.verify_primary_details_on_review_screen1(8, "nainsi3@gmail.com")
    page.verify_primary_details_on_review_screen1(9, "Domestic Partner")
    page.verify_primary_details_on_review_screen1(10, "No")
    page.verify_primary_details_on_review_screen1(11, "7,rue de la1")
    page.verify_primary_details_on_review_screen1(12, "Rotisseriel1")
    page.verify_primary_details_on_review_screen1(13, "Paris1")
    page.verify_primary_details_on_review_screen1(14, "California")
    page.verify_primary_details_on_review_screen1(15, "11111")

    page.access_fifth_dependent_on_review()
    page.verify_primary_details_on_review_screen1(0, "nainsi_enroll6")
    page.verify_primary_details_on_review_screen1(1, "j")
    page.verify_primary_details_on_review_screen1(2, "jain6")
    page.verify_primary_details_on_review_screen1(3, "IV")
    page.verify_primary_details_on_review_screen1(4, datetime.now().strftime('%m/%d/%Y'))
    page.verify_primary_details_on_review_screen1(5, "female")
    page.verify_primary_details_on_review_screen1(6, "XXX-XX-1111")
    page.verify_primary_details_on_review_screen1(7, "(123) 456 7890")
    page.verify_primary_details_on_review_screen1(8, "nainsi4@gmail.com")
    page.verify_primary_details_on_review_screen1(9, "Ex-Spouse")
    page.verify_primary_details_on_review_screen1(10, "No")
    page.verify_primary_details_on_review_screen1(11, "7,rue de la1")
    page.verify_primary_details_on_review_screen1(12, "Rotisseriel1")
    page.verify_primary_details_on_review_screen1(13, "Paris1")
    page.verify_primary_details_on_review_screen1(14, "California")
    page.verify_primary_details_on_review_screen1(15, "11111")

    page.access_sixth_dependent_on_review()
    page.verify_primary_details_on_review_screen1(0, "nainsi_enroll7")
    page.verify_primary_details_on_review_screen1(1, "j")
    page.verify_primary_details_on_review_screen1(2, "jain7")
    page.verify_primary_details_on_review_screen1(3, "V")
    page.verify_primary_details_on_review_screen1(4, datetime.now().strftime('%m/%d/%Y'))
    page.verify_primary_details_on_review_screen1(5, "female")

    page.verify_primary_details_on_review_screen1(6, "XXX-XX-2222")
    page.verify_primary_details_on_review_screen1(7, "(123) 456 7890")
    page.verify_primary_details_on_review_screen1(8, "nainsi5@gmail.com")
    page.verify_primary_details_on_review_screen1(9, "Dependent of a Dependent")
    page.verify_primary_details_on_review_screen1(10, "No")
    page.verify_primary_details_on_review_screen1(11, "7,rue de la1")
    page.verify_primary_details_on_review_screen1(12, "Rotisseriel1")
    page.verify_primary_details_on_review_screen1(13, "Paris1")
    page.verify_primary_details_on_review_screen1(14, "California")
    page.verify_primary_details_on_review_screen1(15, "11111")
    del page

@when("employee verify medical insurance when employee choose no option, on review and submit enrollment screen")
def verify_medical_heading_on_review(context):
    page = Enrollment_Page(context)
    page.verify_medical_heading_on_review()
    del page

@then("Verify default message should be displayed for medical insurance when employee choose no option, on review and submit enrollment screen")
def verify_medical_no_on_review(context):
    page = Enrollment_Page(context)
    page.verify_medical_no_on_review()
    del page

@when("employee verify dental insurance when employee choose no option, on review and submit enrollment screen")
def verify_dental_heading_on_review(context):
    page = Enrollment_Page(context)
    page.verify_dental_heading_on_review()
    del page

@then("Verify default message should be displayed for dental insurance when employee choose no option, on review and submit enrollment screen")
def verify_dental_no_on_review(context):
    page = Enrollment_Page(context)
    page.verify_dental_no_on_review()
    del page

@when("employee verify vision insurance when employee choose no option, on review and submit enrollment screen")
def verify_vision_heading_on_review(context):
    page = Enrollment_Page(context)
    page.verify_vision_heading_on_review()
    del page

@then("Verify default message should be displayed for vision insurance when employee choose no option, on review and submit enrollment screen")
def verify_vision_no_on_review(context):
    page = Enrollment_Page(context)
    page.verify_vision_no_on_review()
    del page

@when("employee verify ancillary insurance when employee choose no option, on review and submit enrollment screen")
def verify_ancillary_heading_on_review(context):
    page = Enrollment_Page(context)
    page.verify_ancillary_heading_on_review()
    del page

@then("Verify default message should be displayed for ancillary insurance when employee choose no option, on review and submit enrollment screen")
def verify_vision_no_on_review(context):
    page = Enrollment_Page(context)
    page.verify_ancillary_no_on_review()
    del page

@when("employee verify fsa insurance when employee choose no option, on review and submit enrollment screen")
def verify_fsa_heading_on_review(context):
    page = Enrollment_Page(context)
    page.verify_fsa_heading_on_review()
    del page

@then("Verify default message should be displayed for fsa insurance when employee choose no option, on review and submit enrollment screen")
def verify_vision_no_on_review(context):
    page = Enrollment_Page(context)
    page.verify_fsa_no_on_review()
    del page

@when("employee access save and close option on review and submit enrollment screen")
def emp_access_save_and_close(context):
    page = Enrollment_Page(context)
    page.emp_access_save_and_close()
    del page

@then("Verify employee should redirect to employee dashboard")
def verify_emp_dashboard(context):
    page = Enrollment_Page(context)
    page.verify_emp_dashboard()
    del page

@when("employee switch role as organization admin to see that Program")
def emp_swtich_role_as_org_admin(context):
    page = Profile_dropdown_page(context)
    page.open_switch_role()
    page.click_orgadmin()
    del page

@when("organization admin access program from side bar")
def org_admin_access_prog(context):
    page = Create_employeePage(context)
    page.click_programs()
    del page


@when("organization admin access particular program to see enrollment table")
def org_admin_click_program(context):
    page = Create_BenefitPage(context)
    page.click_program()
    del page

@when("organization admin access enrollment tab to see enrollment table")
def org_admin_access_enrollment_tab(context):
    page = Enrollment_Page(context)
    page.click_enrollment_tab()
    del page

@when("organization admin apply incomplete enrollment filter")
def apply_incomplete_filter_enrollment(context):
    page = Enrollment_Page(context)
    page.apply_incomplete_filter_enrollment()
    del page

@when("organization admin search for same employee to see incomplete enrollment")
def search_employee_on_enrollment_table(context):
    page = Enrollment_Page(context)
    page.search_employee_on_enrollment_table("nainsi_enroll1 jain1")
    del page

@then("Verify correct details should be display to organization admin in enrollment table")
def verify_emp_details_in_enrollment_table(context):
    page = Enrollment_Page(context)
    page.verify_emp_details_in_enrollment_table("nainsi1","jain1","XXX-XX-1111")
    del page

@then("Verify employee status should be incomplete in enrollment table")
def verify_emp_incomplete_status_in_enrollment_table(context):
    page = Enrollment_Page(context)
    page.verify_emp_status_in_enrollment_table("Incomplete")
    del page

@when("organization admin switch role as employee to enroll in that Program")
def orgadmin_switch_role_as_employee(context):
    page = Profile_dropdown_page(context)
    page.open_switch_role()
    page.click_employee()
    del page


@when("employee access same Program again to choose yes option for all types of Benefits")
def emp_access_same_program_again(context):
    page = Enrollment_Page(context)
    page.emp_access_prog_again()
    del page

@then("Verify employee should be able to see employee and dependents start screen")
def verify_emp_dependent_start_screen(context):
    page = Enrollment_Page(context)
    page.verify_employee_and_dependents_screen()
    del page

@when("employee choose save and continue on all the screens and comes on medical insurance screen")
def emp_choose_save_and_continue_on_all_screens_before_medical(context):
    employee_access_start(context)
    emp_access_save_continue(context)
    time.sleep(1)

@then("Verify employee should redirect to medical insurance screen to select yes option for it")
def verify_medical_start_screen(context):
    emp_access_start_on_medical_first_screen(context)
    verify_medical_2_screen(context)

@when("employee choose yes option for the first question of Medical Benefit")
def emp_choose_yes_on_medical(context):
    page = Enrollment_Page(context)
    page.emp_choose_option_on_medical()
    page.choose_yes_on_medical()
    del page

@then("Verify he should be able to see second question of Medical Benefit when choose yes option")
def verify_second_question_on_medical1(context):
    page = Enrollment_Page(context)
    page.verify_second_question_on_medical1()
    del page

@then("Verify employee should be display in showing plans for, for the next question available on Medical Benefit")
def verify_emp_heading_third_qu_medical(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_medical("Employee")
    del page

@when("employee select spouse dependent for medical insurance benefit")
def emp_select_spouse_for_dependent(context):
    page = Enrollment_Page(context)
    page.emp_select_first_dependent()
    del page

@then("Verify employee+spouse should be displayed in showing plans for, for the next question available on Medical Benefit")
def verify_emp_heading_third_qu_medical(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_medical("Employee + Spouse")
    del page

@when("employee deselect spouse and select Dependent under (26) for medical insurance benefit")
def emp_deselect_spouse_select_dependent_under_26(context):
    emp_select_spouse_for_dependent(context)
    page = Enrollment_Page(context)
    page.emp_select_second_dependent()
    del page

@then("Verify employee+child should be displayed in showing plans for, for the next question available on Medical Benefit")
def verify_emp_heading_third_qu_medical(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_medical("Employee + child")
    del page

@when("employee select Dependent under (26) and Disabled dependent for medical insurance benefit")
def emp_select_dependent26_and_disabled_dependent(context):
    page = Enrollment_Page(context)
    page.emp_select_third_dependent()
    del page

@then("Verify employee+children should be display in showing plans for, for the next question available on Medical Benefit")
def verify_emp_heading_third_qu_medical(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_medical("Employee + Children")
    del page

@when("employee select all the dependents available for medical insurance Benefit")
def emp_select_all_dependents(context):
    emp_select_spouse_for_dependent(context)
    page = Enrollment_Page(context)
    page.emp_select_fourth_dependent()
    page.emp_select_fifth_dependent()
    page.emp_select_sixth_dependent()
    del page

@then("Verify employee+family should be display in showing plans for, for the next question available on Medical Benefit")
def verify_emp_heading_third_qu_medical(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_medical("Family")
    del page

@then("Verify that employee should be able to see third question available for medical insurance Benefit")
def verify_third_qu_on_medical(context):
    page = Enrollment_Page(context)
    page.verify_third_question_on_medical()
    del page

@then("Verify employee should be able to see Medical insurace plan details on plan container")
def verify_medical_plan_details(context):
    page = Enrollment_Page(context)
    page.verify_medical_plan_details()
    del page

@when("employee access more information for medical insurance")
def emp_access_more_info_on_medical(context):
    page = Enrollment_Page(context)
    page.emp_access_more_info()
    del page

@then("Verify correct information should be display on more information popup for medical insurance Benefit")
def verify_medical_more_info_details(context):
    page = Enrollment_Page(context)
    page.verify_plan_more_info_details("medical_benefit","Medical Insurance","$50")
    del page

@when("employee close more information popup for medical insurance Benefit")
def close_more_info_popup(context):
    page = Enrollment_Page(context)
    page.close_more_info_popup()
    del page

@when("employee choose specific plan for medical insurance Benefit")
def emp_choose_medical_plan(context):
    page = Enrollment_Page(context)
    page.emp_choose_medical_plan()
    del page

@then("Verify employee should be able to see fourth question for medical insurance Benefit")
def verify_fourth_qu_on_medical(context):
    page = Enrollment_Page(context)
    page.verify_fourth_question_on_medical()
    del page

@then("Verify that employee should be able to see first primary care physician for medical insurance Benefit")
def verify_first_primary_pcp_heading_medical(context):
    page = Enrollment_Page(context)
    page.verify_first_primary_pcp_heading_medical()
    del page

@when("employee fill details for first primary care physician for medical insurance Benefit")
def emp_add_first_pcp_medical(context):
    page = Enrollment_Page(context)
    page.emp_add_first_pcp_medical()
    del page

# @then("Verify that employee should be able to see second primary care physician for medical insurance Benefit")
# def verify_dependent1_pcp_heading_medical(context):
#     page = Enrollment_Page(context)
#     page.verify_first_dependent_pcp_heading_medical()
#     del page

@when("employee fill details for second primary care physician for medical insurance Benefit")
def emp_add_second_pcp_medical(context):
    page = Enrollment_Page(context)
    page.emp_add_first_dependent1_pcp_medical()
    del page

# @then("Verify that employee should be able to see third primary care physician for medical insurance Benefit")
# def verify_dependent2_pcp_heading_medical(context):
#     page = Enrollment_Page(context)
#     page.verify_second_dependent_pcp_heading_medical()
#     del page

@when("employee fill details for third primary care physician for medical insurance Benefit")
def emp_add_third_pcp_medical(context):
    page = Enrollment_Page(context)
    page.emp_add_first_dependent2_pcp_medical()
    del page

# @then("Verify that employee should be able to see fourth primary care physician for medical insurance Benefit")
# def verify_dependent3_pcp_heading_medical(context):
#     page = Enrollment_Page(context)
#     page.verify_third_dependent_pcp_heading_medical()
#     del page

@when("employee fill details for fourth primary care physician for medical insurance Benefit")
def emp_add_fourth_pcp_medical(context):
    page = Enrollment_Page(context)
    page.emp_add_first_dependent3_pcp_medical()
    del page

# @then("Verify that employee should be able to see fifth primary care physician for medical insurance Benefit")
# def verify_dependent4_pcp_heading_medical(context):
#     page = Enrollment_Page(context)
#     page.verify_fourth_dependent_pcp_heading_medical()
#     del page

@when("employee fill details for fifth primary care physician for medical insurance Benefit")
def emp_add_fifth_pcp_medical(context):
    page = Enrollment_Page(context)
    page.emp_add_first_dependent4_pcp_medical()
    del page

# @then("Verify that employee should be able to see sixth primary care physician for medical insurance Benefit")
# def verify_dependent5_pcp_heading_medical(context):
#     page = Enrollment_Page(context)
#     page.verify_fifth_dependent_pcp_heading_medical()
#     del page

@when("employee fill details for sixth primary care physician for medical insurance Benefit")
def emp_add_sixth_pcp_medical(context):
    page = Enrollment_Page(context)
    page.emp_add_first_dependent5_pcp_medical()
    del page

# @then("Verify that employee should be able to see seventh primary care physician for medical insurance Benefit")
# def verify_dependent6_pcp_heading_medical(context):
#     page = Enrollment_Page(context)
#     page.verify_sixth_dependent_pcp_heading_medical()
#     del page

@when("employee fill details for seventh primary care physician for medical insurance Benefit")
def emp_add_seventh_pcp_medical(context):
    page = Enrollment_Page(context)
    page.emp_add_first_dependent6_pcp_medical()
    del page
    time.sleep(1)

@when("employee choose Save and continue option on medical insurance when choose yes option")
def emp_choose_save_and_continue_on_medical(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page


########################################################################################################################

@then("Verify employee should redirect to Dental insurance screen to select yes option for it")
def verify_dental_start_screen(context):
    emp_access_start_on_dental_screen(context)
    verify_dental_2_screen(context)

@when("employee choose yes option for the first question of Dental Benefit")
def emp_choose_yes_on_dental(context):
    page = Enrollment_Page(context)
    page.choose_yes_on_dental()
    del page

@then("Verify he should be able to see second question of Dental Benefit when choose yes option")
def verify_second_question_on_dental1(context):
    page = Enrollment_Page(context)
    page.verify_second_question_on_dental1()
    del page

@then("Verify employee should be display in showing plans for, for the next question available on Dental Benefit")
def verify_emp_heading_third_qu_dental(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_dental("Employee")
    del page

@when("employee select spouse dependent for Dental insurance benefit")
def emp_select_spouse_for_dependent_dental(context):
    page = Enrollment_Page(context)
    page.emp_select_first_dependent_di()
    del page

@then("Verify employee+spouse should be displayed in showing plans for, for the next question available on Dental Benefit")
def verify_emp_heading_third_qu_dental(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_dental("Employee + Spouse")
    del page

@when("employee deselect spouse and select Dependent under (26) for Dental insurance benefit")
def emp_deselect_spouse_select_dependent_under_26_dental(context):
    emp_select_spouse_for_dependent_dental(context)
    page = Enrollment_Page(context)
    page.emp_select_second_dependent_di()
    del page

@then("Verify employee+child should be displayed in showing plans for, for the next question available on Dental Benefit")
def verify_emp_heading_third_qu_dental(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_dental("Employee + child")
    del page

@when("employee select Dependent under (26) and Disabled dependent for Dental insurance benefit")
def emp_select_dependent26_and_disabled_dependent_dental(context):
    page = Enrollment_Page(context)
    page.emp_select_third_dependent_di()
    del page

@then("Verify employee+children should be display in showing plans for, for the next question available on Dental Benefit")
def verify_emp_heading_third_qu_dental(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_dental("Employee + Children")
    del page

@when("employee select all the dependents available for Dental insurance Benefit")
def emp_select_all_dependents(context):
    emp_select_spouse_for_dependent_dental(context)
    page = Enrollment_Page(context)
    page.emp_select_fourth_dependent_di()
    page.emp_select_fifth_dependent_di()
    page.emp_select_sixth_dependent_di()
    del page

@then("Verify employee+family should be display in showing plans for, for the next question available on Dental Benefit")
def verify_emp_heading_third_qu_dental(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_dental("Family")
    del page

@then("Verify that employee should be able to see third question available for Dental insurance Benefit")
def verify_third_qu_on_dental(context):
    page = Enrollment_Page(context)
    page.verify_third_question_on_dental()
    del page

@then("Verify employee should be able to see Dental insurace plan details on plan container")
def verify_dental_plan_details(context):
    page = Enrollment_Page(context)
    page.verify_dental_plan_details()
    del page

@when("employee access more information for Dental insurance")
def emp_access_more_info_on_dental(context):
    page = Enrollment_Page(context)
    page.emp_access_more_info_dental()
    del page

@then("Verify correct information should be display on more information popup for Dental insurance Benefit")
def verify_dental_more_info_details(context):
    page = Enrollment_Page(context)
    page.verify_plan_more_info_details("dental_benefit", "Dental Insurance", "$50")
    del page

@when("employee close more information popup for Dental insurance Benefit")
def close_more_info_popup(context):
    page = Enrollment_Page(context)
    page.close_more_info_popup()
    del page

@when("employee choose specific plan for Dental insurance Benefit")
def emp_choose_dental_plan(context):
    page = Enrollment_Page(context)
    page.emp_choose_medical_plan()
    del page

@when("employee choose Save and continue option on Dental insurance when choose yes option")
def emp_choose_save_and_continue_on_dental(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page
    time.sleep(2)


########################################################################################################################

@then("Verify employee should redirect to Vision insurance screen to select yes option for it")
def verify_vision_start_screen(context):
    try:
     emp_access_start_on_vision_screen(context)
    except:
        print("unable to click start on vision")
    time.sleep(3)
    verify_vision_2_screen(context)


@when("employee choose yes option for the first question of Vision Benefit")
def emp_choose_yes_on_vision(context):
    page = Enrollment_Page(context)
    page.choose_yes_on_vision()
    del page


@then("Verify he should be able to see second question of Vision Benefit when choose yes option")
def verify_second_question_on_vision1(context):
    page = Enrollment_Page(context)
    page.verify_second_question_on_vision1()
    del page

@then("Verify employee should be display in showing plans for, for the next question available on Vision Benefit")
def verify_emp_heading_third_qu_vision(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_vision("Employee")
    del page

@when("employee select spouse dependent for Vision insurance benefit")
def emp_select_spouse_for_dependent_vision(context):
    page = Enrollment_Page(context)
    page.emp_select_first_dependent_vi()
    del page

@then("Verify employee+spouse should be displayed in showing plans for, for the next question available on Vision Benefit")
def verify_emp_heading_third_qu_dental(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_vision("Employee + Spouse")
    del page

@when("employee deselect spouse and select Dependent under (26) for Vision insurance benefit")
def emp_deselect_spouse_select_dependent_under_26_vision(context):
    emp_select_spouse_for_dependent_vision(context)
    page = Enrollment_Page(context)
    page.emp_select_second_dependent_vi()
    del page

@then("Verify employee+child should be displayed in showing plans for, for the next question available on Vision Benefit")
def verify_emp_heading_third_qu_vision(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_vision("Employee + child")
    del page

@when("employee select Dependent under (26) and Disabled dependent for Vision insurance benefit")
def emp_select_dependent26_and_disabled_dependent_vision(context):
    page = Enrollment_Page(context)
    page.emp_select_third_dependent_vi()
    del page

@then("Verify employee+children should be display in showing plans for, for the next question available on Vision Benefit")
def verify_emp_heading_third_qu_vision(context):
    page = Enrollment_Page(context)
    page.verify_heading_third_qu_vision("Employee + Children")
    del page

@then("Verify that employee should be able to see third question available for Vision insurance Benefit")
def verify_third_qu_on_vision(context):
    page = Enrollment_Page(context)
    page.verify_third_question_on_vision()
    del page

@then("Verify employee should be able to see Vision insurace plan details on plan container")
def verify_vision_plan_details(context):
    page = Enrollment_Page(context)
    page.verify_vision_plan_details()
    del page

@when("employee access more information for Vision insurance")
def emp_access_more_info_on_vision(context):
    page = Enrollment_Page(context)
    page.emp_access_more_info_vision()
    del page

@then("Verify correct information should be display on more information popup for Vision insurance Benefit")
def verify_vision_more_info_details(context):
    page = Enrollment_Page(context)
    page.verify_plan_more_info_details("vision_benefit", "Vision Insurance", "$40")
    del page

@when("employee close more information popup for Vision insurance Benefit")
def close_more_info_popup(context):
    page = Enrollment_Page(context)
    page.close_more_info_popup()
    del page

@when("employee choose specific plan for Vision insurance Benefit")
def emp_choose_vision_plan(context):
    page = Enrollment_Page(context)
    page.emp_choose_medical_plan()
    del page

@when("employee choose Save and continue option on Vision insurance when choose yes option")
def emp_choose_save_and_continue_on_vision(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page

##########################################################################################################

@then("Verify employee should redirect to Ancillary insurance screen to select yes option for it")
def verify_ancillary_start_screen(context):
    verify_ancillary_2_screen(context)

@when("employee choose yes option for the first question of Ancillary Benefit")
def emp_choose_yes_on_ancillary(context):
    page = Enrollment_Page(context)
    page.choose_yes_on_ancillary()
    del page

@then("Verify he should be able to see second question of Ancillary Benefit when choose yes option")
def verify_second_question_on_ancillary1(context):
    page = Enrollment_Page(context)
    page.verify_second_question_on_ancillary1()
    del page

@then("Verify employee should be able to see Ancillary insurace plan details on plan container")
def verify_ancillary_plan_details(context):
    page = Enrollment_Page(context)
    page.verify_ancillary_plan_details()
    del page

@when("employee access more information for Ancillary insurance")
def emp_access_more_info_on_Ancillary(context):
    page = Enrollment_Page(context)
    page.emp_access_more_info_ancillary()
    del page

@then("Verify correct information should be display on more information popup for Ancillary insurance Benefit")
def verify_ancillary_more_info_details(context):
    page = Enrollment_Page(context)
    page.verify_plan_more_info_details_ancillary("ancillary_benefit", "Ancillary Insurance")
    del page

@when("employee close more information popup for Ancillary insurance Benefit")
def close_more_info_popup(context):
    page = Enrollment_Page(context)
    page.close_more_info_popup()
    del page


@then("Verify employee should be able to see third question on Ancillary insurance Benefit")
def verify_third_qu_on_ancillary(context):
    page = Enrollment_Page(context)
    page.verify_third_question_on_ancillary()
    del page

@when("employee add 6 primary beneficiaries which satisfied 100 percentage criteria")
def emp_add_6_primary_beneficiary_for_ancillary(context):
    page = Enrollment_Page(context)
    page.emp_add_6_primary_beneficiary_for_ancillary()
    del page

@when("employee add 6 secondary beneficiaries which satisfied 100 percentage criteria")
def emp_add_6_secondary_beneficiary_for_ancillary(context):
    page = Enrollment_Page(context)
    page.emp_add_6_secondary_beneficiary_for_ancillary()
    del page

@when("employee choose specific plan for Ancillary insurance Benefit")
def emp_choose_ancillary_plan(context):
    page = Enrollment_Page(context)
    page.emp_choose_ancillary_plan()
    del page

@when("employee choose Save and continue option on Ancillary insurance when choose yes option")
def emp_choose_save_and_continue_on_vision(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page

##########################################################################################################

@then("Verify employee should redirect to FSA insurance screen to select yes option for it")
def verify_fsa_start_screen(context):
    verify_fsa_2_screen(context)

@when("employee choose yes option for the first question of FSA Benefit")
def emp_choose_yes_on_fsa(context):
    page = Enrollment_Page(context)
    page.choose_yes_on_fsa()
    del page

@then("Verify he should be able to see second question of FSA Benefit when choose yes option")
def verify_second_question_on_fsa1(context):
    page = Enrollment_Page(context)
    page.verify_second_question_on_fsa1()
    del page

@when("employee fill valid data in contribution field for the second question of FSA Benefit")
def emp_fill_contribution_fsa(context):
    page = Enrollment_Page(context)
    page.emp_fill_contribution_fsa()
    del page

@then("Verify he should be able to see third question of FSA Benefit when choose yes option")
def verify_third_qu_fsa(context):
    page = Enrollment_Page(context)
    page.verify_third_qu_fsa()
    del page

@then("Verify correct information should be displayed in terms and condition field for fsa benefit")
def verify_correct_info_terms_condition(context):
    page = Enrollment_Page(context)
    page.verify_correct_info_terms_condition()
    del page

@then("Verify terms and condition box should be checked")
def verify_terms_checkbox_fsa(context):
    page = Enrollment_Page(context)
    page.verify_terms_checkbox_fsa()
    del page

@then("Verify employee should be able to see FSA insurace plan details on plan container")
def verify_fsa_plan_details(context):
    page = Enrollment_Page(context)
    page.verify_fsa_plan_details()
    del page

@when("employee access more information for FSA insurance")
def emp_access_more_info_on_Ancillary(context):
    page = Enrollment_Page(context)
    page.emp_access_more_info_fsa()
    del page

@then("Verify correct information should be display on more information popup for FSA insurance Benefit")
def verify_fsa_more_info_details(context):
    page = Enrollment_Page(context)
    page.verify_plan_more_info_details("fsa_benefit", "Flexible Spending Account","123")
    del page

@when("employee close more information popup for FSA insurance Benefit")
def close_more_info_popup(context):
    page = Enrollment_Page(context)
    page.close_more_info_popup()
    del page

@when("employee access previous option on FSA screen")
def emp_access_previous_fsa(context):
    page = Enrollment_Page(context)
    page.emp_access_previous_fsa()
    del page

@then("verify alert should be display to employee when access previuos option on FSA screen")
def verify_fsa_alert(context):
    page = Enrollment_Page(context)
    page.verify_fsa_alert()
    del page

@when("employee access yes option on the alert display for FSA insurance Benefit")
def emp_access_yes_fsa(context):
    page = Enrollment_Page(context)
    page.emp_access_yes_fsa()
    del page

@when("employee again choose yes option for the first question of FSA Benefit")
def emp_again_choose_yes_fsa(context):
    emp_choose_yes_on_fsa(context)

@when("employee again fill valid data in contribution field for the second question of FSA Benefit")
def emp_again_fill_contribution_fsa(context):
    emp_fill_contribution_fsa(context)

@then("Verify save and continue button should be display in enabled state")
def verify_save_continue_enabled(context):
    page = Enrollment_Page(context)
    page.verify_save_continue_enabled()
    del page

@when("employee hit save and continue on fsa screen")
def emp_choose_save_and_continue_fsa(context):
    page = Enrollment_Page(context)
    page.emp_access_save_continue()
    del page

@then("Verify employee should redirect to review screen to verify all the insurance selected options as yes")
def verify_review_screen(context):
    page = Enrollment_Page(context)
    page.verify_review_and_submit_screen()
    del page

@when("employee verify medical insurance when employee choose yes option, on review and submit enrollment screen")
def verify_medical_heading_on_review_for_yes(context):
    verify_medical_heading_on_review(context)

@then("Verify correct info should be displayed for medical insurance when employee choose yes option, on review and submit enrollment screen")
def verify_medical_yes_on_review(context):
    page = Enrollment_Page(context)
    page.verify_medical_yes_on_review("nainsi_enroll1 jain1","nainsi_enroll2 jain2","nainsi_enroll3 jain3","nainsi_enroll4 jain4","nainsi_enroll5 jain5","nainsi_enroll6 jain6","nainsi_enroll7 jain7","50","nainsi1","nainsi3","nainsi2")
    del page

@when("employee verify dental insurance when employee choose yes option, on review and submit enrollment screen")
def verify_dental_heading_on_review_for_yes(context):
    verify_dental_heading_on_review(context)

@then("Verify correct info should be displayed for dental insurance when employee choose yes option, on review and submit enrollment screen")
def verify_dental_yes_on_review(context):
    page = Enrollment_Page(context)
    page.verify_dental_yes_on_review("nainsi_enroll1 jain1","nainsi_enroll2 jain2","nainsi_enroll3 jain3","nainsi_enroll4 jain4","nainsi_enroll5 jain5","nainsi_enroll6 jain6","nainsi_enroll7 jain7","50")
    del page

@when("employee verify vision insurance when employee choose yes option, on review and submit enrollment screen")
def verify_vision_heading_on_review_for_yes(context):
    verify_vision_heading_on_review(context)

@then("Verify correct info should be displayed for vision insurance when employee choose yes option, on review and submit enrollment screen")
def verify_vision_yes_on_review(context):
    page = Enrollment_Page(context)
    page.verify_vision_yes_on_review("nainsi_enroll1 jain1","nainsi_enroll3 jain3","nainsi_enroll4 jain4","40")
    del page

@when("employee verify ancillary insurance when employee choose yes option, on review and submit enrollment screen")
def verify_ancillary_heading_on_review_for_yes(context):
    verify_ancillary_heading_on_review(context)

@then("Verify correct info should be displayed for ancillary insurance when employee choose yes option, on review and submit enrollment screen")
def verify_ancillary_yes_on_review(context):
    page = Enrollment_Page(context)
    page.verify_ancillary_yes_on_review()
    del page

@when("employee verify fsa insurance when employee choose yes option, on review and submit enrollment screen")
def verify_fsa_heading_on_review_for_yes(context):
    verify_fsa_heading_on_review(context)

@then("Verify correct info should be displayed for fsa insurance when employee choose yes option, on review and submit enrollment screen")
def verify_fsa_yes_on_review(context):
    page = Enrollment_Page(context)
    page.verify_fsa_yes_on_review("123")

