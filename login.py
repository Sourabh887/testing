from behave import *
from pages.login_page import *

@when("I enter valid username and password")
def step_impl(context):
    page = LoginPage(context)
    page.login()
    del page



@then("I should be able to Login")
def login_success(context):
        print("Successfully Logged in")
        pass


@then("Verify that i am on correct Page after Login")
def verify(context):
    page1 = LoginPage(context)
    page1.verify_afterlogin()
    del page1




