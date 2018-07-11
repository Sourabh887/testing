from behave import *
from pages.edit_organization import *
from pages.create_organization import *
from pages.login_page import *
from pages.search_organization import *
import calendar

org1 = str(calendar.timegm(time.gmtime())) + "Capgemini"
org2 = str(calendar.timegm(time.gmtime())) + "Northout"
@when("I create an organization with pending state")
def create_inactive_org(context) :
    global org1
    page = LoginPage(context)
    page.login()
    del page
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
    page5.enter_org_disp_name(org1)
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7


@when("I search for an orgaization which is pending")
def search_inactive_org(context) :
    page = SearchOrganization(context)
    page.search_with_pending_filter(org1)

@when("I open edit organization modal")
def step_impl(context):
    page1 = EditOrganizationPage(context)
    page1.click_edit_organization()
    del page1

@then("Verify edit organization modal should be open")
def first_modal_verify(context):
      page2 = EditOrganizationPage(context)
      page2.verify_edit_org_Modal()
      del page2


@when("I enter correct data in all fields on first section and go to second section")
def edit_organization(context):
    page3 = EditOrganizationPage(context)
    page3.edit_organization("Org2","Nainsi1","12346","1235","1234567899","1234567899","http://org1.com","75 rue de la ","rotisseriel1","Paris","12344", "7 rue de la","rotisseriel1","Paris","12344")
    time.sleep(1)
    del page3

@when("I enter Organization display name and go on third section")
def edit_org_second_modal(context):
    global org2
    page5 = EditOrganizationPage(context)
    page5.enter_org_disp_name_go_third_section(org2)
    del page5


@when("I enter correct data in all fields on third section and save changes")
def edit_org_third_modal(context):
    page7 = EditOrganizationPage(context)
    page7.edit_organization_third_section("n","n","n","n","n","nainsi1 jain"+str(calendar.timegm(time.gmtime())))
    del page7

@then("Verify Organization should be updated successfully")
def verify_edited_organization(context):
    page = SearchOrganization(context)
    page.search_with_pending_filter(org2)
    page8 = EditOrganizationPage(context)
    page8.verify_organization_edited(org2)
    del page8

