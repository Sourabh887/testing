from behave import *
from pages.search_organization import *
from pages.active_deactive_org import *
from pages.login_page import *
from steps.edit_organization import org2

@when("I enter data in search field to search existing organization")
def step_impl(context):
    page1 = SearchOrganization(context)
    page1.search(org2)
    del page1

@then("Verify Organization should be displayed according to entered search data")
def verify_org(context):
      page2 = SearchOrganization(context)
      page2.verify_searched_org()
      del page2


@when("I clear data in search filed and applied inactive organization filter")
def step_impl(context):
    page = SearchOrganization(context)
    page.search_with_inactive_filter(org2)
    del page

@then("Verify Organization should be displayed according to entered search data and applied inactive filter")
def verify_org(context):
      page2 = SearchOrganization(context)
      page2.verify_searched_org()
      del page2

@when("I activate already inactive organization")
def step_impl(context):
    page = Active_Deactive_Org(context)
    page.click_active_organization()
    page.click_yes_activate()
    del page

@when("I clear data in search filed and applied active organization filter")
def step_impl(context):
    page = SearchOrganization(context)
    page.search_with_active_filter(org2)
    del page

@then("Verify Organization should be displayed according to entered search data and applied active filter")
def verify_org(context):
      page2 = SearchOrganization(context)
      page2.verify_searched_org()
      del page2
