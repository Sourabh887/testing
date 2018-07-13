from selenium import webdriver
# If you don't see colors (RED and GREEN) on command line, add the below lines
# from colorama import init
# init()
import os
# import zipfile
import shutil
import time
import logging
import platform
from pages.base_page_object import BasePage
from pages.signup_claim_account import *
from pages.create_user_api import *
from pages.profile_dropdown import *
from sauceclient import SauceClient

env = "stage"

config = {
    "dev": {
		"url": "http://18.188.55.103:3000",
		"database": "devdb",
		"user": "dev",
		"password": "umfs5hW62eVH6dA3",
		"host": "dev.c20pjk4x9sqv.us-east-2.rds.amazonaws.com",
		"port": 5432,
        "API_URL": "http://18.188.55.103"
	},
	"stage": {
		"url": "http://stage.vbm.benemax.com",
		"database": "ebdb",
		"user": "stage",
		"password": "bP2eCV5YEaxXMkdB",
		"host": "aaqu724uib4gl3.c20pjk4x9sqv.us-east-2.rds.amazonaws.com",
		"port": 5432,
        "API_URL": "http://stage-backend.us-east-2.elasticbeanstalk.com"
	},
	"prod": {
		"url": "http://vbm.benemax.com",
		"database": "ebdb",
		"user": "production",
		"password": "vLfawhtKQV4ke6vc",
		"host": "aa19i4sqw65zubw.c20pjk4x9sqv.us-east-2.rds.amazonaws.com",
		"port": 5432
	}
}


url = config[env]['url']
API_URL = config[env]['API_URL']
databse = config[env]['database']
user = config[env]['user']
password = config[env]['password']
host = config[env]['host']
port = config[env]['port']
email_before_gmail_domain = "nainsitest1"





def before_all(context):
    print("Executing before all - creating benemax admin with owner permission to use it everywhere")
    before_feature(context,feature='')
    page = Create_user(context)
    page.create_universal_benemax_admin_owner_permission(context)
    page1 = ClaimAccountPage(context)
    page1.claim_account_invitation_link("12345678","12345678")
    time.sleep(1)
    page1.click_signuot()
    del page
    del page1
    context.browser.quit()

    # def before_feature(context, scenario):
    #  print("Before feature\n")
    #  # Create logger
    #  # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    #  context.logger = logging.getLogger('seleniumframework_tests')
    #  hdlr = logging.FileHandler('./seleniumframework_tests.log')
    #  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #  hdlr.setFormatter(formatter)
    #  context.logger.addHandler(hdlr)
    #  context.logger.setLevel(logging.DEBUG)

# Scenario level objects are popped off context when scenario exits

def before_feature(context,feature):
    print("User data:", context.config.userdata)
    # desired_cap = {
    #     'platform': "windows 10",
    #     'browserName': "chrome",
    #     'version': "67"
    # }

    desired_caps = {}
    desired_caps['platform'] = os.getenv('SELENIUM_PLATFORM')
    desired_caps['browserName'] = os.getenv('SELENIUM_BROWSER')
    desired_caps['version'] = os.getenv('SELENIUM_VERSION')
    desired_caps['buildinfo']=(os.getenv('JOB_NAME')+" "+os.getenv('BUILD_NUMBER'))


    context.browser = webdriver.Remote(
        command_executor='http://sourabh94:e4be7c8c-f774-4534-b8e6-0be51798cc77@ondemand.saucelabs.com:80/wd/hub',
        desired_capabilities=desired_caps)


    # behave -D BROWSER=chrome
    # if 'BROWSER' in context.config.userdata.keys():
    #     if context.config.userdata['BROWSER'] is None:
    #         BROWSER = 'chrome'
    #     else:
    #         BROWSER = context.config.userdata['BROWSER']
    # else:
    #     BROWSER = 'chrome'
    # # For some reason, python doesn't have switch case -
    # # http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    # current_paltform = platform.system()
    # if current_paltform != "Linux" :
    #     print("I am in window")
    #     if BROWSER == 'chrome':
    #          context.browser = webdriver.Chrome()
    #     elif BROWSER == 'firefox':
    #         context.browser = webdriver.Firefox()
    #     elif BROWSER == 'safari':
    #         context.browser = webdriver.Safari()
    #     elif BROWSER == 'ie':
    #         context.browser = webdriver.Ie()
    #     elif BROWSER == 'opera':
    #         context.browser = webdriver.Opera()
    #     elif BROWSER == 'phantomjs':
    #         context.browser = webdriver.PhantomJS()
    #     else:
    #         print("Browser you entered:", BROWSER, "is invalid value")
    # else :
    #     print("I am in linux")
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--no-sandbox')
    #     try:
    #         context.browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
    #     except Exception as e:
    #         print(e)

    # context.browser.get("http://18.216.125.171:3000/home")
    context.browser.get(url)
    context.browser.implicitly_wait(3)
    # context.browser.maximize_window()
    print("Before scenario\n")

    # a = context.browser.get_window_size()
    # print(a)

    # context.browser.set_window_size(1382, 744)
    time.sleep(5)


def after_feature(context, scenario):
    # print("scenario status" + scenario.status)
    # if scenario.status == "failed":
    #     if not os.path.exists("failed_scenarios_screenshots"):
    #         os.makedirs("failed_scenarios_screenshots")
    #     os.chdir("failed_scenarios_screenshots")
    #     context.browser.save_screenshot(scenario.name + "_failed.png")
    # context.browser.quit()

    print("scenario status" + scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()

    def after_scenario(context, scenario):
            print("\nAfter Feature")

    if hasattr(context,'browser'):
        sauce_client = SauceClient("sourabh94", "e4be7c8c-f774-4534-b8e6-0be51798cc77")
        test_status = scenario.status == 'passed'
        sauce_client.jobs.update_job(context.browser.session_id, passed=test_status)

def after_all(context):
    print("User data:", context.config.userdata)
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            os.rmdir("failed_scenarios_screenshots")
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
    time.strftime("%d_%m_%Y"),
    'zip',
     "failed_scenarios_screenshots")
            #os.rmdir("failed_scenarios_screenshots")
            print("Executing after all")



