from behave import *
from pages.active_deactive_org import *
from pages.login_page import *
from pages.search_organization import *
from steps.edit_organization import org2

@when("I open Activate/Deactivate organization modal to activate an Organization")
def step_impl(context):
    page = SearchOrganization(context)
    page.search_with_pending_filter(org2)
    del page
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    del page1

@then("Verify Activate/Deactivate modal should be open")
def active_modal_verify(context):
      page2 = Active_Deactive_Org(context)
      page2.verify_active_org_Modal()
      del page2


@when("I choose Yes option to activate an Organization")
def edit_organization(context):
    page3 = Active_Deactive_Org(context)
    page3.click_yes_activate()
    time.sleep(2)
    del page3

@then("organization should be activated Successfully")
def edit_org_second_modal(context):
    pass
    print("Organization activated successfully")


@then("verify Organization status should be show as active in list")
def verify_org_active(context):
    page = SearchOrganization(context)
    page.search_with_active_filter(org2)
    del page
    page7 =  Active_Deactive_Org(context)
    page7.verify_activated_organization(org2)
    del page7

@when("I again open Activate/Deactivate organization modal to deactivate an organization")
def step_impl(context):
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    del page1

@then("Verify cctivate/deactivate modal should be open")
def active_modal_verify(context):
      page2 = Active_Deactive_Org(context)
      page2.verify_deactive_org_Modal()
      del page2


@when("I choose Yes option to deactivate an Organization")
def edit_organization(context):
    page3 = Active_Deactive_Org(context)
    page3.click_yes_deactivate()
    time.sleep(2)
    del page3

@then("organization should be deactivated Successfully")
def edit_org_second_modal(context):
    pass
    print("Organization deactivated successfully")


@then("verify Organization status should be show as deactive in list")
def verify_org_active(context):
    page = SearchOrganization(context)
    page.search_with_inactive_filter(org2)
    del page
    page7 =  Active_Deactive_Org(context)
    page7.verify_deactivated_organization(org2)
    del page7

