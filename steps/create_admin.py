from behave import *
from pages.create_admin import *
from pages.create_user_api import dict1
from pages.edit_admin import *
from pages.login_page import *
from pages.signup_claim_account import *
from pages.search_admin import SearchAdminPage
import calendar
from pages.create_user_api import *
from environment import email_before_gmail_domain


@when("I open create admin modal")
def step_impl(context):
    page1 = LoginPage(context)
    page1.login()
    page1.verify_afterlogin()
    del page1
    page = CreateAdminPage(context)
    page.click_create_administrator()
    del page

@then("Verify correct admin modal should be open")
def verify_create_admin_modal(context):
      page2 = CreateAdminPage(context)
      page2.verify_admin_modal()
      del page2

@when("I enter correct data in all fields  and submit details")
def create_admin(context):
    global first_name
    showtime = calendar.timegm(time.gmtime())
    first_name = str(showtime)+ "Nainsi"
    page3 = CreateAdminPage(context)
    email = email_before_gmail_domain+"+"+"30"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
    page3.create_admin_owner(first_name, "Jain", email )
    del page3


@then("Verify admin should be created and displayed in table view")
def verify_created_admin(context):
    page4 = SearchAdminPage(context)
    page4.search_with_pending_filter(first_name)
    page4.verify_searched_admin(first_name)
    del page4

@then("Verify admin should be created as in Pending state")
def verify_admin_inactive(context):
      page6 = CreateAdminPage(context)
      page6.verify_created_admin_pending_state()
      del page6

@when("Admin signuot from existing account")
def signout(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@when("Admin create another Benemax admin with inactive status")
def create_another_admin(context) :
    page = Create_user(context)
    page.create_user_gettoken()
    del page

@then("that created admin complete claim account process")
def admin_claim_account(context):
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@then("verify that created admin should show in table view")
def verify_created_admin(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page1 = LoginPage(context)
    page1.login()
    page1.verify_afterlogin()
    del page1
    page = EditAdminPage(context)
    page.click_admin_tab()
    del page
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(dict1["first_name2"])
    page4.verify_searched_admin(dict1["first_name2"])
    del page4

@then("verify that created admin should show in active state")
def verify_admin_active_after_claim_account(context):
    page4 = CreateAdminPage(context)
    page4.verify_created_admin_active_state()
    del page4

@when("Admin with owner permission deactivate already active admin")
def admin_deactivate_another_admin(context) :
    page5 = EditAdminPage(context)
    page5.deactivate_admin()
    del page5

@then("Verify admin should still show in table view")
def admin_show_in_table(context):
    page4 = SearchAdminPage(context)
    page4.search_with_inactive_filter(dict1["first_name2"])
    page4.verify_searched_admin(dict1["first_name2"])
    del page4

@then("Verify admin should be show as Inactive state")
def verify_inactive_admin(context):
    page4 = CreateAdminPage(context)
    page4.verify_created_admin_inactive_state()
    del page4



