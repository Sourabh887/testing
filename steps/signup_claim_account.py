from behave import *
from pages.signup_claim_account import *

@when("I fill valid details in all the provided fields")
def step_impl(context):
    page = ClaimAccountPage(context)
    page.visit_signup('http://stage-front.us-east-2.elasticbeanstalk.com/signup')
    page.signup('Nainsi','Jain','nainsi2@mailnesia.com','12345678','12345678')
    time.sleep(5)
    del page



@then("I should be able to Signup successfully")
def verify(context):
        time.sleep(3)
        page1 = ClaimAccountPage(context)
        page1.verify_success_msg()
        time.sleep(3)
        del page1


