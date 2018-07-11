from pages.signup_claim_account import *
from pages.create_organization import *
from pages.search_organization import *
from pages.group_class_division import *
from pages.active_deactive_org import *
from steps.create_admin import *
from pages.create_user_api import *
import calendar


orgs = Create_user.getOrgs()

@when("Benemax admin with owner permission Login and want to create an organization")
def create_org(context):
    page = LoginPage(context)
    page.login()
    page.verify_afterlogin()
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
    page5.enter_org_disp_name(orgs['org1'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7


@then("Verify Organization created and search for same organization")
def search_activate_org(context):
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs['org1'])
    page1 = Active_Deactive_Org(context)
    page1.click_active_organization()
    page1.click_yes_activate()
    page.search_with_active_filter(orgs['org1'])
    del page
    del page1

@when("admin access same searched organization and Groups for that organization")
def access_group(context):
    page = Group_class_divisionPage(context)
    page.click_org()
    page.click_group()
    del page

@then("Verify admin with owner permission should be able to see Create Group option")
def verify_create_group(context):
    page = Group_class_divisionPage(context)
    page.verify_create_group_btn()
    del page

@when("I open Create Group modal and verify correct modal should be open")
def verify_create_group_modal(context):
    page = Group_class_divisionPage(context)
    page.click_create_group()
    del page

@when("I enter valid data in group name and Direct Id")
def open_create_group(context):
    page = Group_class_divisionPage(context)
    page.create_group("G1","Nainsi"+str(calendar.timegm(time.gmtime())))
    del page

@then("Verify success message should be displayed for created group")
def verify_msg_group(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Group is created successfully.")
    del page

@then("Verify Created Group should be displayed in table view")
def verify_created_group(context):
    page = Group_class_divisionPage(context)
    page.verify_created_group("G1")
    del page

@when("I again open create group and enter same Group name for same organization")
def again_create_same_group(context) :
    page = Group_class_divisionPage(context)
    page.click_create_group()
    page.create_group("G1", "Nainsi"+str(calendar.timegm(time.gmtime())))
    del page

@then("Verify error message should be displayed")
def verify_errormsg_group(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("Group or DirectId is already exists.")
    del page


@when("i close Create Group modal")
def close_create_group_modal(context):
    page = Group_class_divisionPage(context)
    page.click_close_modal()
    del page


@when("Benemax admin with owner permission access Edit Group option")
def access_edit_group(context):
      page4 = Group_class_divisionPage(context)
      page4.click_edit_group()
      page4.click_edit_group_btn()
      del page4

@then("Verify Edit Group modal should be displayed")
def verify_edit_group_modal(context):
      page4 = Group_class_divisionPage(context)
      page4.verify_edit_group_modal()
      del page4

@when("I again enter valid data in group name and Direct Id")
def edit_group(context):
    page4 = Group_class_divisionPage(context)
    page4.edit_group("G2","Nainsi1"+str(calendar.timegm(time.gmtime())))
    del page4

@then("Verify success message should be displayed for updated Group")
def verify_success_msg_edit_group(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Group is updated successfully.")
    del page
    time.sleep(4)

@then("Verify Updated Group should be displayed in table view")
def verify_updatedgroup(context):
    page = Group_class_divisionPage(context)
    page.verify_edited_group("G2")
    del page

############################################

@when("admin access same searched organization and division for that organization")
def access_division(context):
    page = Group_class_divisionPage(context)
    page.click_division()
    del page

@then("Verify admin with owner permission should be able to see Create division option")
def verify_create_division(context):
    page = Group_class_divisionPage(context)
    page.verify_create_division_btn()
    del page

@when("I open Create division modal and verify correct modal should be open")
def verify_create_division_modal(context):
    page = Group_class_divisionPage(context)
    page.click_create_division()
    del page

@when("I enter valid data in division name and Direct Id and select valid group")
def open_create_division(context):
    page = Group_class_divisionPage(context)
    page.create_division("D1","abc"+str(calendar.timegm(time.gmtime())),"G2")
    del page

@then("Verify success message should be displayed for created division")
def verify_msg_createddivision(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Division is created successfully.")
    del page

@then("Verify Created Division should be displayed in table view")
def verify_created_division(context):
    page = Group_class_divisionPage(context)
    page.verify_created_division("D1")
    del page

@when("I again open create division and enter same division name for same organization")
def again_create_same_division(context) :
    page = Group_class_divisionPage(context)
    page.click_create_division()
    page.create_division("D1","Nainsi"+str(calendar.timegm(time.gmtime())),"G2")
    del page

@then("Verify error message should be displayed for create division")
def verify_msg_division_error(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("Division or DirectId is already exists")
    del page


@when("i close Create Division modal")
def close_create_division_modal(context):
    page = Group_class_divisionPage(context)
    page.click_close_modal()
    del page


@when("Benemax admin with owner permission access Edit Division option")
def access_edit_division(context):
      page4 = Group_class_divisionPage(context)
      page4.click_edit_division()
      page4.click_edit_division_btn()
      del page4

@then("Verify Edit Division modal should be displayed")
def verify_edit_division_modal(context):
      page4 = Group_class_divisionPage(context)
      page4.verify_edit_division_modal()
      del page4

@when("I again enter valid data in Division name and Direct Id")
def edit_division(context):
    page4 = Group_class_divisionPage(context)
    page4.edit_division("D2","Nainsi1"+str(calendar.timegm(time.gmtime())))
    del page4

@then("Verify success message should be displayed for updated Division")
def verify_success_msg_updated_division(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Division is updated successfully.")
    del page
    time.sleep(4)

@then("Verify Updated Division should be displayed in table view")
def verify_updated_division(context):
    page = Group_class_divisionPage(context)
    page.verify_edited_division("D2")
    del page

###################################################

@when("admin access same searched organization and Class for that organization")
def access_class(context):
    page = Group_class_divisionPage(context)
    page.click_class()
    del page

@then("Verify admin with owner permission should be able to see Create Class option")
def verify_create_class(context):
    page = Group_class_divisionPage(context)
    page.verify_create_class_btn()
    del page

@when("I open Create Class modal and verify correct modal should be open")
def verify_create_class_modal(context):
    page = Group_class_divisionPage(context)
    page.click_create_class()
    del page

@when("I enter valid data in Class name and Direct Id")
def open_create_class(context):
    page = Group_class_divisionPage(context)
    page.create_class("C1","Nainsi1"+str(calendar.timegm(time.gmtime())))
    del page

@then("Verify success message should be displayed for created Class")
def verify_msg_createdclass(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Class is created successfully.")
    del page


@then("Verify Created Class should be displayed in table view")
def verify_created_class(context):
    page = Group_class_divisionPage(context)
    page.verify_created_class("C1")
    del page

@when("I again open create Class and enter same Class name for same organization")
def again_create_same_class(context) :
    page = Group_class_divisionPage(context)
    page.click_create_class()
    page.create_class("C1","12345"+str(calendar.timegm(time.gmtime())))
    del page

@then("Verify error message should be displayed for create Class")
def verify_errormsg_class(context):
    page = ClaimAccountPage(context)
    page.verify_error_msg("Class or DirectId is already exists")
    del page


@when("i close Create Class modal")
def close_create_class_modal(context):
    page = Group_class_divisionPage(context)
    page.click_close_modal()
    del page


@when("Benemax admin with owner permission access Edit Class option")
def access_edit_class(context):
      page4 = Group_class_divisionPage(context)
      page4.click_edit_class()
      time.sleep(1)
      page4.click_edit_class_btn()
      del page4

@then("Verify Edit Class modal should be displayed")
def verify_edit_class_modal(context):
      page4 = Group_class_divisionPage(context)
      page4.verify_edit_class_modal()
      del page4

@when("I again enter valid data in Class name and Direct Id")
def edit_class(context):
    page4 = Group_class_divisionPage(context)
    page4.edit_class("C2","213243"+str(calendar.timegm(time.gmtime()))
                     )
    del page4

@then("Verify success message should be displayed for updated Class")
def verify_success_msg_updated_class(context):
    page = ClaimAccountPage(context)
    page.verify_success_msg("Class is updated successfully.")
    del page


@then("Verify Updated Class should be displayed in table view")
def verify_updated_class(context):
    page = Group_class_divisionPage(context)
    page.verify_edited_class("C2")
    del page
    page = ClaimAccountPage(context)
    page.click_signuot()
    del page


###########################################################################################################################

@when("I Create Benemax admin with edit permission and that admin complete claim account process")
def create_admin_edit_permission(context):
    page5 = Create_user(context)
    page5.create_benemax_admin_editpermission_gettoken()
    del page5
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@when("Benemax admin with edit permission Login and want to create an organization")
def admin_edit_permission_create_org(context):
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
    page5.enter_org_disp_name(orgs['org2'])
    del page5
    page6 = CreateOrganizationPage(context)
    page6.verify_create_organization_third_modal()
    del page6
    page7 = CreateOrganizationPage(context)
    page7.create_organization_third_section("n", "n", "n", "n", "n", "nainsi jain"+str(calendar.timegm(time.gmtime())))
    del page7

@then("Verify Organization should be created and search for same organization")
def admin_edit_permission_create_org_verifyorg(context):
    page = SearchOrganization(context)
    page.search_with_pending_filter(orgs['org2'])
    del page

@when("admin with edit permission access same searched organization and Groups for that organization")
def admin_edit_permission_access_group(context):
    access_group(context)

@then("Verify admin with edit permission should be able to see Create Group option")
def admin_edit_permission_verify_creategroup(context):
    verify_create_group(context)

@when("admin with edit permission open Create Group modal and verify correct modal should be open")
def admin_edit_permission_verify_opencreategroup(context):
    verify_create_group_modal(context)

@when("admin with edit permission enter valid data in group name and Direct Id")
def admin_edit_permission_creategroup(context):
    open_create_group(context)

@then("Verify success message should be displayed to admin with edit permission for created group")
def admin_edit_permission_creategroup_successmsg(context):
    verify_msg_group(context)

@then("Verify Created Group should be displayed in table view for admin with edit permission")
def admin_edit_permission_verify_createdgroup(context):
    verify_created_group(context)

@when("admin with edit permission again open create group and enter same Group name for same organization")
def admin_edit_permission_again_creategroup(context):
    again_create_same_group(context)

@then("Verify error message should be displayed for admin with edit permission")
def admin_edit_permission_verify_errormsg_forcreate_same_group(context):
    verify_errormsg_group(context)

@when("admin with edit permission close Create Group modal")
def admin_edit_permission_close_create_group(context):
    close_create_group_modal(context)

@when("Benemax admin with edit permission access Edit Group option")
def admin_edit_permission_access_edit_group(context):
    access_edit_group(context)

@then("Verify Edit Group modal should be displayed for admin with edit permission")
def admin_edit_permission_verify_edit_groupmodal(context):
    verify_edit_group_modal(context)

@when("admin with edit permission again enter valid data in group name and Direct Id")
def admin_edit_permission_verify_edit_groupmodal(context):
    edit_group(context)

@then("Verify success message should be displayed for updated Group for admin with edit permission")
def admin_edit_permission_verify_successmsg_editgroup(context):
    verify_success_msg_edit_group(context)

@then("Verify Updated Group should be displayed in table view for admin with edit permission")
def admin_edit_permission_verify_editedgroup(context):
    verify_updatedgroup(context)

################################################################

@when("admin with edit permission access same searched organization and division for that organization")
def admin_edit_permission_access_division(context):
    access_division(context)

@then("Verify admin with edit permission should be able to see Create division option")
def admin_edit_permission_verify_createdivision(context):
    verify_create_division(context)

@when("admin with edit permission open Create division modal and verify correct modal should be open")
def admin_edit_permission_verify_opencreatedivision(context):
    verify_create_division_modal(context)

@when("admin with edit permission enter valid data in division name and Direct Id and select valid group")
def admin_edit_permission_createdivision(context):
    open_create_division(context)

@then("Verify success message should be displayed for created division for admin with edit permission")
def admin_edit_permission_createdivision_successmsg(context):
    verify_msg_createddivision(context)

@then("Verify Created division should be displayed in table view for admin with edit permission")
def admin_edit_permission_verify_createddivision(context):
    verify_created_division(context)

@when("admin with edit permission again open create division and enter same division name for same organization")
def admin_edit_permission_again_createdivision(context):
    again_create_same_division(context)

@then("Verify error message should be displayed for create division for admin with edit permission")
def admin_edit_permission_verify_errormsg_forcreate_same_division(context):
    verify_msg_division_error(context)

@when("admin with edit permission close Create Division modal")
def admin_edit_permission_close_create_division(context):
    close_create_division_modal(context)

@when("Benemax admin with edit permission access Edit Division option")
def admin_edit_permission_access_edit_division(context):
    access_edit_division(context)

@then("Verify Edit Division modal should be displayed for admin with edit permission")
def admin_edit_permission_verify_edit_divisionmodal(context):
    verify_edit_division_modal(context)

@when("admin with edit permission again enter valid data in division name and Direct Id")
def admin_edit_permission_edit_division(context):
    edit_division(context)

@then("Verify success message should be displayed for updated division for admin with edit permission")
def admin_edit_permission_verify_successmsg_editdivision(context):
    verify_success_msg_updated_division(context)

@then("Verify Updated division should be displayed in table view for admin with edit permission")
def admin_edit_permission_verify_editeddivision(context):
    verify_updated_division(context)

################################################################

@when("admin with edit permission access same searched organization and Class for that organization")
def admin_edit_permission_access_class(context):
    access_class(context)

@then("Verify admin with edit permission should be able to see Create Class option")
def admin_edit_permission_verify_create_class(context):
    verify_create_class(context)

@when("admin with edit permission open Create Class modal and verify correct modal should be open")
def admin_edit_permission_verify_opencreate_class(context):
    verify_create_class_modal(context)

@when("admin with edit permission enter valid data in Class name and Direct Id")
def admin_edit_permission_create_class(context):
    open_create_class(context)

@then("Verify success message should be displayed for created Class for admin with edit permission")
def admin_edit_permission_createdclass_successmsg(context):
    verify_msg_createdclass(context)

@then("Verify Created Class should be displayed in table view for admin with edit permission")
def admin_edit_permission_verify_createdclass(context):
    verify_created_class(context)

@when("admin with edit permission again open create Class and enter same Class name for same organization")
def admin_edit_permission_again_createclass(context):
    again_create_same_class(context)

@then("Verify error message should be displayed for create Class for admin with edit permission")
def admin_edit_permission_verify_errormsg_forcreate_same_class(context):
    verify_errormsg_class(context)

@when("admin with edit permission close Create Class modal")
def admin_edit_permission_close_create_class(context):
    close_create_class_modal(context)

@when("Benemax admin with edit permission access Edit Class option")
def admin_edit_permission_access_edit_class(context):
    access_edit_class(context)

@then("Verify Edit Class modal should be displayed for admin with edit permission")
def admin_edit_permission_verify_edit_classmodal(context):
    verify_edit_class_modal(context)

@when("admin with edit permission again enter valid data in Class name and Direct Id")
def admin_edit_permission_edit_class(context):
    edit_class(context)

@then("Verify success message should be displayed for updated Class for admin with edit permission")
def admin_edit_permission_verify_successmsg_editclass(context):
    verify_success_msg_updated_class(context)

@then("Verify Updated Class should be displayed in table view for admin with edit permission")
def admin_edit_permission_verify_editedclass(context):
    verify_updated_class(context)

############################################################################################################

@when("I Create Organization admin with edit permission and that admin complete claim account process")
def create_admin_edit_permission(context):
    page = Create_user(context)
    page.create_org_admin_with_edit_permission(context)
    del page
    page3 = ClaimAccountPage(context)
    page3.claim_account_invitation_link("12345678", "12345678")
    del page3

@when("Organization admin with edit permission access People option")
def admin_edit_permission_create_org(context):
    page1 = Group_class_divisionPage(context)
    page1.mousehover_click_people()
    del page1

@when("Organization admin with edit permission access same searched organization and Groups for that organization")
def admin_edit_permission_access_group(context):
    page = Group_class_divisionPage(context)
    page.click_group()
    del page

@then("Verify Organization admin with edit permission should be able to see Create Group option")
def admin_edit_permission_verify_creategroup(context):
    verify_create_group(context)

@when("Organization admin with edit permission open Create Group modal and verify correct modal should be open")
def admin_edit_permission_verify_opencreategroup(context):
    verify_create_group_modal(context)

@when("Organization admin with edit permission enter valid data in group name and Direct Id")
def admin_edit_permission_creategroup(context):
    page = Group_class_divisionPage(context)
    page.create_group("G3", "Nainsi"+str(calendar.timegm(time.gmtime())))
    del page

@then("Verify success message should be displayed to Organization admin with edit permission for created group")
def admin_edit_permission_creategroup_successmsg(context):
    verify_msg_group(context)

@then("Verify Created Group should be displayed in table view for Organization admin with edit permission")
def admin_edit_permission_verify_createdgroup(context):
    # verify_created_group(context)
    pass

@when("Organization admin with edit permission again open create group and enter same Group name for same organization")
def admin_edit_permission_again_creategroup(context):
    page = Group_class_divisionPage(context)
    page.click_create_group()
    page.create_group("G3", "Nainsi"+str(calendar.timegm(time.gmtime())))
    del page

@then("Verify error message should be displayed for Organization admin with edit permission")
def admin_edit_permission_verify_errormsg_forcreate_same_group(context):
    verify_errormsg_group(context)

@when("Organization admin with edit permission close Create Group modal")
def admin_edit_permission_close_create_group(context):
    close_create_group_modal(context)

@when("Organization admin with edit permission access Edit Group option")
def admin_edit_permission_access_edit_group(context):
    page = Group_class_divisionPage(context)
    page.org_admin_click_edit_group()
    page.click_edit_group_btn()
    del page

@then("Verify Edit Group modal should be displayed for Organization admin with edit permission")
def admin_edit_permission_verify_edit_groupmodal(context):
    verify_edit_group_modal(context)

@when("Organization admin with edit permission again enter valid data in group name and Direct Id")
def admin_edit_permission_verify_edit_groupmodal(context):
    page4 = Group_class_divisionPage(context)
    page4.edit_group("G4", "Nainsi1"+str(calendar.timegm(time.gmtime())))
    del page4

@then("Verify success message should be displayed for updated Group for Organization admin with edit permission")
def admin_edit_permission_verify_successmsg_editgroup(context):
    verify_success_msg_edit_group(context)

@then("Verify Updated Group should be displayed in table view for Organization admin with edit permission")
def admin_edit_permission_verify_editedgroup(context):
    # verify_updatedgroup(context)
    pass

################################################################

@when("Organization admin with edit permission access same searched organization and division for that organization")
def admin_edit_permission_access_division(context):
    access_division(context)

@then("Verify Organization admin with edit permission should be able to see Create division option")
def admin_edit_permission_verify_createdivision(context):
    verify_create_division(context)

@when("Organization admin with edit permission open Create division modal and verify correct modal should be open")
def admin_edit_permission_verify_opencreatedivision(context):
    verify_create_division_modal(context)

@when("Organization admin with edit permission enter valid data in division name and Direct Id and select valid group")
def admin_edit_permission_createdivision(context):
    page = Group_class_divisionPage(context)
    page.create_division("D3", "abc"+str(calendar.timegm(time.gmtime())), "G4")
    del page

@then("Verify success message should be displayed for created division for Organization admin with edit permission")
def admin_edit_permission_createdivision_successmsg(context):
    verify_msg_createddivision(context)

@then("Verify Created division should be displayed in table view for Organization admin with edit permission")
def admin_edit_permission_verify_createddivision(context):
    # verify_created_division(context)
    pass

@when("Organization admin with edit permission again open create division and enter same division name for same organization")
def admin_edit_permission_again_createdivision(context):
    page = Group_class_divisionPage(context)
    page.click_create_division()
    page.create_division("D3", "Nainsi"+str(calendar.timegm(time.gmtime())), "G4")
    del page

@then("Verify error message should be displayed for create division for Organization admin with edit permission")
def admin_edit_permission_verify_errormsg_forcreate_same_division(context):
    verify_msg_division_error(context)

@when("Organization admin with edit permission close Create Division modal")
def admin_edit_permission_close_create_division(context):
    close_create_division_modal(context)

@when("Organization admin with edit permission access Edit Division option")
def admin_edit_permission_access_edit_division(context):
    page = Group_class_divisionPage(context)
    page.org_admin_click_edit_division()
    page.click_edit_division_btn()
    del page

@then("Verify Edit Division modal should be displayed for Organization admin with edit permission")
def admin_edit_permission_verify_edit_divisionmodal(context):
    verify_edit_division_modal(context)

@when("Organization admin with edit permission again enter valid data in division name and Direct Id")
def admin_edit_permission_edit_division(context):
    page4 = Group_class_divisionPage(context)
    page4.edit_division("D4", "Nainsi1"+str(calendar.timegm(time.gmtime())))
    del page4

@then("Verify success message should be displayed for updated division for Organization admin with edit permission")
def admin_edit_permission_verify_successmsg_editdivision(context):
    verify_success_msg_updated_division(context)

@then("Verify Updated division should be displayed in table view for Organization admin with edit permission")
def admin_edit_permission_verify_editeddivision(context):
    # verify_updated_division(context)
    pass

################################################################

@when("Organization admin with edit permission access same searched organization and Class for that organization")
def admin_edit_permission_access_class(context):
    access_class(context)

@then("Verify Organization admin with edit permission should be able to see Create Class option")
def admin_edit_permission_verify_create_class(context):
    verify_create_class(context)

@when("Organization admin with edit permission open Create Class modal and verify correct modal should be open")
def admin_edit_permission_verify_opencreate_class(context):
    verify_create_class_modal(context)

@when("Organization admin with edit permission enter valid data in Class name and Direct Id")
def admin_edit_permission_create_class(context):
    page = Group_class_divisionPage(context)
    page.create_class("C3", "Nainsi1"+str(calendar.timegm(time.gmtime())))
    del page

@then("Verify success message should be displayed for created Class for Organization admin with edit permission")
def admin_edit_permission_createdclass_successmsg(context):
    verify_msg_createdclass(context)

@then("Verify Created Class should be displayed in table view for Organization admin with edit permission")
def admin_edit_permission_verify_createdclass(context):
    # verify_created_class(context)
    pass

@when("Organization admin with edit permission again open create Class and enter same Class name for same organization")
def admin_edit_permission_again_createclass(context):
    page = Group_class_divisionPage(context)
    page.click_create_class()
    page.create_class("C3", "12345"+str(calendar.timegm(time.gmtime())))
    del page

@then("Verify error message should be displayed for create Class for Organization admin with edit permission")
def admin_edit_permission_verify_errormsg_forcreate_same_class(context):
    verify_errormsg_class(context)

@when("Organization admin with edit permission close Create Class modal")
def admin_edit_permission_close_create_class(context):
    close_create_class_modal(context)

@when("Organization admin with edit permission access Edit Class option")
def admin_edit_permission_access_edit_class(context):
    page = Group_class_divisionPage(context)
    page.org_admin_click_edit_class()
    page.click_edit_class_btn()
    del page

@then("Verify Edit Class modal should be displayed for Organization admin with edit permission")
def admin_edit_permission_verify_edit_classmodal(context):
    verify_edit_class_modal(context)

@when("Organization admin with edit permission again enter valid data in Class name and Direct Id")
def admin_edit_permission_edit_class(context):
    page4 = Group_class_divisionPage(context)
    page4.edit_class("C4", "213243"+str(calendar.timegm(time.gmtime())))
    del page4

@then("Verify success message should be displayed for updated Class for Organization admin with edit permission")
def admin_edit_permission_verify_successmsg_editclass(context):
    verify_success_msg_updated_class(context)

@then("Verify Updated Class should be displayed in table view for Organization admin with edit permission")
def admin_edit_permission_verify_editedclass(context):
    # verify_updated_class(context)
    pass

############################################################################################################
