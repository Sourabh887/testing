from selenium.webdriver.common.by import By
from pages.base_page_object import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import calendar
from selenium.webdriver.support.select import Select
from environment import *
from datetime import datetime
from datetime import timedelta
from pages.signup_claim_account import *
# from tkinter import filedialog
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Enrollment_Page(BasePage):
    locator_dictionary = {
        "verify_no_program_view": (By.XPATH, "//h3[contains(text(),'all caught up!')]"),
        "verify_prog_on_dashboard": (By.XPATH, "//p[text()='Open Enrollment']"),
        "access_prog":(By.XPATH,"//p[text()=' Start your enrollment']"),
        "access_prog_again":(By.XPATH,"//p[text()=' Continue your enrollment']"),
        "verify_prog_first_page": (By.XPATH, "//button[text()='Get Started']"),
        "verify_members_first_page": (By.XPATH, "//h3[text()='Employee & Dependents']"),
        "access_members_first_page": (By.XPATH, "//button[text()='Start']"),
        "verify_employee_dependents_page": (By.XPATH, "//h4[text()=' Employee and Dependents ']"),
        "loader": (By.ID, "api-loader"),
        "choose_date": (By.XPATH, "//table[@role='grid']/tbody//tr//td[@role='gridcell']//span[not(@class='disabled') and not(@class ='disabled is-other-month') and not(@class='is-other-month')]"),
        "choose_date1":(By.XPATH,"//div[@class='bs-datepicker-head']"),

        "primary_fname":(By.NAME, "first_name"),
        "primary_middle_name": (By.NAME, "middle_name"),
        "primary_last_name": (By.NAME, "last_name"),
        "primary_suffix": (By.NAME, "suffix"),
        "primary_dob": (By.NAME, "dob"),
        "primary_gender": (By.NAME, "gender"),
        "primary_ssn": (By.NAME, "ssn1"),
        "primary_phone": (By.NAME, "phone"),
        "primary_eamil": (By.NAME, "email"),
        "primary_tobacco": (By.NAME, "take_toboco"),
        "primary_address1": (By.NAME, "address1"),
        "primary_address2": (By.NAME, "address2"),
        "primary_city": (By.NAME, "city"),
        "primary_state": (By.NAME, "state"),
        "primary_zip": (By.NAME, "_zip"),
        "primary_cancel": (By.XPATH, "//button[text()=' Cancel']"),
        "popup_yes_primary":(By.XPATH,"//footer[@class='modal-footer']/button[2]"),
        "primary_update": (By.XPATH, "//button[@type='submit']"),

        "add_dependent_name":(By.XPATH,"//span[text()='Add']"),
        "verify_dependent_page":(By.XPATH,"//span[text()='Dependent']"),
        "dependent_relationship": (By.NAME, "relationship_to_primary"),
        "dependent_checkbox":(By.XPATH,"//label[@for='checkboxG']"),
        "dependent_add": (By.XPATH, "//button[text()='Add Dependent']"),
        "dependent_update": (By.XPATH, "//button[@type='submit']"),
        "header_scroll": (By.XPATH, "//div[@class='row']/div/h3"),
        "scroll_down_ele":(By.XPATH,"//input[@name='email']"),
        "remove_dependent": (By.XPATH, "(//a[@class='close-modal'])[6]"),
        "yes_remove":(By.XPATH,"//span[text()='Yes, Remove']"),
        "scroll_dob":(By.XPATH,"//span[text()='Date of Birth']"),
        "scroll_relationship": (By.XPATH, "//span[text()='Address Line 1']"),
        "save_and_continue":(By.XPATH,"//button[text()='Save and Continue']"),
        "save_and_close": (By.XPATH, "//button[text()=' Save and Close ']"),
        "next_button":(By.XPATH,"//button[text()=' Next']"),
        "next_button1": (By.XPATH, "//button[text()=' Next ']"),
        "previous_button": (By.XPATH, "//button[text()=' Previous ']"),

        "medical_start_screen":(By.XPATH,"//h3[text()='Medical Insurance']"),
        "start_on_medical":(By.XPATH,"//button[text()='Start']"),
        "choose_no_medical":(By.XPATH,"//label[@for='radio2']"),
        "choose_yes_medical": (By.XPATH, "//label[@for='radio1']"),
        "waiving_mi1": (By.XPATH, "//select[@name='waiving_MI']/option[2]"),
        # "second_qu_on_medical":(By.XPATH,"(//*[@id='MIQuestion1']//h3/text())[4]"),
        # "second_qu_on_medical": (By.XPATH, "(//*[@id='MIQuestion1']//h3/text())[last()]"),
        "second_qu_on_medical": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[2]"),
        "second_qu_on_medical_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[3]"),
        "third_qu_on_medical_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[4]"),
        "fourth_qu_on_medical_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[5]"),
        "waiving_mi":(By.NAME,"waiving_MI"),
        "step_2":(By.XPATH,"//li[@class='step1']"),
        "other_reason":(By.ID,"reason"),
        "verify_medical_2_screen":(By.XPATH,"//*[@id='enrollmentHeader']/h4"),
        "verify_no_on_review_for_medical":(By.XPATH,"//p[text()='Not interested in this type of insurance.']"),
        "verify_medical_heading_on_review":(By.XPATH,"//span[text()='Medical Insurance']"),
        "verify_emp_heading_third_qu_medical":(By.XPATH,"//*[@id='MIQuestion3']//span[2]"),
        "medical_fsa_cancel_on_alert":(By.XPATH,"//modal-container//section/div[1]/a"),

        "emp_select_first_dependent":(By.XPATH,"(//label[@class='css-label label-dependants'])[2]"),
        "emp_select_second_dependent": (By.XPATH, "(//label[@class='css-label label-dependants'])[3]"),
        "emp_select_third_dependent": (By.XPATH, "(//label[@class='css-label label-dependants'])[4]"),
        "emp_select_fourth_dependent": (By.XPATH, "(//label[@class='css-label label-dependants'])[5]"),
        "emp_select_fifth_dependent": (By.XPATH, "(//label[@class='css-label label-dependants'])[6]"),
        "emp_select_sixth_dependent": (By.XPATH, "(//label[@class='css-label label-dependants'])[7]"),

        "dental_start_screen": (By.XPATH, "//h3[text()='Dental Insurance']"),
        "start_on_dental": (By.XPATH, "//button[text()='Start']"),
        "verify_dental_2_screen": (By.XPATH, "//*[@id='enrollmentHeader']/h4"),
        "choose_no_dental": (By.XPATH, "//label[@for='enroll-dental7']"),
        "choose_yes_dental": (By.XPATH, "//label[@for='enroll-dental6']"),
        "step_3": (By.XPATH, "//li[@class='step2']"),
        "second_qu_on_dental_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[7]"),
        "third_qu_on_dental_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[8]"),
        "verify_no_on_review_for_dental": (By.XPATH, "//p[text()='You have waived the coverage for this beanefit offering']"),
        "verify_dental_heading_on_review": (By.XPATH, "//span[text()='Dental Insurance']"),
        "verify_emp_heading_third_qu_dental": (By.XPATH, "//*[@id='DIQuestion2']//span[2]"),
        "dental_your_health_plans":(By.XPATH,"//*[@id='DIQuestion2']//div[@class='card-body']/p"),
        "dental_more_info": (By.LINK_TEXT, "More Information"),
        "dental_plan_name": (By.XPATH, "(//div[@class='card-header card-special']/h3)[2]"),
        "dental_plan_cost_per_pay_period": (By.XPATH, "(//div[@class='card-body']/ul/li[1]/div)[2]"),

        "emp_select_first_dependent_di": (By.XPATH, "(//label[@class='css-label label-dependants'])[9]"),
        "emp_select_second_dependent_di": (By.XPATH, "(//label[@class='css-label label-dependants'])[10]"),
        "emp_select_third_dependent_di": (By.XPATH, "(//label[@class='css-label label-dependants'])[11]"),
        "emp_select_fourth_dependent_di": (By.XPATH, "(//label[@class='css-label label-dependants'])[12]"),
        "emp_select_fifth_dependent_di": (By.XPATH, "(//label[@class='css-label label-dependants'])[13]"),
        "emp_select_sixth_dependent_di": (By.XPATH, "(//label[@class='css-label label-dependants'])[14]"),

        "emp_select_first_dependent_vi": (By.XPATH, "(//label[@class='css-label label-dependants'])[16]"),
        "emp_select_second_dependent_vi": (By.XPATH, "(//label[@class='css-label label-dependants'])[17]"),
        "emp_select_third_dependent_vi": (By.XPATH, "(//label[@class='css-label label-dependants'])[18]"),

        "vision_start_screen": (By.XPATH, "//h3[text()='Vision Insurance']"),
        "start_on_vision": (By.XPATH, "//button[text()='Start']"),
        "verify_vision_2_screen": (By.XPATH, "//*[@id='enrollmentHeader']/h4"),
        "choose_no_vision": (By.XPATH, "//label[@for='enroll-dental9']"),
        "choose_yes_vision": (By.XPATH, "//label[@for='enroll-dental8']"),
        "step_4": (By.XPATH, "//li[@class='step3']"),
        "second_qu_on_vision_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[10]"),
        "third_qu_on_vision_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[11]"),
        "verify_no_on_review_for_vision": (By.XPATH, "//p[text()='You have waived the coverage for this beanefit offering']"),
        "verify_vision_heading_on_review": (By.XPATH, "//span[text()='Vision Insurance']"),
        "verify_emp_heading_third_qu_vision": (By.XPATH, "//*[@id='VIQuestion2']//span[2]"),
        "vision_your_health_plans": (By.XPATH, "//*[@id='VIQuestion2']//div[@class='card-body']/p"),
        "vision_more_info": (By.LINK_TEXT, "More Information"),
        "vision_plan_name": (By.XPATH, "(//div[@class='card-header card-special']/h3)[3]"),
        "vision_plan_cost_per_pay_period": (By.XPATH, "(//div[@class='card-body']/ul/li[1]/div)[3]"),

        "ancillary_start_screen": (By.XPATH, "//h3[text()='Ancillary Insurance']"),
        "start_on_ancillary": (By.XPATH, "//button[text()='Start']"),
        "verify_ancillary_2_screen": (By.XPATH, "//*[@id='enrollmentHeader']/h4"),
        "choose_no_ancillary": (By.XPATH, "//label[@for='enroll-dental11']"),
        "choose_yes_ancillary": (By.XPATH, "//label[@for='enroll-dental10']"),
        "step_5": (By.XPATH, "//li[@class='step4']"),
        "second_qu_on_ancillary_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[13]"),
        "third_qu_on_ancillary_yes": (By.XPATH, "(//h3[@class='enroll-heading d-inline-block'])[14]"),
        "verify_no_on_review_for_ancillary": (By.XPATH, "//p[text()='You have waived the coverage for this beanefit offering']"),
        "verify_ancillary_heading_on_review": (By.XPATH, "//span[text()='Ancillary Insurance']"),
        "ancillary_plan_name": (By.XPATH, "(//div[@class='card-header card-special']/h3)[4]"),
        "ancillary_your_health_plans": (By.XPATH, "//*[@id='AIQuestion1']//div[@class='card-body']/p/p"),
        "ancillary_more_info": (By.LINK_TEXT, "More Information"),

        "fsa_start_screen": (By.XPATH, "(//h3[text()='Flexible Spending Accounts'])[1]"),
        "start_on_fsa": (By.XPATH, "//button[text()='Start']"),
        "verify_fsa_2_screen": (By.XPATH, "//*[@id='enrollmentHeader']/h4"),
        "choose_no_fsa": (By.XPATH, "//label[@for='enroll-FSA13']"),
        "choose_yes_fsa": (By.XPATH, "//label[@for='enroll-FSA12']"),
        "step_6": (By.XPATH, "//li[@class='step5']"),
        "second_qu_on_fsa_yes": (By.XPATH, "(//*[@id='flexible_spending']//h3)[3]"),
        "third_qu_on_fsa_yes": (By.XPATH, "(//*[@id='flexible_spending']//h3)[4]"),
        "verify_no_on_review_for_fsa": (By.XPATH, "//p[text()='You have waived the coverage for this beanefit offering']"),
        "verify_fsa_heading_on_review": (By.XPATH, "//span[text()='Flexible Spending Accounts']"),
        "fsa_contribution": (By.XPATH, "//*[@id='flexible_spending']//div[@class='form-group mb-0']/input"),
        "fsa_terms_condition": (By.XPATH,"//*[@id='flexible_spending']//div[@class='enroll-terms']/p"),
        "fsa_terms_checkbox": (By.XPATH, "//label[@for='check-agree']"),
        "fsa_plan_name": (By.XPATH, "//*[@id='flexible_spending']//div[@class='card-header card-special']/h3"),
        "fsa_your_health_plans": (By.XPATH, "//*[@id='flexible_spending']//div[@class='card-body']/p/p"),
        "fsa_more_info": (By.LINK_TEXT, "More Information"),
        "fsa_max_contribution": (By.XPATH, "//*[@id='flexible_spending']//div[@class='planrate']/span"),
        "fsa_alert":(By.XPATH, "//div[@class='modal-header']/h4/span"),
        "yes_fsa":(By.XPATH,"//span[text()='Yes, Remove']"),

        "verify_review_and_submit_screen": (By.XPATH, "//h3[text()='Review and Submit']"),
        "scroll_to_members": (By.XPATH, "//span[text()='Member Details']"),
        "verify_primary_name": (By.XPATH, "(//span[@class='tab-secondary'][text()='nainsi_enroll1 jain1'])[2]"),
        "access_first_dependent_on_review":(By.XPATH,"(//div[@class='enrolled-members']//div[@class='tab-inner-html'])[1]"),
        "verify_first_dependent_name": (By.XPATH, "(//*[@id='review_enroll']//div/span[2])[2]"),
        "access_second_dependent_on_review": (By.XPATH, "(//div[@class='enrolled-members']//div[@class='tab-inner-html'])[2]"),
        "verify_second_dependent_name": (By.XPATH, "(//*[@id='review_enroll']//div/span[2])[3]"),
        "access_third_dependent_on_review": (By.XPATH, "(//div[@class='enrolled-members']//div[@class='tab-inner-html'])[3]"),
        "verify_third_dependent_name": (By.XPATH, "(//*[@id='review_enroll']//div/span[2])[4]"),
        "access_fourth_dependent_on_review": (By.XPATH, "(//div[@class='enrolled-members']//div[@class='tab-inner-html'])[4]"),
        "verify_fourth_dependent_name": (By.XPATH, "(//*[@id='review_enroll']//div/span[2])[5]"),
        "access_fifth_dependent_on_review": (By.XPATH, "(//div[@class='enrolled-members']//div[@class='tab-inner-html'])[5]"),
        "verify_fifth_dependent_name": (By.XPATH, "(//*[@id='review_enroll']//div/span[2])[6]"),
        "access_sixth_dependent_on_review": (By.XPATH,"(//div[@class='enrolled-members']//div[@class='tab-inner-html'])[6]"),
        "verify_sixth_dependent_name": (By.XPATH, "(//*[@id='review_enroll']//div/span[2])[7]"),
        "label_fname":(By.XPATH,"//*[@id='review_enroll']//label[text()='First Name']"),
        "scroll_to_members_on_review":(By.XPATH,"(//h3[@class='enroll-heading enroll-heading-review'])[1]"),
        "review_header": (By.XPATH, "//h3[text()='Review and Submit']"),
        "verify_emp_dashboard":(By.XPATH,"//h3[text()='Your Tasks']"),

        "verify_yes_on_review_for_medical_plan_name":(By.XPATH,"(//div[@class='row row-bordered']/div[@class='col-md-12']/input)[1]"),
        "verify_primary_name_medical_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[1]"),
        "verify_dependent1_name_medical_on_review":(By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[2]"),
        "verify_dependent2_name_medical_on_review":(By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[3]"),
        "verify_dependent3_name_medical_on_review":(By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[4]"),
        "verify_dependent4_name_medical_on_review":(By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[5]"),
        "verify_dependent5_name_medical_on_review":(By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[6]"),
        "verify_dependent6_name_medical_on_review":(By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[7]"),
        "verify_medical_cost_per_pay_period_on_review":(By.XPATH, "(//*[@id='review_enroll']//ul/li[1]//span)[1]"),
        "verify_medical_co_pay_on_review": (By.XPATH, "//*[@id='review_enroll']//ul/li[2]/div"),
        "verify_medical_rx_cost_on_review": (By.XPATH, "//*[@id='review_enroll']//ul/li[3]/div"),
        "verify_medical_deductible_on_review": (By.XPATH, "//*[@id='review_enroll']//ul/li[4]/div"),

        "verify_yes_on_review_for_dental_plan_name": (By.XPATH, "(//div[@class='row row-bordered']/div[@class='col-md-12']/input)[2]"),
        "verify_primary_name_dental_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[8]"),
        "verify_dependent1_name_dental_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[9]"),
        "verify_dependent2_name_dental_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[10]"),
        "verify_dependent3_name_dental_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[11]"),
        "verify_dependent4_name_dental_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[12]"),
        "verify_dependent5_name_dental_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[13]"),
        "verify_dependent6_name_dental_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[14]"),
        "verify_dental_cost_per_pay_period_on_review": (By.XPATH, "(//*[@id='review_enroll']//ul/li[1]//span)[2]"),

        "verify_yes_on_review_for_vision_plan_name": (By.XPATH, "(//div[@class='row row-bordered']/div[@class='col-md-12']/input)[3]"),
        "verify_primary_name_vision_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[15]"),
        "verify_dependent1_name_vision_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[16]"),
        "verify_dependent2_name_vision_on_review": (By.XPATH, "(//*[@id='review_enroll']/form//label/span[2])[17]"),
        "verify_vision_cost_per_pay_period_on_review": (By.XPATH, "(//*[@id='review_enroll']//ul/li[1]//span)[3]"),

        "verify_yes_on_review_for_ancillary_plan_name": (By.XPATH, "(//div[@class='row row-bordered']/div[@class='col-md-12']/input)[4]"),
        "verify_yes_on_review_for_fsa_plan_name": (By.XPATH, "(//div[@class='row row-bordered']/div[@class='col-md-12']/input)[5]"),

        "medical_plan_name":(By.XPATH,"//div[@class='card-header card-special']/h3"),
        "medical_plan_cost_per_pay_period": (By.XPATH, "//div[@class='card-body']/ul/li[1]/div"),
        "medical_plan_co_pay": (By.XPATH, "//div[@class='card-body']/ul/li[2]/div"),
        "medical_plan_rx_cost": (By.XPATH, "//div[@class='card-body']/ul/li[3]/div"),
        "medical_plan_deductible": (By.XPATH, "//div[@class='card-body']/ul/li[4]/div"),
        "choose_medical_plan":(By.XPATH,"//div[@class='card text-center card-enroll-rates']"),
        "choose_ancillary_plan": (By.XPATH, "//*[@id='AIQuestion1']//div[@class='card text-center card-enroll-rates']"),

        "medical_more_info":(By.LINK_TEXT,"More Information"),
        "medical_more_info_benefit_name": (By.XPATH, "//div[@class='benefit-display-name']//p"),
        "medical_more_info_benefit_heading": (By.XPATH, "//h3[@class='benefits-subheading']/span"),
        "medical_more_info_benefit_effective_start_date": (By.XPATH, "//aside/span[1]"),
        "medical_more_info_benefit_effective_end_date": (By.XPATH, "//aside/span[2]"),
        "medical_more_info_cost_per_pay_period": (By.XPATH, "//ul/li/div[@class='planrate text-center']"),
        "medical_more_info_plan_info": (By.XPATH, "//section/div/p"),
        "medical_more_info_quick_links": (By.XPATH, "//section/ul[1]/li/a"),
        "medical_more_info_document_link": (By.XPATH, "//section/ul[2]/li/a"),
        # "plan_more_info_close_modal":(By.XPATH,"//a[@class='close-modal']"),
        "plan_more_info_close_modal": (By.XPATH, "//app-root/div[1]/a"),

        "mi_verify_primary_heading_pcp":(By.XPATH,"(//h4[@class='enroll-subheading ml-0'])[1]"),
        "mi_enter_primary_fname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[1]"),
        "mi_enter_primary_lname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[2]"),
        "mi_enter_primary_pcpid_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[3]"),
        "mi_enter_primary_city_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[4]"),
        "mi_enter_primary_state_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//select)[1]"),
        "mi_enter_primary_zip_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[5]"),

        "mi_verify_dependent1_heading_pcp": (By.XPATH, "(//h4[@class='enroll-subheading ml-0'])[2]"),
        "mi_enter_dependent1_fname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[6]"),
        "mi_enter_dependent1_lname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[7]"),
        "mi_enter_dependent1_pcpid_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[8]"),
        "mi_enter_dependent1_city_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[9]"),
        "mi_enter_dependent1_state_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//select)[2]"),
        "mi_enter_dependent1_zip_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[10]"),

        "mi_verify_dependent2_heading_pcp": (By.XPATH, "(//h4[@class='enroll-subheading ml-0'])[3]"),
        "mi_enter_dependent2_fname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[11]"),
        "mi_enter_dependent2_lname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[12]"),
        "mi_enter_dependent2_pcpid_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[13]"),
        "mi_enter_dependent2_city_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[14]"),
        "mi_enter_dependent2_state_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//select)[3]"),
        "mi_enter_dependent2_zip_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[15]"),

        "mi_verify_dependent3_heading_pcp": (By.XPATH, "(//h4[@class='enroll-subheading ml-0'])[4]"),
        "mi_enter_dependent3_fname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[16]"),
        "mi_enter_dependent3_lname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[17]"),
        "mi_enter_dependent3_pcpid_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[18]"),
        "mi_enter_dependent3_city_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[19]"),
        "mi_enter_dependent3_state_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//select)[4]"),
        "mi_enter_dependent3_zip_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[20]"),

        "mi_verify_dependent4_heading_pcp": (By.XPATH, "(//h4[@class='enroll-subheading ml-0'])[5]"),
        "mi_enter_dependent4_fname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[21]"),
        "mi_enter_dependent4_lname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[22]"),
        "mi_enter_dependent4_pcpid_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[23]"),
        "mi_enter_dependent4_city_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[24]"),
        "mi_enter_dependent4_state_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//select)[5]"),
        "mi_enter_dependent4_zip_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[25]"),

        "mi_verify_dependent5_heading_pcp": (By.XPATH, "(//h4[@class='enroll-subheading ml-0'])[6]"),
        "mi_enter_dependent5_fname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[26]"),
        "mi_enter_dependent5_lname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[27]"),
        "mi_enter_dependent5_pcpid_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[28]"),
        "mi_enter_dependent5_city_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[29]"),
        "mi_enter_dependent5_state_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//select)[6]"),
        "mi_enter_dependent5_zip_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[30]"),

        "mi_verify_dependent6_heading_pcp": (By.XPATH, "(//h4[@class='enroll-subheading ml-0'])[7]"),
        "mi_enter_dependent6_fname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[31]"),
        "mi_enter_dependent6_lname_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[32]"),
        "mi_enter_dependent6_pcpid_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[33]"),
        "mi_enter_dependent6_city_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[34]"),
        "mi_enter_dependent6_state_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//select)[7]"),
        "mi_enter_dependent6_zip_pcp": (By.XPATH, "(//*[@id='MIQuestion4']//input)[35]"),

        "ai_beneficiary_fname":(By.XPATH, "//th[text()='Beneficiary First Name']"),
        "ai_primary1_fname":(By.XPATH,"//*[@id='AIQuestion2']//table/tbody/tr[2]/td[1]/input"),
        "ai_primary1_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[2]/td[2]/input"),
        "ai_primary1_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[2]/td[3]/select"),
        "ai_primary1_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[2]/td[4]/select"),
        "ai_primary1_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[2]/td[5]/div[@class='mt-2']/div[2]/input"),
        "ai_beneficiary_right_checkbox":(By.XPATH, "//button[@class='check-button check-done']"),

        "ai_primary2_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[3]/td[1]/input"),
        "ai_primary2_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[3]/td[2]/input"),
        "ai_primary2_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[3]/td[3]/select"),
        "ai_primary2_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[3]/td[4]/select"),
        "ai_primary2_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[3]/td[5]/div[@class='mt-2']/div[2]/input"),

        "ai_primary3_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[4]/td[1]/input"),
        "ai_primary3_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[4]/td[2]/input"),
        "ai_primary3_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[4]/td[3]/select"),
        "ai_primary3_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[4]/td[4]/select"),
        "ai_primary3_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[4]/td[5]/div[@class='mt-2']/div[2]/input"),

        "ai_primary4_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[5]/td[1]/input"),
        "ai_primary4_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[5]/td[2]/input"),
        "ai_primary4_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[5]/td[3]/select"),
        "ai_primary4_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[5]/td[4]/select"),
        "ai_primary4_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[5]/td[5]/div[@class='mt-2']/div[2]/input"),

        "ai_primary5_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[6]/td[1]/input"),
        "ai_primary5_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[6]/td[2]/input"),
        "ai_primary5_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[6]/td[3]/select"),
        "ai_primary5_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[6]/td[4]/select"),
        "ai_primary5_percentage": (By.XPATH, "//*[@id='AIQuestion2']/div[2]/table/tbody/tr[6]/td[5]/div[@class='mt-2']/div[2]/input"),
        "ai_primary5_other":(By.XPATH,"//*[@id='AIQuestion2']/div[2]/table/tbody/tr[6]/td[4]/input"),

        "ai_primary6_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[7]/td[1]/input"),
        "ai_primary6_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[7]/td[2]/input"),
        "ai_primary6_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[7]/td[3]/select"),
        "ai_primary6_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[7]/td[4]/select"),
        "ai_primary6_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[7]/td[5]/div[@class='mt-2']/div[2]/input"),

        "ai_secondary1_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[8]/td[1]/input"),
        "ai_secondary1_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[8]/td[2]/input"),
        "ai_secondary1_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[8]/td[3]/select"),
        "ai_secondary1_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[8]/td[4]/select"),
        "ai_secondary1_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[8]/td[5]/div[@class='mt-2']/div[2]/input"),

        "ai_secondary2_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[9]/td[1]/input"),
        "ai_secondary2_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[9]/td[2]/input"),
        "ai_secondary2_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[9]/td[3]/select"),
        "ai_secondary2_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[9]/td[4]/select"),
        "ai_secondary2_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[9]/td[5]/div[@class='mt-2']/div[2]/input"),

        "ai_secondary3_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[10]/td[1]/input"),
        "ai_secondary3_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[10]/td[2]/input"),
        "ai_secondary3_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[10]/td[3]/select"),
        "ai_secondary3_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[10]/td[4]/select"),
        "ai_secondary3_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[10]/td[5]/div[@class='mt-2']/div[2]/input"),

        "ai_secondary4_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[11]/td[1]/input"),
        "ai_secondary4_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[11]/td[2]/input"),
        "ai_secondary4_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[11]/td[3]/select"),
        "ai_secondary4_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[11]/td[4]/select"),
        "ai_secondary4_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[11]/td[5]/div[@class='mt-2']/div[2]/input"),

        "ai_secondary5_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[12]/td[1]/input"),
        "ai_secondary5_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[12]/td[2]/input"),
        "ai_secondary5_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[12]/td[3]/select"),
        "ai_secondary5_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[12]/td[4]/select"),
        "ai_secondary5_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[12]/td[5]/div[@class='mt-2']/div[2]/input"),
        "ai_secondary5_other":(By.XPATH,"//*[@id='AIQuestion2']/div[2]/table/tbody/tr[12]/td[4]/input"),

        "ai_secondary6_fname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[13]/td[1]/input"),
        "ai_secondary6_lname": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[13]/td[2]/input"),
        "ai_secondary6_select_relationshiptype": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[13]/td[3]/select"),
        "ai_secondary6_select_beneficiary_relationship": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[13]/td[4]/select"),
        "ai_secondary6_percentage": (By.XPATH, "//*[@id='AIQuestion2']//table/tbody/tr[13]/td[5]/div[@class='mt-2']/div[2]/input"),

        "enrollment_tab":(By.XPATH,"//span[text()='Enrollment']"),
        "apply_enrollment_filter":(By.XPATH,"//div/tab[2]/div[@class='container-fluid org-controls']//select"),
        "search_enrollment":(By.XPATH,"//tabset/div/tab[2]/div[1]//input"),
        "emp_fname_in_enrollment_table":(By.XPATH,"//tab[2]//table/tbody/tr[2]/td[1]/span"),
        "emp_lname_in_enrollment_table": (By.XPATH, "//tab[2]//table/tbody/tr[2]/td[2]/span"),
        "emp_ssn_in_enrollment_table": (By.XPATH, "//tab[2]/div[2]//table/tbody/tr[2]/td[3]"),
        "emp_status_in_enrollment_table": (By.XPATH, "//tab[2]/div[2]//table/tbody/tr[2]/td[4]"),

    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            )

    def verify_no_program_view(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_no_program_view'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_no_program_view'])
        link_2 = link_1.text
        link_3 = "You're all caught up!"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_prog_on_emp_dashboard(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_prog_on_dashboard'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_prog_on_dashboard'])
        link_2 = link_1.text
        link_3 = "Open Enrollment"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_access_prog(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_prog'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['access_prog'])))
        del wait
        self.find_element(*self.locator_dictionary['access_prog']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_access_prog_again(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_prog_again'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['access_prog_again'])))
        del wait
        self.find_element(*self.locator_dictionary['access_prog_again']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_prog_start_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_prog_first_page'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_prog_first_page'])
        link_2 = link_1.text
        link_3 = "Get Started"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def emp_access_prog_first_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_prog_first_page'])
        del page4
        self.find_element(*self.locator_dictionary['verify_prog_first_page']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_members_start_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_members_first_page'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_members_first_page'])
        link_2 = link_1.text
        link_3 = "Employee & Dependents"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def employee_access_start(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_members_first_page'])
        del page4
        self.find_element(*self.locator_dictionary['access_members_first_page']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_employee_and_dependents_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_employee_dependents_page'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_employee_dependents_page'])
        link_2 = link_1.text
        link_3 = "1 Employee and Dependents"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_already_filled_primary(self,fname,mname,lname,email):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['primary_fname'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['primary_fname'])
        link_2 = link_1.text
        link_3 = fname
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['primary_middle_name'])
        link_2 = link_1.text
        link_3 = mname
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['primary_last_name'])
        link_2 = link_1.text
        link_3 = lname
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['primary_ssn'])
        link_2 = link_1.text
        link_3 = link_2.contains("-1111")
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['primary_eamil'])
        link_2 = link_1.text
        link_3 = email
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def employee_update_primary_details(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['primary_fname'])
        del page4
        self.find_element(*self.locator_dictionary['primary_fname']).clear()
        self.find_element(*self.locator_dictionary['primary_fname']).send_keys("nainsi_enroll1")
        self.find_element(*self.locator_dictionary['primary_middle_name']).clear()
        self.find_element(*self.locator_dictionary['primary_middle_name']).send_keys("a")
        self.find_element(*self.locator_dictionary['primary_last_name']).clear()
        self.find_element(*self.locator_dictionary['primary_last_name']).send_keys("jain1")
        select_suffix = self.find_element(*self.locator_dictionary['primary_suffix'])
        select = Select(select_suffix)
        select.select_by_visible_text("Senior")
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['primary_dob']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        element = self.find_element(*self.locator_dictionary['choose_date1'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        select_gender = self.find_element(*self.locator_dictionary['primary_gender'])
        select = Select(select_gender)
        select.select_by_visible_text("Female")
        del select
        self.find_element(*self.locator_dictionary['primary_phone']).send_keys("1234567890")
        select_tobacco = self.find_element(*self.locator_dictionary['primary_tobacco'])
        select = Select(select_tobacco)
        select.select_by_visible_text("No")
        del select
        self.find_element(*self.locator_dictionary['primary_address1']).send_keys("7,rue de la")
        self.find_element(*self.locator_dictionary['primary_address2']).send_keys("Rotisseriel")
        self.find_element(*self.locator_dictionary['primary_city']).send_keys("Paris")
        select_state = self.find_element(*self.locator_dictionary['primary_state'])
        select = Select(select_state)
        select.select_by_visible_text("Florida")
        del select
        self.find_element(*self.locator_dictionary['primary_zip']).send_keys("11111")
        element = self.find_element(*self.locator_dictionary['primary_cancel'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        self.find_element(*self.locator_dictionary['primary_cancel']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['popup_yes_primary'])))
        del wait
        self.find_element(*self.locator_dictionary['popup_yes_primary']).click()
        time.sleep(2)
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        self.find_element(*self.locator_dictionary['primary_fname']).send_keys("nainsi_enroll1")
        self.find_element(*self.locator_dictionary['primary_middle_name']).send_keys("a")
        self.find_element(*self.locator_dictionary['primary_last_name']).send_keys("jain1")
        select_suffix = self.find_element(*self.locator_dictionary['primary_suffix'])
        select = Select(select_suffix)
        select.select_by_visible_text("Senior")
        del select
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['primary_dob']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        select_gender = self.find_element(*self.locator_dictionary['primary_gender'])
        select = Select(select_gender)
        select.select_by_visible_text("Female")
        del select
        self.find_element(*self.locator_dictionary['primary_phone']).send_keys("1234567890")
        select_tobacco = self.find_element(*self.locator_dictionary['primary_tobacco'])
        select = Select(select_tobacco)
        select.select_by_visible_text("No")
        del select
        self.find_element(*self.locator_dictionary['primary_address1']).send_keys("7,rue de la")
        self.find_element(*self.locator_dictionary['primary_address2']).send_keys("Rotisseriel")
        self.find_element(*self.locator_dictionary['primary_city']).send_keys("Paris")
        select_state = self.find_element(*self.locator_dictionary['primary_state'])
        select = Select(select_state)
        select.select_by_visible_text("Florida")
        del select
        self.find_element(*self.locator_dictionary['primary_zip']).send_keys("11111")
        self.find_element(*self.locator_dictionary['primary_update']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element

    def access_add_dependent(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['add_dependent_name'])
        del page4
        self.find_element(*self.locator_dictionary['add_dependent_name']).click()
        time.sleep(1)

    def verify_dependent_page(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent_page'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent_page'])
        link_2 = link_1.text
        link_3 = "DEPENDENT"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def add_dependent(self,relationship_name,dependent_fname,dependent_middle_name,dependent_last_name,dependent_suffix,dependent_email):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['primary_fname'])
        del page4
        self.find_element(*self.locator_dictionary['primary_fname']).send_keys(dependent_fname)
        self.find_element(*self.locator_dictionary['primary_middle_name']).send_keys(dependent_middle_name)
        self.find_element(*self.locator_dictionary['primary_last_name']).send_keys(dependent_last_name)
        select_suffix = self.find_element(*self.locator_dictionary['primary_suffix'])
        select = Select(select_suffix)
        select.select_by_visible_text(dependent_suffix)
        del select
        self.find_element(*self.locator_dictionary['primary_eamil']).send_keys(dependent_email)
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['primary_dob']).click()
        time.sleep(1)
        print("Click on Calendar")
        element = self.find_element(*self.locator_dictionary['choose_date1'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        try:
            ele = self.find_elements(*self.locator_dictionary['choose_date'])
            for ele1 in ele:
                if ele1.text == d:
                    print("enter in first if loop")
                    print(ele1.text)
                    ele1.click()
                    break
        except:
            ele = self.find_elements(*self.locator_dictionary['choose_date'])
            for ele1 in ele:
                if ele1.text == d:
                    print("enter in first if loop")
                    print(ele1.text)
                    ele1.click()
                    break

        select_gender = self.find_element(*self.locator_dictionary['primary_gender'])
        select = Select(select_gender)
        select.select_by_visible_text("Female")
        del select
        self.find_element(*self.locator_dictionary['primary_ssn']).send_keys("1111111111")
        self.find_element(*self.locator_dictionary['primary_phone']).send_keys("1234567890")

        select_relationship = self.find_element(*self.locator_dictionary['dependent_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text(relationship_name)
        del select
        select_tobacco = self.find_element(*self.locator_dictionary['primary_tobacco'])
        select = Select(select_tobacco)
        select.select_by_visible_text("No")
        del select
        element = self.find_element(*self.locator_dictionary['scroll_down_ele'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        self.find_element(*self.locator_dictionary['dependent_checkbox']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['dependent_checkbox']).click()
        self.find_element(*self.locator_dictionary['primary_address1']).clear()
        self.find_element(*self.locator_dictionary['primary_address1']).send_keys("7,rue de la1")
        self.find_element(*self.locator_dictionary['primary_address2']).clear()
        self.find_element(*self.locator_dictionary['primary_address2']).send_keys("Rotisseriel1")
        self.find_element(*self.locator_dictionary['primary_city']).clear()
        self.find_element(*self.locator_dictionary['primary_city']).send_keys("Paris1")
        select_state = self.find_element(*self.locator_dictionary['primary_state'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        self.find_element(*self.locator_dictionary['primary_zip']).clear()
        self.find_element(*self.locator_dictionary['primary_zip']).send_keys("11111")
        element = self.find_element(*self.locator_dictionary['dependent_add'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        self.find_element(*self.locator_dictionary['dependent_add']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element

    def click_cancel_yes_on_popup(self):
        element = self.find_element(*self.locator_dictionary['primary_cancel'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        self.find_element(*self.locator_dictionary['primary_cancel']).click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.visibility_of_element_located((self.locator_dictionary['popup_yes_primary'])))
        del wait
        self.find_element(*self.locator_dictionary['popup_yes_primary']).click()
        time.sleep(3)


    def emp_update_dependent(self,relationship_name,dependent_fname,dependent_middle_name,dependent_last_name,dependent_suffix,dependent_email):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['primary_fname'])
        del page4
        self.find_element(*self.locator_dictionary['primary_fname']).send_keys(dependent_fname)
        self.find_element(*self.locator_dictionary['primary_middle_name']).send_keys(dependent_middle_name)
        self.find_element(*self.locator_dictionary['primary_last_name']).send_keys(dependent_last_name)
        select_suffix = self.find_element(*self.locator_dictionary['primary_suffix'])
        select = Select(select_suffix)
        select.select_by_visible_text(dependent_suffix)
        del select
        self.find_element(*self.locator_dictionary['primary_eamil']).send_keys(dependent_email)
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['primary_dob']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        element = self.find_element(*self.locator_dictionary['choose_date1'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        select_gender = self.find_element(*self.locator_dictionary['primary_gender'])
        select = Select(select_gender)
        select.select_by_visible_text("Female")
        del select
        self.find_element(*self.locator_dictionary['primary_ssn']).send_keys("111111111")
        self.find_element(*self.locator_dictionary['primary_phone']).send_keys("1234567890")

        select_relationship = self.find_element(*self.locator_dictionary['dependent_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text(relationship_name)
        del select
        select_tobacco = self.find_element(*self.locator_dictionary['primary_tobacco'])
        select = Select(select_tobacco)
        select.select_by_visible_text("No")
        del select
        self.find_element(*self.locator_dictionary['dependent_checkbox']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['dependent_checkbox']).click()
        self.find_element(*self.locator_dictionary['primary_address1']).clear()
        self.find_element(*self.locator_dictionary['primary_address1']).send_keys("7,rue de la1")
        self.find_element(*self.locator_dictionary['primary_address2']).clear()
        self.find_element(*self.locator_dictionary['primary_address2']).send_keys("Rotisseriel1")
        self.find_element(*self.locator_dictionary['primary_city']).clear()
        self.find_element(*self.locator_dictionary['primary_city']).send_keys("Paris1")
        select_state = self.find_element(*self.locator_dictionary['primary_state'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        self.find_element(*self.locator_dictionary['primary_zip']).clear()
        self.find_element(*self.locator_dictionary['primary_zip']).send_keys("11111")
        self.find_element(*self.locator_dictionary['dependent_update']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element

    def emp_update_dependent1(self,relationship_name,dependent_fname,dependent_middle_name,dependent_last_name,dependent_suffix,dependent_email):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['primary_fname'])
        del page4
        self.find_element(*self.locator_dictionary['primary_fname']).clear()
        self.find_element(*self.locator_dictionary['primary_fname']).send_keys(dependent_fname)
        self.find_element(*self.locator_dictionary['primary_middle_name']).clear()
        self.find_element(*self.locator_dictionary['primary_middle_name']).send_keys(dependent_middle_name)
        self.find_element(*self.locator_dictionary['primary_last_name']).clear()
        self.find_element(*self.locator_dictionary['primary_last_name']).send_keys(dependent_last_name)
        select_suffix = self.find_element(*self.locator_dictionary['primary_suffix'])
        select = Select(select_suffix)
        select.select_by_visible_text(dependent_suffix)
        del select
        self.find_element(*self.locator_dictionary['primary_eamil']).clear()
        self.find_element(*self.locator_dictionary['primary_eamil']).send_keys(dependent_email)
        b = time.strftime("%d")
        print(b)
        if b[0] == "0":
            d = b.replace("0", "")
            print(d)
        else:
            d = b
        self.find_element(*self.locator_dictionary['primary_dob']).click()
        time.sleep(1)
        print("Click on Calendar")
        ele = self.find_elements(*self.locator_dictionary['choose_date'])
        element = self.find_element(*self.locator_dictionary['choose_date1'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        # ele = self.browser.find_elements(By.XPATH,"//table[@role='grid']/tbody//tr//td//span")
        print("get all the dates")
        for ele1 in ele:
            if ele1.text == d:
                print("enter in first if loop")
                print(ele1.text)
                ele1.click()
                break
        select_gender = self.find_element(*self.locator_dictionary['primary_gender'])
        select = Select(select_gender)
        select.select_by_visible_text("Female")
        del select
        self.find_element(*self.locator_dictionary['primary_ssn']).clear()
        self.find_element(*self.locator_dictionary['primary_ssn']).send_keys("2222222222")
        self.find_element(*self.locator_dictionary['primary_phone']).clear()
        self.find_element(*self.locator_dictionary['primary_phone']).send_keys("1234567890")

        select_relationship = self.find_element(*self.locator_dictionary['dependent_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text(relationship_name)
        del select
        select_tobacco = self.find_element(*self.locator_dictionary['primary_tobacco'])
        select = Select(select_tobacco)
        select.select_by_visible_text("No")
        del select
        self.find_element(*self.locator_dictionary['dependent_checkbox']).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary['dependent_checkbox']).click()
        self.find_element(*self.locator_dictionary['primary_address1']).clear()
        self.find_element(*self.locator_dictionary['primary_address1']).send_keys("7,rue de la1")
        self.find_element(*self.locator_dictionary['primary_address2']).clear()
        self.find_element(*self.locator_dictionary['primary_address2']).send_keys("Rotisseriel1")
        self.find_element(*self.locator_dictionary['primary_city']).clear()
        self.find_element(*self.locator_dictionary['primary_city']).send_keys("Paris1")
        select_state = self.find_element(*self.locator_dictionary['primary_state'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        self.find_element(*self.locator_dictionary['primary_zip']).clear()
        self.find_element(*self.locator_dictionary['primary_zip']).send_keys("11111")
        self.find_element(*self.locator_dictionary['dependent_update']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element

    def scroll_to_dob(self):
        element = self.find_element(*self.locator_dictionary['scroll_dob'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element

    def scroll_to_relationship(self):
        element = self.find_element(*self.locator_dictionary['primary_eamil'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element

    def remove_dependent(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['remove_dependent'])
        del page4
        self.find_element(*self.locator_dictionary['remove_dependent']).click()
        self.find_element(*self.locator_dictionary['yes_remove']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_access_save_continue(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_continue'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['save_and_continue'])))
        del wait
        self.find_element(*self.locator_dictionary['save_and_continue']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_medical_start_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['medical_start_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['medical_start_screen'])
        link_2 = link_1.text
        link_3 = "Medical Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def choose_no_on_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_medical'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_medical']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_second_question_on_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['next_button'])
        del page4
        self.find_element(*self.locator_dictionary['next_button']).click()
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['second_qu_on_medical'])
        del page4
        link = self.find_element(*self.locator_dictionary['second_qu_on_medical'])
        link_1 = link.text
        link_2 = link_1.replace("b.","").strip()
        print(link_2)
        link_3 = "Why are you waiving medical insurance coverage?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_second_question_on_medical1(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['second_qu_on_medical_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['second_qu_on_medical_yes'])
        link_1 = link.text
        link_2 = link_1.replace("b.","").strip()
        print(link_2)
        link_3 = "Who will be include in your medical plan?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_third_question_on_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['next_button'])
        del page4
        self.find_element(*self.locator_dictionary['next_button']).click()
        # try:
        #     if(self.find_element(*self.locator_dictionary['medical_more_info']).is_displayed()):
        #         print("more info is displaying")
        # except:
        #     self.find_element(*self.locator_dictionary['next_button']).click()
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['third_qu_on_medical_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['third_qu_on_medical_yes'])
        link_1 = link.text
        link_2 = link_1.replace("c.","").strip()
        print(link_2)
        link_3 = "Which plan would you like to enroll in?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_fourth_question_on_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['next_button'])
        del page4
        self.find_element(*self.locator_dictionary['next_button']).click()
        time.sleep(1)

        ############Please remove this line when scroll code is pushed#######################
        self.find_element(*self.locator_dictionary['next_button']).click()
        # try:
        #     if(self.find_element(*self.locator_dictionary['mi_enter_dependent6_fname_pcp']).is_displayed()):
        #         print("primary pcp is displaying")
        # except:
        #     print("primary pcp is not displaying")
        #     self.find_element(*self.locator_dictionary['next_button']).click()
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fourth_qu_on_medical_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['fourth_qu_on_medical_yes'])
        link_1 = link.text
        link_2 = link_1.replace("d.","").strip()
        print(link_2)
        link_3 = "Who are your primary care physicians?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3



    def hit_save_and_continue_again_come_back_on_medical(self):
        # page4 = BasePage(self)
        # page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_continue'])
        # del page4
        # self.find_element(*self.locator_dictionary['save_and_continue']).click()
        # wait = WebDriverWait(self.browser, 15)
        # wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        # del wait
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['step_2'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        self.find_element(*self.locator_dictionary['step_2']).click()
        time.sleep(1)


    def emp_choose_option_on_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['waiving_mi'])
        del page4
        select_mi_waiving = self.find_element(*self.locator_dictionary['waiving_mi'])
        select = Select(select_mi_waiving)
        select.select_by_visible_text("I am covered as a spouse or dependent under another group Medical plan")
        del select

    def verify_selected_option_on_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['waiving_mi1'])
        del page4
        select_mi_waiving = self.find_element(*self.locator_dictionary['waiving_mi1'])
        select2 = select_mi_waiving.text
        select3 = "I am covered as a spouse or dependent under another group Medical plan"
        assert select2 == select3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(select2, select3)
        del select2,select3

    def emp_choose_other_on_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['waiving_mi'])
        del page4
        select_mi_waiving = self.find_element(*self.locator_dictionary['waiving_mi'])
        select = Select(select_mi_waiving)
        select.select_by_visible_text("Other")
        del select

    def emp_fill_valid_data_in_other_for_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['other_reason'])
        del page4
        self.find_element(*self.locator_dictionary['other_reason']).send_keys("Not interested in this type of insurance.")

    def verify_other_data_for_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['other_reason'])
        del page4
        link_2 = self.browser.execute_script("return (document.getElementById('reason').value)")
        print(str(link_2))
        link_3 = "Not interested in this type of insurance."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_2
        del link_3

    def verify_dental_first_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['dental_start_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['dental_start_screen'])
        link_2 = link_1.text
        link_3 = "Dental Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_access_start_on_medical_first_screen(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['start_on_medical'])
        del page4
        self.find_element(*self.locator_dictionary['start_on_medical']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_medical_2_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_medical_2_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_medical_2_screen'])
        link_2 = link_1.text
        link_3 = "2 Medical Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_access_start_on_dental_first_screen(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['start_on_dental'])
        del page4
        self.find_element(*self.locator_dictionary['start_on_dental']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_dental_2_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dental_2_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dental_2_screen'])
        link_2 = link_1.text
        link_3 = "3 Dental Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def choose_no_on_dental(self):
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_dental'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_dental']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def hit_save_and_continue_again_come_back_on_dental(self):
        # page4 = BasePage(self)
        # page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_continue'])
        # del page4
        # self.find_element(*self.locator_dictionary['save_and_continue']).click()
        # wait = WebDriverWait(self.browser, 15)
        # wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        # del wait
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['step_3'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        self.find_element(*self.locator_dictionary['step_3']).click()
        time.sleep(1)

    def verify_no_option_on_dental(self):
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_dental'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_dental']).is_selected()
        return True

    def verify_vision_first_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['vision_start_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['vision_start_screen'])
        link_2 = link_1.text
        link_3 = "Vision Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_access_start_on_vision_first_screen(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['start_on_vision'])
        del page4
        self.find_element(*self.locator_dictionary['start_on_vision']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_vision_2_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_vision_2_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_vision_2_screen'])
        link_2 = link_1.text
        link_3 = "4 Vision Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def choose_no_on_vision(self):
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_vision'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_vision']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def hit_save_and_continue_again_come_back_on_vision(self):
        # page4 = BasePage(self)
        # page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_continue'])
        # del page4
        # self.find_element(*self.locator_dictionary['save_and_continue']).click()
        # wait = WebDriverWait(self.browser, 15)
        # wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        # del wait
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['step_4'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        self.find_element(*self.locator_dictionary['step_4']).click()
        time.sleep(1)

    def hit_save_and_continue_again_come_back_on_vision1(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_continue'])
        del page4
        self.find_element(*self.locator_dictionary['save_and_continue']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['step_4'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        self.find_element(*self.locator_dictionary['step_4']).click()
        time.sleep(1)

    def verify_no_option_on_vision(self):
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_vision'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_vision']).is_selected()
        return True

    def verify_ancillary_first_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['ancillary_start_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['ancillary_start_screen'])
        link_2 = link_1.text
        link_3 = "Ancillary Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_access_start_on_ancillary_first_screen(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['start_on_ancillary'])
        del page4
        self.find_element(*self.locator_dictionary['start_on_ancillary']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_ancillary_2_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_ancillary_2_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_ancillary_2_screen'])
        link_2 = link_1.text
        link_3 = "5 Ancillary Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def choose_no_on_ancillary(self):
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_ancillary'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_ancillary']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def hit_save_and_continue_again_come_back_on_ancillary(self):
        # page4 = BasePage(self)
        # page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_continue'])
        # del page4
        # self.find_element(*self.locator_dictionary['save_and_continue']).click()
        # wait = WebDriverWait(self.browser, 15)
        # wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        # del wait
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['step_5'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        time.sleep(1)
        self.find_element(*self.locator_dictionary['step_5']).click()
        time.sleep(1)

    def verify_no_option_on_ancillary(self):
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_ancillary'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_ancillary']).is_selected()
        return True

    def verify_fsa_first_screen(self):
        try:
            if(self.find_element(*self.locator_dictionary['fsa_start_screen']).is_displayed()):
                print("fsa start screen is not blank")
            else:
                self.emp_access_save_continue()
                self.hit_save_and_continue_again_come_back_on_fsa()
        except:
            print("fsa screen is visible")
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fsa_start_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['fsa_start_screen'])
        link_2 = link_1.text
        link_3 = "Flexible Spending Accounts"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_access_start_on_fsa_first_screen(self):
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['start_on_fsa'])
        del page4
        self.find_element(*self.locator_dictionary['start_on_fsa']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_fsa_2_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_fsa_2_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_fsa_2_screen'])
        link_2 = link_1.text
        link_3 = "6 Flexible Spending Account"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def choose_no_on_fsa(self):
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_fsa'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_fsa']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def hit_save_and_continue_again_come_back_on_fsa(self):
        # page4 = BasePage(self)
        # page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_continue'])
        # del page4
        # self.find_element(*self.locator_dictionary['save_and_continue']).click()
        # wait = WebDriverWait(self.browser, 15)
        # wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        # del wai
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['step_6'])
        del page4
        self.find_element(*self.locator_dictionary['step_6']).click()
        time.sleep(1)

    def verify_no_option_on_fsa(self):
        element = self.find_element(*self.locator_dictionary['header_scroll'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_no_fsa'])
        del page4
        self.find_element(*self.locator_dictionary['choose_no_fsa']).is_selected()
        return True

    def verify_review_and_submit_screen(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_review_and_submit_screen'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_review_and_submit_screen'])
        link_2 = link_1.text
        link_3 = "Review and Submit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_primary_on_review_screen(self):
        element = self.find_element(*self.locator_dictionary['scroll_to_members'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_primary_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_primary_name'])
        link_2 = link_1.text
        link_3 = "nainsi_enroll1 jain1"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def get_shadow_root_elements(self,element):
        ele = self.browser.execute_script("return arguments[0].shadowRoot",element)
        print(ele)
        return ele

    # def verify_primary_details_on_review_screen(self):
    #     link_2 = self.browser.execute_script("return (document.querySelector('#review_enroll  input').value)")
    #     if not(link_2):
    #         print("element is null")
    #     else:
    #         print("element is not null")
    #     print(link_2)
    #     # link_2 = link_1.text
    #     print(link_2)
    #     link_3 = "nainsi_enroll1"
    #     assert link_2 == link_3, "Visible text is not as expected." \
    #                              " Actual: {}, Expected: {}".format(link_2, link_3)
    #     del link_2
    #     del link_3

    def verify_primary_details_on_review_screen(self,index_number,expected_text):

        link_2 = self.browser.execute_script("return (document.querySelectorAll('input')["+str(index_number)+"].value)")
        print(str(link_2))
        link_3 = expected_text
        assert link_2 == link_3, "Visible text is not as expected." \
                                     " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_2
        del link_3

        # link_2 = self.browser.execute_script("return ($x('//*[@id='review_enroll']/form/div/div[2]/div[2]/input')[0].value)")
        # print(str(link_2))
        # link_3 = expected_text
        # assert link_2 == link_3, "Visible text is not as expected." \
        #                          " Actual: {}, Expected: {}".format(link_2, link_3)
        # del link_2
        # del link_3

    def verify_primary_details_on_review_screen1(self,index_number,expected_text):
        element = self.find_element(*self.locator_dictionary['label_fname'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        link_2 = self.browser.execute_script(
            "return (document.getElementsByClassName('input-review')[" + str(index_number) + "].value)")
        print(str(link_2))
        link_3 = expected_text
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_2
        del link_3



    def verify_primary_suffix_on_review_screen(self,index_number,expected_text):
        link_2 = self.browser.execute_script(
            "return (document.querySelectorAll('input.input-review')[" + str(index_number) + "].value)")
        print(str(link_2))
        link_3 = expected_text
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_2
        del link_3


        del link_3

    def verify_first_dependent_on_review_screen(self, expected_first_dependent_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_first_dependent_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_first_dependent_name'])
        link_2 = link_1.text
        link_3 = expected_first_dependent_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def access_first_dependent_on_review(self):
        element = self.find_element(*self.locator_dictionary['review_header'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_first_dependent_on_review'])
        del page4
        self.find_element(*self.locator_dictionary['access_first_dependent_on_review']).click()
        time.sleep(1)
        element = self.find_element(*self.locator_dictionary['label_fname'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)


    def verify_second_dependent_on_review_screen(self, expected_second_dependent_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_second_dependent_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_second_dependent_name'])
        link_2 = link_1.text
        link_3 = expected_second_dependent_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def access_second_dependent_on_review(self):
        element = self.find_element(*self.locator_dictionary['review_header'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_second_dependent_on_review'])
        del page4
        self.find_element(*self.locator_dictionary['access_second_dependent_on_review']).click()
        time.sleep(1)
        element = self.find_element(*self.locator_dictionary['label_fname'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)

    def verify_third_dependent_on_review_screen(self, expected_third_dependent_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_third_dependent_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_third_dependent_name'])
        link_2 = link_1.text
        link_3 = expected_third_dependent_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def access_third_dependent_on_review(self):
        element = self.find_element(*self.locator_dictionary['review_header'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_third_dependent_on_review'])
        del page4
        self.find_element(*self.locator_dictionary['access_third_dependent_on_review']).click()
        time.sleep(1)
        element = self.find_element(*self.locator_dictionary['label_fname'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)

    def verify_fourth_dependent_on_review_screen(self, expected_fourth_dependent_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_fourth_dependent_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_fourth_dependent_name'])
        link_2 = link_1.text
        link_3 = expected_fourth_dependent_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def access_fourth_dependent_on_review(self):
        element = self.find_element(*self.locator_dictionary['review_header'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_fourth_dependent_on_review'])
        del page4
        self.find_element(*self.locator_dictionary['access_fourth_dependent_on_review']).click()
        time.sleep(1)
        element = self.find_element(*self.locator_dictionary['label_fname'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)

    def verify_fifth_dependent_on_review_screen(self, expected_fifth_dependent_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_fifth_dependent_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_fifth_dependent_name'])
        link_2 = link_1.text
        link_3 = expected_fifth_dependent_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def access_fifth_dependent_on_review(self):
        element = self.find_element(*self.locator_dictionary['review_header'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_fifth_dependent_on_review'])
        del page4
        self.find_element(*self.locator_dictionary['access_fifth_dependent_on_review']).click()
        time.sleep(1)
        element = self.find_element(*self.locator_dictionary['label_fname'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)

    def verify_sixth_dependent_on_review_screen(self, expected_sixth_dependent_name):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_sixth_dependent_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_sixth_dependent_name'])
        link_2 = link_1.text
        link_3 = expected_sixth_dependent_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def access_sixth_dependent_on_review(self):
        element = self.find_element(*self.locator_dictionary['review_header'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['access_sixth_dependent_on_review'])
        del page4
        self.find_element(*self.locator_dictionary['access_sixth_dependent_on_review']).click()
        time.sleep(1)
        element = self.find_element(*self.locator_dictionary['label_fname'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        time.sleep(1)


    def verify_medical_no_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_no_on_review_for_medical'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_no_on_review_for_medical'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_no_on_review_for_medical'])
        link_2 = link_1.text
        link_3 = "Not interested in this type of insurance."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_medical_heading_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_medical_heading_on_review'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_medical_heading_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_medical_heading_on_review'])
        link_2 = link_1.text
        link_3 = "Medical Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_dental_no_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_no_on_review_for_dental'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_no_on_review_for_dental'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_no_on_review_for_dental'])
        link_2 = link_1.text
        link_3 = "You have waived the coverage for this beanefit offering"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_dental_heading_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_dental_heading_on_review'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dental_heading_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dental_heading_on_review'])
        link_2 = link_1.text
        link_3 = "Dental Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_vision_no_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_no_on_review_for_vision'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_no_on_review_for_vision'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_no_on_review_for_vision'])
        link_2 = link_1.text
        link_3 = "You have waived the coverage for this beanefit offering"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_vision_heading_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_vision_heading_on_review'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_vision_heading_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_vision_heading_on_review'])
        link_2 = link_1.text
        link_3 = "Vision Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_ancillary_no_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_no_on_review_for_ancillary'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_no_on_review_for_ancillary'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_no_on_review_for_ancillary'])
        link_2 = link_1.text
        link_3 = "You have waived the coverage for this beanefit offering"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_ancillary_heading_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_ancillary_heading_on_review'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_ancillary_heading_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_ancillary_heading_on_review'])
        link_2 = link_1.text
        link_3 = "Ancillary Insurance"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3


    def verify_fsa_no_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_no_on_review_for_fsa'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_no_on_review_for_fsa'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_no_on_review_for_fsa'])
        link_2 = link_1.text
        link_3 = "You have waived the coverage for this beanefit offering"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_fsa_heading_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_fsa_heading_on_review'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_fsa_heading_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_fsa_heading_on_review'])
        link_2 = link_1.text
        link_3 = "Flexible Spending Accounts"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_access_save_and_close(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_close'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['save_and_close'])))
        del wait
        self.find_element(*self.locator_dictionary['save_and_close']).click()
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_emp_dashboard(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_emp_dashboard'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_emp_dashboard'])
        link_2 = link_1.text
        link_3 = "Your Tasks"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def choose_yes_on_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_yes_medical'])
        del page4
        self.find_element(*self.locator_dictionary['choose_yes_medical']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_heading_third_qu_medical(self,heading_showing_plans_for):
        element = self.find_element(*self.locator_dictionary['second_qu_on_medical_yes'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_emp_heading_third_qu_medical'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_emp_heading_third_qu_medical'])
        link_2 = link_1.text
        link_3 = heading_showing_plans_for
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_select_first_dependent(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_first_dependent'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_first_dependent']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_second_dependent(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_second_dependent'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_second_dependent']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_third_dependent(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_third_dependent'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_third_dependent']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_fourth_dependent(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_fourth_dependent'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_fourth_dependent']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_fifth_dependent(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_fifth_dependent'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_fifth_dependent']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_sixth_dependent(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_sixth_dependent'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_sixth_dependent']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_medical_plan_details(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['medical_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['medical_plan_name'])
        link_2 = link_1.text
        link_3 = "medical_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_plan_cost_per_pay_period'])
        link_2 = link_1.text
        link_3 = "$ 50"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_plan_co_pay'])
        link_2 = link_1.text
        link_3 = "nainsi1"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_plan_rx_cost'])
        link_2 = link_1.text
        link_3 = "nainsi3"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_plan_deductible'])
        link_2 = link_1.text
        link_3 = "nainsi2"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def emp_access_more_info(self):
        # element = self.find_element(*self.locator_dictionary['third_qu_on_medical_yes'])
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        # del element
        try:
            if(self.find_element(*self.locator_dictionary['fourth_qu_on_medical_yes']).is_displayed()):
                print("more info link is displaying")
            else:
                element = self.find_element(*self.locator_dictionary['third_qu_on_medical_yes'])
                self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
                del element
        except:
            print("medical more info link is not displaying")
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['medical_more_info'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['medical_more_info'])))
        del wait
        self.find_element(*self.locator_dictionary['medical_more_info']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_plan_more_info_details(self,benefit_name,benefit_heading,cost_per_pay_period):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['medical_more_info_benefit_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_benefit_name'])
        link_2 = link_1.text
        link_3 = benefit_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_benefit_heading'])
        link_2 = link_1.text
        link_3 = benefit_heading
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_cost_per_pay_period'])
        link_2 = link_1.text
        link_3 = cost_per_pay_period
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_plan_info'])
        link_2 = link_1.text
        link_3 = "Hey! Creating new Benefit.Please check to enroll in it."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_quick_links'])
        link_2 = link_1.text
        link_3 = "benemax"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_document_link'])
        link_2 = link_1.text
        link_3 = "benemax_doc"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def close_more_info_popup(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['plan_more_info_close_modal'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['plan_more_info_close_modal'])))
        del wait
        self.find_element(*self.locator_dictionary['plan_more_info_close_modal']).click()
        time.sleep(2)
        # wait = WebDriverWait(self.browser, 15)
        # wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        # del wait

    def emp_choose_medical_plan(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_medical_plan'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['choose_medical_plan'])))
        del wait
        self.find_element(*self.locator_dictionary['choose_medical_plan']).click()
        time.sleep(1)
        try:
            if(self.find_element(*self.locator_dictionary['medical_fsa_cancel_on_alert']).is_displayed()):
                self.find_element(*self.locator_dictionary['medical_fsa_cancel_on_alert']).click()
                time.sleep(1)
                # self.find_element(*self.locator_dictionary['choose_medical_plan']).click()
                # time.sleep(1)
        except:
            print("alert to clear fsa is not displaying")



    def emp_choose_ancillary_plan(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['previous_button'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['previous_button'])))
        del wait
        self.find_element(*self.locator_dictionary['previous_button']).click()
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_ancillary_plan'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['choose_ancillary_plan'])))
        del wait
        self.find_element(*self.locator_dictionary['choose_ancillary_plan']).click()
        time.sleep(1)

    def verify_first_primary_pcp_heading_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_verify_primary_heading_pcp'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['mi_verify_primary_heading_pcp'])
        link_2 = link_1.text
        link_2 = link_1.text
        link_3 = "nainsi_enroll1 jain1"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_first_dependent_pcp_heading_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_verify_dependent1_heading_pcp'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['mi_verify_dependent1_heading_pcp'])
        link_2 = link_1.text
        link_3 = "nainsi_enroll2 jain2"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_second_dependent_pcp_heading_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_verify_dependent2_heading_pcp'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['mi_verify_dependent2_heading_pcp'])
        link_2 = link_1.text
        link_3 = "nainsi_enroll3 jain3"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_third_dependent_pcp_heading_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_verify_dependent3_heading_pcp'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['mi_verify_dependent3_heading_pcp'])
        link_2 = link_1.text
        link_3 = "nainsi_enroll4 jain4"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_fourth_dependent_pcp_heading_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_verify_dependent4_heading_pcp'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['mi_verify_dependent4_heading_pcp'])
        link_2 = link_1.text
        link_3 = "nainsi_enroll6 jain6"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_fifth_dependent_pcp_heading_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_verify_dependent5_heading_pcp'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['mi_verify_dependent5_heading_pcp'])
        link_2 = link_1.text
        link_3 = "nainsi_enroll7 jain7"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_sixth_dependent_pcp_heading_medical(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_verify_dependent6_heading_pcp'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['mi_verify_dependent6_heading_pcp'])
        link_2 = link_1.text
        link_3 = "nainsi_enroll5 jain5"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def emp_add_first_pcp_medical(self):
        element = self.find_element(*self.locator_dictionary['mi_verify_primary_heading_pcp'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_enter_primary_fname_pcp'])
        del page4
        self.find_element(*self.locator_dictionary['mi_enter_primary_fname_pcp']).send_keys("nainsi1")
        self.find_element(*self.locator_dictionary['mi_enter_primary_lname_pcp']).send_keys("jain1")
        self.find_element(*self.locator_dictionary['mi_enter_primary_pcpid_pcp']).send_keys("123456")
        self.find_element(*self.locator_dictionary['mi_enter_primary_city_pcp']).send_keys("California")
        select_state = self.find_element(*self.locator_dictionary['mi_enter_primary_state_pcp'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        # select_state = self.browser.execute_script("return (document.getElementById('medical_insurance').getElementsByClassName('org-select')[0])")
        # select = Select(select_state)
        # select.select_by_value("5")
        # del select
        self.find_element(*self.locator_dictionary['mi_enter_primary_zip_pcp']).send_keys("11111")

    def emp_add_first_dependent1_pcp_medical(self):
        element = self.find_element(*self.locator_dictionary['mi_verify_dependent1_heading_pcp'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_enter_dependent1_fname_pcp'])
        del page4
        self.find_element(*self.locator_dictionary['mi_enter_dependent1_fname_pcp']).send_keys("nainsi2")
        self.find_element(*self.locator_dictionary['mi_enter_dependent1_lname_pcp']).send_keys("jain2")
        self.find_element(*self.locator_dictionary['mi_enter_dependent1_pcpid_pcp']).send_keys("123456")
        self.find_element(*self.locator_dictionary['mi_enter_dependent1_city_pcp']).send_keys("California")
        select_state = self.find_element(*self.locator_dictionary['mi_enter_dependent1_state_pcp'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        # select_state = self.browser.execute_script("return (document.getElementById('medical_insurance').getElementsByClassName('org-select')[1])")
        # select = Select(select_state)
        # select.select_by_value("5")
        # del select
        self.find_element(*self.locator_dictionary['mi_enter_dependent1_zip_pcp']).send_keys("11111")

    def emp_add_first_dependent2_pcp_medical(self):
        element = self.find_element(*self.locator_dictionary['mi_verify_dependent2_heading_pcp'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_enter_dependent2_fname_pcp'])
        del page4
        self.find_element(*self.locator_dictionary['mi_enter_dependent2_fname_pcp']).send_keys("nainsi3")
        self.find_element(*self.locator_dictionary['mi_enter_dependent2_lname_pcp']).send_keys("jain3")
        self.find_element(*self.locator_dictionary['mi_enter_dependent2_pcpid_pcp']).send_keys("123456")
        self.find_element(*self.locator_dictionary['mi_enter_dependent2_city_pcp']).send_keys("California")
        select_state = self.find_element(*self.locator_dictionary['mi_enter_dependent2_state_pcp'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        # select_state = self.browser.execute_script("return (document.getElementById('medical_insurance').getElementsByClassName('org-select')[2])")
        # select = Select(select_state)
        # select.select_by_value("5")
        # del select
        self.find_element(*self.locator_dictionary['mi_enter_dependent2_zip_pcp']).send_keys("11111")

    def emp_add_first_dependent3_pcp_medical(self):
        element = self.find_element(*self.locator_dictionary['mi_verify_dependent3_heading_pcp'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_enter_dependent3_fname_pcp'])
        del page4
        self.find_element(*self.locator_dictionary['mi_enter_dependent3_fname_pcp']).send_keys("nainsi4")
        self.find_element(*self.locator_dictionary['mi_enter_dependent3_lname_pcp']).send_keys("jain4")
        self.find_element(*self.locator_dictionary['mi_enter_dependent3_pcpid_pcp']).send_keys("123456")
        self.find_element(*self.locator_dictionary['mi_enter_dependent3_city_pcp']).send_keys("California")
        select_state = self.find_element(*self.locator_dictionary['mi_enter_dependent3_state_pcp'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        # select_state =self.browser.execute_script("return (document.getElementById('medical_insurance').getElementsByClassName('org-select')[3])")
        # select = Select(select_state)
        # select.select_by_value("5")
        # del select
        self.find_element(*self.locator_dictionary['mi_enter_dependent3_zip_pcp']).send_keys("11111")

    def emp_add_first_dependent4_pcp_medical(self):
        element = self.find_element(*self.locator_dictionary['mi_verify_dependent4_heading_pcp'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_enter_dependent4_fname_pcp'])
        del page4
        self.find_element(*self.locator_dictionary['mi_enter_dependent4_fname_pcp']).send_keys("nainsi5")
        self.find_element(*self.locator_dictionary['mi_enter_dependent4_lname_pcp']).send_keys("jain5")
        self.find_element(*self.locator_dictionary['mi_enter_dependent4_pcpid_pcp']).send_keys("123456")
        self.find_element(*self.locator_dictionary['mi_enter_dependent4_city_pcp']).send_keys("California")
        select_state = self.find_element(*self.locator_dictionary['mi_enter_dependent4_state_pcp'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        # select_state =self.browser.execute_script("return (document.getElementById('medical_insurance').getElementsByClassName('org-select')[4])")
        # select = Select(select_state)
        # select.select_by_value("5")
        # del select
        self.find_element(*self.locator_dictionary['mi_enter_dependent4_zip_pcp']).send_keys("11111")

    def emp_add_first_dependent5_pcp_medical(self):
        element = self.find_element(*self.locator_dictionary['mi_verify_dependent5_heading_pcp'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_enter_dependent5_fname_pcp'])
        del page4
        self.find_element(*self.locator_dictionary['mi_enter_dependent5_fname_pcp']).send_keys("nainsi6")
        self.find_element(*self.locator_dictionary['mi_enter_dependent5_lname_pcp']).send_keys("jain6")
        self.find_element(*self.locator_dictionary['mi_enter_dependent5_pcpid_pcp']).send_keys("123456")
        self.find_element(*self.locator_dictionary['mi_enter_dependent5_city_pcp']).send_keys("California")
        select_state = self.find_element(*self.locator_dictionary['mi_enter_dependent5_state_pcp'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        # select_state =self.browser.execute_script("return (document.getElementById('medical_insurance').getElementsByClassName('org-select')[5])")
        # select = Select(select_state)
        # select.select_by_value("5")
        # del select
        self.find_element(*self.locator_dictionary['mi_enter_dependent5_zip_pcp']).send_keys("11111")

    def emp_add_first_dependent6_pcp_medical(self):
        element = self.find_element(*self.locator_dictionary['mi_verify_dependent6_heading_pcp'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['mi_enter_dependent6_fname_pcp'])
        del page4
        self.find_element(*self.locator_dictionary['mi_enter_dependent6_fname_pcp']).send_keys("nainsi7")
        self.find_element(*self.locator_dictionary['mi_enter_dependent6_lname_pcp']).send_keys("jain7")
        self.find_element(*self.locator_dictionary['mi_enter_dependent6_pcpid_pcp']).send_keys("123456")
        self.find_element(*self.locator_dictionary['mi_enter_dependent6_city_pcp']).send_keys("California")
        select_state = self.find_element(*self.locator_dictionary['mi_enter_dependent6_state_pcp'])
        select = Select(select_state)
        select.select_by_visible_text("California")
        del select
        # select_state =self.browser.execute_script("return (document.getElementById('medical_insurance').getElementsByClassName('org-select')[6].value=5)")
        # select = Select(select_state)
        # select.select_by_value("5")
        # del select
        self.find_element(*self.locator_dictionary['mi_enter_dependent6_zip_pcp']).send_keys("11111")

    def choose_yes_on_dental(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_yes_dental'])
        del page4
        self.find_element(*self.locator_dictionary['choose_yes_dental']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_second_question_on_dental1(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['second_qu_on_dental_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['second_qu_on_dental_yes'])
        link_1 = link.text
        link_2 = link_1.replace("b.","").strip()
        print(link_2)
        link_3 = "Who will be include in your Dental Insurance plan?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_heading_third_qu_dental(self,heading_showing_plans_for):
        element = self.find_element(*self.locator_dictionary['second_qu_on_dental_yes'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_emp_heading_third_qu_dental'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_emp_heading_third_qu_dental'])
        link_2 = link_1.text
        link_3 = heading_showing_plans_for
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_select_first_dependent_di(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_first_dependent_di'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_first_dependent_di']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_second_dependent_di(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_second_dependent_di'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_second_dependent_di']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_third_dependent_di(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_third_dependent_di'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_third_dependent_di']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_fourth_dependent_di(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_fourth_dependent_di'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_fourth_dependent_di']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_fifth_dependent_di(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_fifth_dependent_di'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_fifth_dependent_di']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_sixth_dependent_di(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_sixth_dependent_di'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_sixth_dependent_di']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_third_question_on_dental(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['next_button1'])
        del page4
        self.find_element(*self.locator_dictionary['next_button1']).click()
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['third_qu_on_dental_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['third_qu_on_dental_yes'])
        link_1 = link.text
        link_2 = link_1.replace("c.","").strip()
        print(link_2)
        link_3 = "Which plan would you like to enroll in?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_dental_plan_details(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['dental_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['dental_plan_name'])
        link_2 = link_1.text
        link_3 = "dental_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['dental_plan_cost_per_pay_period'])
        link_2 = link_1.text
        link_3 = "$ 50"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['dental_your_health_plans'])
        link_2 = link_1.text
        link_3 = "Hey! Creating new Benefit.Please check to enroll in it."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def emp_access_more_info_dental(self):
        element = self.find_element(*self.locator_dictionary['third_qu_on_dental_yes'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['dental_more_info'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['dental_more_info'])))
        del wait
        self.find_element(*self.locator_dictionary['dental_more_info']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def choose_yes_on_vision(self):
        try:
            if(self.find_element(*self.locator_dictionary['choose_yes_vision']).is_displayed()):
                print("screen is not blank")
            else:
                self.emp_access_save_continue()
                self.emp_access_start_on_ancillary_first_screen()
                self.emp_access_save_continue()
                # self.emp_access_start_on_fsa_first_screen()
                # self.emp_access_save_continue()
                self.hit_save_and_continue_again_come_back_on_vision()
        except:
            print("vision screen is visible")

        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_yes_vision'])
        del page4
        self.find_element(*self.locator_dictionary['choose_yes_vision']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_second_question_on_vision1(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['second_qu_on_vision_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['second_qu_on_vision_yes'])
        link_1 = link.text
        link_2 = link_1.replace("b.","").strip()
        print(link_2)
        link_3 = "Who will be include in your Vision Insurance plan?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_heading_third_qu_vision(self,heading_showing_plans_for):
        element = self.find_element(*self.locator_dictionary['second_qu_on_vision_yes'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_emp_heading_third_qu_vision'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_emp_heading_third_qu_vision'])
        link_2 = link_1.text
        link_3 = heading_showing_plans_for
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_select_first_dependent_vi(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_first_dependent_vi'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_first_dependent_vi']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_second_dependent_vi(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_second_dependent_vi'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_second_dependent_vi']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_select_third_dependent_vi(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_select_third_dependent_vi'])
        del page4
        self.find_element(*self.locator_dictionary['emp_select_third_dependent_vi']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait


    def verify_third_question_on_vision(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['next_button1'])
        del page4
        self.find_element(*self.locator_dictionary['next_button1']).click()
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['third_qu_on_vision_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['third_qu_on_vision_yes'])
        link_1 = link.text
        link_2 = link_1.replace("c.","").strip()
        print(link_2)
        link_3 = "Which plan would you like to enroll in?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_vision_plan_details(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['vision_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['vision_plan_name'])
        link_2 = link_1.text
        link_3 = "vision_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['vision_plan_cost_per_pay_period'])
        link_2 = link_1.text
        link_3 = "$ 40"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['vision_your_health_plans'])
        link_2 = link_1.text
        link_3 = "Hey! Creating new Benefit.Please check to enroll in it."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def emp_access_more_info_vision(self):
        element = self.find_element(*self.locator_dictionary['third_qu_on_vision_yes'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['vision_more_info'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['vision_more_info'])))
        del wait
        self.find_element(*self.locator_dictionary['vision_more_info']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def choose_yes_on_ancillary(self):
        try:
            if (self.find_element(*self.locator_dictionary['choose_yes_ancillary']).is_displayed()):
                print("screen is not blank for ancillary")
            else:
                # self.emp_access_save_continue()
                # self.emp_access_start_on_fsa_first_screen()
                self.emp_access_save_continue()
                self.hit_save_and_continue_again_come_back_on_ancillary()
        except:
            print("ancillary screen is visible")
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_yes_ancillary'])
        del page4
        self.find_element(*self.locator_dictionary['choose_yes_ancillary']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_second_question_on_ancillary1(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['second_qu_on_ancillary_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['second_qu_on_ancillary_yes'])
        link_1 = link.text
        link_2 = link_1.replace("b.","").strip()
        print(link_2)
        link_3 = "Which plan would you like to enroll in?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_ancillary_plan_details(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['ancillary_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['ancillary_plan_name'])
        link_2 = link_1.text
        link_3 = "ancillary_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['ancillary_your_health_plans'])
        link_2 = link_1.text
        link_3 = "Hey! Creating new Benefit.Please check to enroll in it."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def emp_access_more_info_ancillary(self):
        element = self.find_element(*self.locator_dictionary['second_qu_on_ancillary_yes'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['ancillary_more_info'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['ancillary_more_info'])))
        del wait
        self.find_element(*self.locator_dictionary['ancillary_more_info']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_plan_more_info_details_ancillary(self,benefit_name,benefit_heading):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['medical_more_info_benefit_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_benefit_name'])
        link_2 = link_1.text
        link_3 = benefit_name
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_benefit_heading'])
        link_2 = link_1.text
        link_3 = benefit_heading
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_plan_info'])
        link_2 = link_1.text
        link_3 = "Hey! Creating new Benefit.Please check to enroll in it."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_quick_links'])
        link_2 = link_1.text
        link_3 = "benemax"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['medical_more_info_document_link'])
        link_2 = link_1.text
        link_3 = "benemax_doc"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_third_question_on_ancillary(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['next_button1'])
        del page4
        self.find_element(*self.locator_dictionary['next_button1']).click()
        time.sleep(1)
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['third_qu_on_ancillary_yes'])
        del page4
        link = self.find_element(*self.locator_dictionary['third_qu_on_ancillary_yes'])
        link_1 = link.text
        link_2 = link_1.replace("c.","").strip()
        print(link_2)
        link_3 = "Who is your beneficiary?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_add_6_primary_beneficiary_for_ancillary(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['ai_beneficiary_fname'])
        del page4
        self.find_element(*self.locator_dictionary['ai_primary1_fname']).send_keys("n1")
        self.find_element(*self.locator_dictionary['ai_primary1_lname']).send_keys("j1")
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary1_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Primary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary1_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Spouse")
        del select
        self.find_element(*self.locator_dictionary['ai_primary1_percentage']).send_keys("20")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_primary2_fname']).send_keys("n2")
        self.find_element(*self.locator_dictionary['ai_primary2_lname']).send_keys("j2")
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary2_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Primary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary2_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Child")
        del select
        self.find_element(*self.locator_dictionary['ai_primary2_percentage']).send_keys("20")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_primary3_fname']).send_keys("n3")
        self.find_element(*self.locator_dictionary['ai_primary3_lname']).send_keys("j3")
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary3_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Primary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary3_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Parent")
        del select
        self.find_element(*self.locator_dictionary['ai_primary3_percentage']).send_keys("20")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_primary4_fname']).send_keys("n4")
        self.find_element(*self.locator_dictionary['ai_primary4_lname']).send_keys("j4")
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary4_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Primary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary4_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Sibling")
        del select
        self.find_element(*self.locator_dictionary['ai_primary4_percentage']).send_keys("20")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_primary5_fname']).send_keys("n5")
        self.find_element(*self.locator_dictionary['ai_primary5_lname']).send_keys("j5")
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary5_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Primary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary5_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Other")
        del select
        self.find_element(*self.locator_dictionary['ai_primary5_other']).send_keys("other reasons")
        self.find_element(*self.locator_dictionary['ai_primary5_percentage']).send_keys("10")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_primary6_fname']).send_keys("n6")
        self.find_element(*self.locator_dictionary['ai_primary6_lname']).send_keys("j6")
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary6_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Primary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_primary6_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Sibling")
        del select
        self.find_element(*self.locator_dictionary['ai_primary6_percentage']).send_keys("10")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

    def emp_add_6_secondary_beneficiary_for_ancillary(self):
        element = self.find_element(*self.locator_dictionary['ai_secondary1_fname'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        self.find_element(*self.locator_dictionary['ai_secondary1_fname']).send_keys("n1")
        self.find_element(*self.locator_dictionary['ai_secondary1_lname']).send_keys("j1")
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary1_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Secondary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary1_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Spouse")
        del select
        self.find_element(*self.locator_dictionary['ai_secondary1_percentage']).send_keys("20")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_secondary2_fname']).send_keys("n2")
        self.find_element(*self.locator_dictionary['ai_secondary2_lname']).send_keys("j2")
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary2_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Secondary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary2_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Child")
        del select
        self.find_element(*self.locator_dictionary['ai_secondary2_percentage']).send_keys("20")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_secondary3_fname']).send_keys("n3")
        self.find_element(*self.locator_dictionary['ai_secondary3_lname']).send_keys("j3")
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary3_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Secondary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary3_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Parent")
        del select
        self.find_element(*self.locator_dictionary['ai_secondary3_percentage']).send_keys("20")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_secondary4_fname']).send_keys("n4")
        self.find_element(*self.locator_dictionary['ai_secondary4_lname']).send_keys("j4")
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary4_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Secondary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary4_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Sibling")
        del select
        self.find_element(*self.locator_dictionary['ai_secondary4_percentage']).send_keys("20")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_secondary5_fname']).send_keys("n5")
        self.find_element(*self.locator_dictionary['ai_secondary5_lname']).send_keys("j5")
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary5_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Secondary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary5_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Other")
        del select
        self.find_element(*self.locator_dictionary['ai_secondary5_other']).send_keys("other reasons")
        self.find_element(*self.locator_dictionary['ai_secondary5_percentage']).send_keys("10")
        time.sleep(1)
        self.find_element(*self.locator_dictionary['ai_beneficiary_right_checkbox']).click()

        self.find_element(*self.locator_dictionary['ai_secondary6_fname']).send_keys("n6")
        self.find_element(*self.locator_dictionary['ai_secondary6_lname']).send_keys("j6")
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary6_select_relationshiptype'])
        select = Select(select_relationship)
        select.select_by_visible_text("Secondary")
        del select
        select_relationship = self.find_element(*self.locator_dictionary['ai_secondary6_select_beneficiary_relationship'])
        select = Select(select_relationship)
        select.select_by_visible_text("Sibling")
        del select
        self.find_element(*self.locator_dictionary['ai_secondary6_percentage']).send_keys("10")

    def choose_yes_on_fsa(self):
        try:
            if (self.find_element(*self.locator_dictionary['choose_yes_fsa']).is_displayed()):
                print("screen is not blank for fsa")
            else:
                self.emp_access_save_continue()
                self.hit_save_and_continue_again_come_back_on_fsa()
        except:
            print("fsa screen is visible")
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['choose_yes_fsa'])
        del page4
        self.find_element(*self.locator_dictionary['choose_yes_fsa']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_second_question_on_fsa1(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['second_qu_on_fsa_yes'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['second_qu_on_fsa_yes'])
        link_2 = link_1.text
        link_3 = "How much would you like to contribute per year?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_fill_contribution_fsa(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fsa_contribution'])
        del page4
        self.find_element(*self.locator_dictionary['fsa_contribution']).send_keys("10")

    def verify_third_qu_fsa(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['third_qu_on_fsa_yes'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['third_qu_on_fsa_yes'])
        link_2 = link_1.text
        link_3 = "Do you agree to the Terms & Conditions?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_correct_info_terms_condition(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fsa_terms_condition'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['fsa_terms_condition'])
        link_2 = link_1.text
        link_3 = "Hey! Creating new Benefit.Please check to enroll in it."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def verify_terms_checkbox_fsa(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fsa_terms_checkbox'])
        del page4
        self.find_element(*self.locator_dictionary['fsa_terms_checkbox']).is_selected()
        return True

    def verify_fsa_plan_details(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fsa_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['fsa_plan_name'])
        link_2 = link_1.text
        link_3 = "fsa_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['fsa_max_contribution'])
        link_2 = link_1.text
        link_3 = "123"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['fsa_your_health_plans'])
        link_2 = link_1.text
        link_3 = "Hey! Creating new Benefit.Please check to enroll in it."
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def emp_access_more_info_fsa(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fsa_more_info'])
        del page4
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.element_to_be_clickable((self.locator_dictionary['fsa_more_info'])))
        del wait
        self.find_element(*self.locator_dictionary['fsa_more_info']).click()
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def emp_access_previous_fsa(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['previous_button'])
        del page4
        self.find_element(*self.locator_dictionary['previous_button']).click()
        time.sleep(1)

    def verify_fsa_alert(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['fsa_alert'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['fsa_alert'])
        link_2 = link_1.text
        link_3 = "Are you sure?"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1
        del link_2
        del link_3

    def emp_access_yes_fsa(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['yes_fsa'])
        del page4
        self.find_element(*self.locator_dictionary['yes_fsa']).click()
        time.sleep(1)

    def verify_save_continue_enabled(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['save_and_continue'])
        del page4
        self.find_element(*self.locator_dictionary['save_and_continue']).is_enabled()
        return True

    def verify_medical_yes_on_review(self,primary_name_medical_on_review,dependent1_name_medical_on_review,dependent2_name_medical_on_review,dependent3_name_medical_on_review,dependent4_name_medical_on_review,dependent5_name_medical_on_review,dependent6_name_medical_on_review,medical_cost_per_pay_period_on_review,medical_co_pay_on_review,medical_rx_cost_on_review,medical_deductible_on_review):
        element = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_medical_plan_name'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_yes_on_review_for_medical_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_medical_plan_name'])
        link_2 = link_1.text
        link_3 = "medical_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_primary_name_medical_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_primary_name_medical_on_review'])
        link_2 = link_1.text
        link_3 = primary_name_medical_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent1_name_medical_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent1_name_medical_on_review'])
        link_2 = link_1.text
        link_3 = dependent1_name_medical_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent2_name_medical_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent2_name_medical_on_review'])
        link_2 = link_1.text
        link_3 = dependent2_name_medical_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent3_name_medical_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent3_name_medical_on_review'])
        link_2 = link_1.text
        link_3 = dependent3_name_medical_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent4_name_medical_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent4_name_medical_on_review'])
        link_2 = link_1.text
        link_3 = dependent4_name_medical_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent5_name_medical_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent5_name_medical_on_review'])
        link_2 = link_1.text
        link_3 = dependent5_name_medical_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent6_name_medical_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent6_name_medical_on_review'])
        link_2 = link_1.text
        link_3 = dependent6_name_medical_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_medical_cost_per_pay_period_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_medical_cost_per_pay_period_on_review'])
        link_2 = link_1.text
        link_3 = medical_cost_per_pay_period_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_medical_co_pay_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_medical_co_pay_on_review'])
        link_2 = link_1.text
        link_3 = medical_co_pay_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_medical_rx_cost_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_medical_rx_cost_on_review'])
        link_2 = link_1.text
        link_3 = medical_rx_cost_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_medical_deductible_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_medical_deductible_on_review'])
        link_2 = link_1.text
        link_3 = medical_deductible_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_dental_yes_on_review(self,primary_name_dental_on_review,dependent1_name_dental_on_review,dependent2_name_dental_on_review,dependent3_name_dental_on_review,dependent4_name_dental_on_review,dependent5_name_dental_on_review,dependent6_name_dental_on_review,dental_cost_per_pay_period_on_review):
        element = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_dental_plan_name'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_yes_on_review_for_dental_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_dental_plan_name'])
        link_2 = link_1.text
        link_3 = "dental_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_primary_name_dental_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_primary_name_dental_on_review'])
        link_2 = link_1.text
        link_3 = primary_name_dental_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent1_name_dental_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent1_name_dental_on_review'])
        link_2 = link_1.text
        link_3 = dependent1_name_dental_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent2_name_dental_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent2_name_dental_on_review'])
        link_2 = link_1.text
        link_3 = dependent2_name_dental_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent3_name_dental_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent3_name_dental_on_review'])
        link_2 = link_1.text
        link_3 = dependent3_name_dental_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent4_name_dental_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent4_name_dental_on_review'])
        link_2 = link_1.text
        link_3 = dependent4_name_dental_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent5_name_dental_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent5_name_dental_on_review'])
        link_2 = link_1.text
        link_3 = dependent5_name_dental_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent6_name_dental_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent6_name_dental_on_review'])
        link_2 = link_1.text
        link_3 = dependent6_name_dental_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dental_cost_per_pay_period_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dental_cost_per_pay_period_on_review'])
        link_2 = link_1.text
        link_3 = dental_cost_per_pay_period_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_vision_yes_on_review(self,primary_name_vision_on_review,dependent1_name_vision_on_review,dependent2_name_vision_on_review,vision_cost_per_pay_period_on_review):
        element = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_vision_plan_name'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_yes_on_review_for_vision_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_vision_plan_name'])
        link_2 = link_1.text
        link_3 = "vision_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_primary_name_vision_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_primary_name_vision_on_review'])
        link_2 = link_1.text
        link_3 = primary_name_vision_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent1_name_vision_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent1_name_vision_on_review'])
        link_2 = link_1.text
        link_3 = dependent1_name_vision_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_dependent2_name_vision_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_dependent2_name_vision_on_review'])
        link_2 = link_1.text
        link_3 = dependent2_name_vision_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_vision_cost_per_pay_period_on_review'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_vision_cost_per_pay_period_on_review'])
        link_2 = link_1.text
        link_3 = vision_cost_per_pay_period_on_review
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_ancillary_yes_on_review(self):
        element = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_ancillary_plan_name'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_yes_on_review_for_ancillary_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_ancillary_plan_name'])
        link_2 = link_1.text
        link_3 = "ancillary_benefit"
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1,link_2,link_3

    def verify_fsa_yes_on_review(self,fsa_maximum_contribution):
        element = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_fsa_plan_name'])
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        del element
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['verify_yes_on_review_for_fsa_plan_name'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['verify_yes_on_review_for_fsa_plan_name'])
        link_2 = link_1.text
        link_3 = fsa_maximum_contribution
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def click_enrollment_tab(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['enrollment_tab'])
        del page4
        self.find_element(*self.locator_dictionary['enrollment_tab']).click()
        time.sleep(1)

    def apply_incomplete_filter_enrollment(self):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['apply_enrollment_filter'])
        del page4
        select_employee_state = self.find_element(*self.locator_dictionary['apply_enrollment_filter'])
        select = Select(select_employee_state)
        select.select_by_visible_text("Incomplete Enrollments")
        del select
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def search_employee_on_enrollment_table(self,employee_name_on_enrollment_table):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['search_enrollment'])
        del page4
        self.find_element(*self.locator_dictionary['search_enrollment']).send_keys(employee_name_on_enrollment_table)
        time.sleep(1)
        wait = WebDriverWait(self.browser, 15)
        wait.until(EC.invisibility_of_element_located((self.locator_dictionary['loader'])))
        del wait

    def verify_emp_details_in_enrollment_table(self,emp_fname_in_enrollment_table,emp_lname_in_enrollment_table,emp_ssn_in_enrollment_table):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_fname_in_enrollment_table'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['emp_fname_in_enrollment_table'])
        link_2 = link_1.text
        link_3 = emp_fname_in_enrollment_table
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['emp_lname_in_enrollment_table'])
        link_2 = link_1.text
        link_3 = emp_lname_in_enrollment_table
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3
        link_1 = self.find_element(*self.locator_dictionary['emp_ssn_in_enrollment_table'])
        link_2 = link_1.text
        link_3 = emp_ssn_in_enrollment_table
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3

    def verify_emp_status_in_enrollment_table(self,emp_status_in_enrollment_table):
        page4 = BasePage(self)
        page4.wait_for_ele_visibility(*self.locator_dictionary['emp_status_in_enrollment_table'])
        del page4
        link_1 = self.find_element(*self.locator_dictionary['emp_status_in_enrollment_table'])
        link_2 = link_1.text
        link_3 = emp_status_in_enrollment_table
        assert link_2 == link_3, "Visible text is not as expected." \
                                 " Actual: {}, Expected: {}".format(link_2, link_3)
        del link_1, link_2, link_3







