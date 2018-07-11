from behave import *
from pages.create_organization import *
from pages.login_page import *
from pages.search_organization import *
import calendar

@when("I open create organization modal")
def step_impl(context):
    page = LoginPage(context)
    page.login()
    del page
    page1 = CreateOrganizationPage(context)
    page1.click_create_organization()
    del page1

@then("Verify correct modal should be open")
def first_modal_verify(context):
      page2 = CreateOrganizationPage(context)
      page2.verify_create_organization_first_modal()
      del page2


@when("I enter correct data in all fields on first section and continue the process")
def create_organization(context):
    page3 = CreateOrganizationPage(context)
    page3.create_organization("Org1","Nainsi","12345","1234","1234567890","1234567890","http://org.com","7 rue de la ","rotisseriel","Paris","12345", "5 rue de la","rotisseriel","Paris","12345")
    time.sleep(3)
    del page3

@then("Verify I redirected on second section")
def first_modal_verify(context):
      page4 = CreateOrganizationPage(context)
      page4.verify_create_organization_second_modal()
      del page4

@when("I enter Organization display name and continue process")
def create_org_second_modal(context):
    global org1
    showtime = calendar.timegm(time.gmtime())
    org1 = str(showtime) + "Capgemini"
    page5 = CreateOrganizationPage(context)
    page5.enter_org_disp_name(org1)
    page5.image_upload()
    del page5

@then("Verify I redirected on third section")
def third_modal_verify(context):
      page6 = CreateOrganizationPage(context)
      page6.verify_create_organization_third_modal()
      del page6

@when("I enter correct data in all fields on third section and finish the process")
def create_org_third_modal(context):
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n","n","n","n","n","nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7


@then("Verify Organization should be created successfully")
def verify_created_organization(context):
      page = SearchOrganization(context)
      page.search_with_pending_filter(org1)
      page8 = CreateOrganizationPage(context)
      page8.verify_organization_created(org1)
      del page8

