from steps.create_admin import *
from pages.create_user_api import *
from pages.signup_claim_account import *
from environment import email_before_gmail_domain

edit_admin_name = str(calendar.timegm(time.gmtime()))+"Nainsi"
edit_admin_email = email_before_gmail_domain+"+"+"31"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
@given("I create Benemax admin with owner permission")
def create_admin_api(context):
    page = Create_user(context)
    page.create_user_gettoken()
    del page

@when("Created Benemax admin complete claim account process")
def complete_claim_account(context):
    page = ClaimAccountPage(context)
    page.claim_account_invitation_link("12345678","12345678")
    del page

@then("Verify admin should be redirected to Dashboard view")
def admin_dashboard_view(context):
    page = LoginPage(context)
    page.verify_afterlogin()
    del page

@when("I Signout from existing admin accuont and again login as Benemax admin with owner permission")
def signout_admin(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page = LoginPage(context)
    page.login()
    page.verify_afterlogin()
    del page

@when("I search for an admin with owner permission")
def verify_edit_admin_modal(context):
      page = EditAdminPage(context)
      page.click_admin_tab()
      page2 = SearchAdminPage(context)
      page2.search_with_active_filter(dict1["first_name2"])
      del page2

@when("I edit details of benemax admin with owner permission and without changing permission enter correct data in all fields and submit details")
def edit_admin(context):
    page = EditAdminPage(context)
    page.click_edit_administrator()
    del page
    page3 = EditAdminPage(context)
    page3.edit_admin_owner(edit_admin_name, "Jain", edit_admin_email )
    del page3

@then("Verify admin should be edited and displayed in table view")
def verify_edited_admin(context):
      page4 = SearchAdminPage(context)
      page4.search_with_active_filter(edit_admin_name)
      page4.verify_searched_admin(edit_admin_name)
      del page4

@then("Verify admin should be edited as in activate state")
def verify_edited_admin_active(context):
      page6 = EditAdminPage(context)
      page6.verify_edited_admin_active_state()
      del page6

@when ("admin signout from existing account and wants to Login with old email")
def admin_signout_login_with_old_email(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page1 = LoginPage(context)
    page1.dynamic_login_with_click_loginink(dict1["api_email"],"12345678")
    del page1


@then("verify admin should not be able to Login")
def verify_admin_not_login(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("No account associated with this email or password")
    del page
    time.sleep(1)

@when ("admin wants to Login with newly updated email and password")
def admin_login_edit_email(context):
    page = LoginPage(context)
    page.dynamic_login_without_click_loginink(edit_admin_email,"12345678")
    del page

@then("verify admin should be able to Login with newly updated email and Password")
def verify_login(context) :
    page1 = LoginPage(context)
    page1.verify_afterlogin()
    del page1
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@when("Benemax admin Login and search for an admin with owner permission")
def create_search_admin_edit_permission(context) :
    page = LoginPage(context)
    page.login()
    del page
    page = EditAdminPage(context)
    page.click_admin_tab()
    del page
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(edit_admin_name)
    page4.verify_searched_admin(edit_admin_name)
    del page4

@when("I open edit modal to change permission of already existing admin from owner to edit")
def admin_edit_permission(context):
    page3 = EditAdminPage(context)
    page3.click_edit_administrator()
    del page3

@then("Verify correct edit modal for admin should be open")
def verify_admin_edit_permission(context):
    page3 = EditAdminPage(context)
    page3.verify_admin_tab()
    del page3

@when("admin edit details and change admin permission from owner to edit")
def admin_edit_permission(context):
    page3 = EditAdminPage(context)
    page3.edit_admin_edit_permission()
    del page3

@then("Verify admin should be still displayed in table view")
def verify_admin_table_view(context):
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(edit_admin_name)
    page4.verify_searched_admin(edit_admin_name)
    del page4

@when ("I Signout from existing admin accuont and again login as Benemax admin with edit permission")
def admin_signout_login_with_edit_permission(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page1 = LoginPage(context)
    page1.dynamic_login_with_click_loginink(edit_admin_email,"12345678")
    del page1

@then("Verify only organization view should be displayed to admin and administrator view should not be displayed")
def verify_org_view_admin(context):
    page1 = LoginPage(context)
    page1.verify_afterlogin()
    del page1

@when("Benemax admin with edit permission signout from existing account")
def admin_signout_login_with_edit_permission(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page

@then("Benemax admin with owner permission again Login to change permission of another admin who has edit permission")
def admin_Login_with_owner_permission(context):
    page1 = LoginPage(context)
    page1.login()
    del page1




@when("Benemax admin Login and search for an admin with edit permission")
def create_search_admin_edit_permission(context) :
    page = EditAdminPage(context)
    page.click_admin_tab()
    del page
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(edit_admin_name)
    page4.verify_searched_admin(edit_admin_name)
    del page4

@when("I open edit modal to change permission of already existing admin from edit to read")
def admin_edit_permission(context):
    page3 = EditAdminPage(context)
    page3.click_edit_administrator()
    del page3

@then("Verify correct edit modal for admin with edit permission should be open")
def verify_admin_edit_permission(context):
    page3 = EditAdminPage(context)
    page3.verify_admin_tab()
    del page3


@when("admin edit details and change admin permission from edit to read")
def admin_edit_permission(context):
    page3 = EditAdminPage(context)
    page3.edit_admin_read_permission()
    del page3

@then("Verify admin should be still displayed in table view with active status")
def verify_admin_table_view(context):
    page4 = SearchAdminPage(context)
    page4.search_with_active_filter(edit_admin_name)
    page4.verify_searched_admin(edit_admin_name)
    del page4

@when ("I Signout from existing admin accuont and again login as Benemax admin with read permission")
def admin_signout_login_with_edit_permission(context):
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page
    page1 = LoginPage(context)
    page1.dynamic_login_with_click_loginink(edit_admin_email,"12345678")
    del page1

@then("Verify only organization view should be displayed to admin")
def verify_org_view_admin(context):
    page2 = LoginPage(context)
    page2.verify_org_text_afterlogin()
    del page2












