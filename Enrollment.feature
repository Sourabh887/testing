Feature: Employee enroll in all available Benefits which satisfied Group, class and Divison criteria
  Scenario: Benemax admin associate himself as an employee in active organization
    When I Create Benemax admin with owner permission and he logged in and create organization and activate it
    When Benemax admin associate himself in that active Organization
    Then Verify Benemax admin as an employee should be show in active state for that active Organization

  Scenario: When there is no Program on Employee Dashboard
    When Benemax admin switch his role as Employee
    Then Verify default message should be display when there is no Program on Dashboard

  Scenario: Benemax admin make Organization and create Programs and all types of Benefits in it.
    When Employee switch his role back as Benemax admin
    When Benemax admin access same Organization to Create open Enrollment Program in it
    When Benemax admin with owner permission create Program for open enrollment state
    When Benemax admin with owner permission create all types of Benefits in that Program
    Then Verify all types of Benefits should be displayed in that Program

  Scenario: Benemax admin as an Employee access Open Enrollment program
    When Benemax admin with Owner permission access switch role
    When Benemax admin switch his role as an employee
    Then Verify Program should be displayed on Dashboard
    When Benemax admin as an employee access that particular Program
    Then Verify he should reidrected Program start screen

  Scenario: Benemax admin as an Employee update Primary details
    When Benemax admin as an employee access get started option for open enrollment Program
    Then Veirfy he should redircted to members screen
    When Benemax admin as an employee access start option on members start screen
    Then Verify he should redirected to Employee and dependents screen
    When employee fill valid data in all fields provided and access update option
    Then verify success message should be displayed when we update primary

  Scenario:Benemax admin as an employee add each type of Dependent
    When Benemax admin as an employee access add dependent option
    Then Verify he should be able to see add dependent page
    When employee fill valid data in all fields provided and access add dependent option
    Then verify success message should be displayed when we add dependents
    When employee access cancel option and access yes option on popup showing for the last added dependent
    When employee again filled valid data in all fields provided to update dependent
    Then verify scuccess message should be displayed when employee update dependent

  Scenario: Benemax admin as an employee remove particular dependent and want to add same dependent again
    When Benemax admin as an employee remove particular dependent
    Then Verify success message should be displayed when dependent deleted successfully
    When Benemax admin as an employee try to add same dependent again
    Then Verify success message should be displayed when employee added same dependent again
    When Employee access save and continue option after adding dependents
    Then Verify employee should redirect to medical insurance start screen
    When employee access start option on medical insurance start screen
    Then Verify he should redirect to medical insurance screen

  Scenario: Benemax admin as an employee choose no option for medical Benefit
    When employee choose no option for the first question of Medical Benefit
    Then Verify he should be able to see second question of Medical Benefit
    When employee firstly choose any option apart from other for second question of medical Benefit
    When employee hit save and continue option for medical insurance screen
    Then Verify he should redirect to Dental insurance first screen
    When employee access start option on dental insurance start screen
    Then Verify he should redirect to dental insurance screen

  Scenario: Benemax admin as an employee choose no option for Dental Benefit
    When employee choose no option for the first question of Dental Benefit
    When employee hit save and continue option and again come back on same medical insurance screen
    Then Verify correct selected option should be displayed to employee for medical insurance
    When employee choose other option for second question on medical Benefit
    When employee fill valid data in other option for medical insurance
    When employee access save and continue option on medical screen and again come back on same screen
    Then verify already filled data should be displayed in other option for medical insurance second question
    When employee hit save and continue on medical insurance screen to go on dental screen
    When employee hit save and continue option for dental insurance screen
    Then Verify he should redirect to Vision insurance first screen
    When employee access start option on Vision insurance start screen
    Then Verify he should redirect to Vision insurance screen
#
  Scenario: Benemax admin as an employee choose no option for Vision Benefit
    When employee choose no option for the first question of Vision Benefit
    When employee hit save and continue option and again come back on same dental insurance screen
    Then Verify correct selected option should be displayed to employee for dental insurance
    When employee hit save and continue on dental insurance screen to go on vision screen
    When employee hit save and continue option for Vision insurance screen
    Then Verify he should redirect to Ancillary insurance first screen
    When employee access start option on Ancillary insurance start screen
    Then Verify he should redirect to Ancillary insurance screen

  Scenario: Benemax admin as an employee choose no option for Ancillary Benefit
    When employee choose no option for the first question of Ancillary Benefit
    When employee hit save and continue option and again come back on same Vision insurance screen
    Then Verify correct selected option should be displayed to employee for Vision insurance
    When employee hit save and continue on vision insurance screen to go on ancillary screen
    When employee hit save and continue option for Ancillary insurance screen
    Then Verify he should redirect to FSA insurance first screen
    When employee access start option on FSA insurance start screen
    Then Verify he should redirect to FSA insurance screen

  Scenario: Benemax admin as an employee choose no option for FSA Benefit
    When employee choose no option for the first question of FSA Benefit
    When employee hit save and continue option and again come back on same Ancillary insurance screen
    Then Verify correct selected option should be displayed to employee for ancillary insurance
    When employee hit save and continue option for FSA insurance screen
    Then Verify he should redirect to review and submit enrollment screen
    Then Verify correct selected option should be displayed to employee for FSA insurance
    When employee hit save and continue on fsa insurance screen to go on review screen


  Scenario: On Review and submit enrollment screen, verify all the details of primary and dependent
    When employee verify primary details on review and submit enrollment screen
    Then Verify correct primary details should be displayed to employee
    When employee verify all the dependents details on review and submit enrollment screen
    Then Verify correct dependent details should be displayed to employee

  Scenario: On Review and submit enrollment screen, verify all the details when employee choose no option for each type of benefit to enroll
    When employee verify medical insurance when employee choose no option, on review and submit enrollment screen
    Then Verify default message should be displayed for medical insurance when employee choose no option, on review and submit enrollment screen
    When employee verify dental insurance when employee choose no option, on review and submit enrollment screen
    Then Verify default message should be displayed for dental insurance when employee choose no option, on review and submit enrollment screen
    When employee verify vision insurance when employee choose no option, on review and submit enrollment screen
    Then Verify default message should be displayed for vision insurance when employee choose no option, on review and submit enrollment screen
    When employee verify ancillary insurance when employee choose no option, on review and submit enrollment screen
    Then Verify default message should be displayed for ancillary insurance when employee choose no option, on review and submit enrollment screen
################Please uncomment this when issues get resolved on stage##########################3
#      When employee verify fsa insurance when employee choose no option, on review and submit enrollment screen
#      Then Verify default message should be displayed for fsa insurance when employee choose no option, on review and submit enrollment screen
#
  Scenario: employee access save and close on review and submit enrollment screen
    When employee access save and close option on review and submit enrollment screen
    Then Verify employee should redirect to employee dashboard

  Scenario: organization admin access Program to verify employee in enrollment table
    When employee switch role as organization admin to see that Program
    When organization admin access program from side bar
    When organization admin access particular program to see enrollment table
    When organization admin access enrollment tab to see enrollment table
    When organization admin apply incomplete enrollment filter
    When organization admin search for same employee to see incomplete enrollment
    Then Verify correct details should be display to organization admin in enrollment table
    Then Verify employee status should be incomplete in enrollment table
    When organization admin switch role as employee to enroll in that Program
    When employee access same Program again to choose yes option for all types of Benefits
    Then Verify employee should be able to see employee and dependents start screen


  Scenario: empoyee choose yes option for medical insurance Benefit
    When employee choose save and continue on all the screens and comes on medical insurance screen
    Then Verify employee should redirect to medical insurance screen to select yes option for it
    When employee choose yes option for the first question of Medical Benefit
    Then Verify he should be able to see second question of Medical Benefit when choose yes option
    Then Verify employee should be display in showing plans for, for the next question available on Medical Benefit

  Scenario: employee select different type of dependents to check correct text should be display for the next question available on Medical Benefit
    When employee select spouse dependent for medical insurance benefit
    Then Verify employee+spouse should be displayed in showing plans for, for the next question available on Medical Benefit
    When employee deselect spouse and select Dependent under (26) for medical insurance benefit
    Then Verify employee+child should be displayed in showing plans for, for the next question available on Medical Benefit
    When employee select Dependent under (26) and Disabled dependent for medical insurance benefit
    Then Verify employee+children should be display in showing plans for, for the next question available on Medical Benefit
    When employee select all the dependents available for medical insurance Benefit
    Then Verify employee+family should be display in showing plans for, for the next question available on Medical Benefit

  Scenario: employee select particular Plan for medical insurance Benefit
    Then Verify that employee should be able to see third question available for medical insurance Benefit
    Then Verify employee should be able to see Medical insurace plan details on plan container
    When employee access more information for medical insurance
    Then Verify correct information should be display on more information popup for medical insurance Benefit
    When employee close more information popup for medical insurance Benefit
    When employee choose specific plan for medical insurance Benefit
    Then Verify employee should be able to see fourth question for medical insurance Benefit

  Scenario: employee fill details for all the primary care physicians available for medical insurance Benefit
    Then Verify that employee should be able to see first primary care physician for medical insurance Benefit
    When employee fill details for first primary care physician for medical insurance Benefit
    When employee fill details for second primary care physician for medical insurance Benefit
    When employee fill details for third primary care physician for medical insurance Benefit
    When employee fill details for fourth primary care physician for medical insurance Benefit
    When employee fill details for fifth primary care physician for medical insurance Benefit
    When employee fill details for sixth primary care physician for medical insurance Benefit
    When employee fill details for seventh primary care physician for medical insurance Benefit
    When employee choose Save and continue option on medical insurance when choose yes option
    Then Verify employee should redirect to Dental insurance screen to select yes option for it

  Scenario: empoyee choose yes option for dental insurance Benefit
    When employee choose yes option for the first question of Dental Benefit
    Then Verify he should be able to see second question of Dental Benefit when choose yes option
    Then Verify employee should be display in showing plans for, for the next question available on Dental Benefit

  Scenario: employee select different type of dependents to check correct text should be display for the next question available on Dental Benefit
    When employee select spouse dependent for Dental insurance benefit
    Then Verify employee+spouse should be displayed in showing plans for, for the next question available on Dental Benefit
    When employee deselect spouse and select Dependent under (26) for Dental insurance benefit
    Then Verify employee+child should be displayed in showing plans for, for the next question available on Dental Benefit
    When employee select Dependent under (26) and Disabled dependent for Dental insurance benefit
    Then Verify employee+children should be display in showing plans for, for the next question available on Dental Benefit
    When employee select all the dependents available for Dental insurance Benefit
    Then Verify employee+family should be display in showing plans for, for the next question available on Dental Benefit

  Scenario: employee select particular Plan for Dental insurance Benefit
    Then Verify that employee should be able to see third question available for Dental insurance Benefit
    Then Verify employee should be able to see Dental insurace plan details on plan container
    When employee access more information for Dental insurance
    Then Verify correct information should be display on more information popup for Dental insurance Benefit
    When employee close more information popup for Dental insurance Benefit
    When employee choose specific plan for Dental insurance Benefit
    When employee choose Save and continue option on Dental insurance when choose yes option
    Then Verify employee should redirect to Vision insurance screen to select yes option for it

  Scenario: empoyee choose yes option for vision insurance Benefit
    When employee choose yes option for the first question of Vision Benefit
    Then Verify he should be able to see second question of Vision Benefit when choose yes option
    Then Verify employee should be display in showing plans for, for the next question available on Vision Benefit

  Scenario: employee select different type of dependents to check correct text should be display for the next question available on Vision Benefit
    When employee select spouse dependent for Vision insurance benefit
    Then Verify employee+spouse should be displayed in showing plans for, for the next question available on Vision Benefit
    When employee deselect spouse and select Dependent under (26) for Vision insurance benefit
    Then Verify employee+child should be displayed in showing plans for, for the next question available on Vision Benefit
    When employee select Dependent under (26) and Disabled dependent for Vision insurance benefit
    Then Verify employee+children should be display in showing plans for, for the next question available on Vision Benefit

  Scenario: employee select particular Plan for Vision insurance Benefit
    Then Verify that employee should be able to see third question available for Vision insurance Benefit
    Then Verify employee should be able to see Vision insurace plan details on plan container
    When employee access more information for Vision insurance
    Then Verify correct information should be display on more information popup for Vision insurance Benefit
    When employee close more information popup for Vision insurance Benefit
    When employee choose specific plan for Vision insurance Benefit
    When employee choose Save and continue option on Vision insurance when choose yes option
    Then Verify employee should redirect to Ancillary insurance screen to select yes option for it

  Scenario: empoyee choose yes option for ancillary insurance Benefit
    When employee choose yes option for the first question of Ancillary Benefit
    Then Verify he should be able to see second question of Ancillary Benefit when choose yes option

  Scenario: employee select particular Plan for Ancillary insurance Benefit
    Then Verify employee should be able to see Ancillary insurace plan details on plan container
    When employee access more information for Ancillary insurance
    Then Verify correct information should be display on more information popup for Ancillary insurance Benefit
    When employee close more information popup for Ancillary insurance Benefit
    Then Verify employee should be able to see third question on Ancillary insurance Benefit

  Scenario: employee fill primary and secondary beneficiaries for Ancillary insurance Benefit
    When employee add 6 primary beneficiaries which satisfied 100 percentage criteria
    When employee add 6 secondary beneficiaries which satisfied 100 percentage criteria
    When employee choose specific plan for Ancillary insurance Benefit
    When employee choose Save and continue option on Ancillary insurance when choose yes option
    Then Verify employee should redirect to FSA insurance screen to select yes option for it

#  Scenario: empoyee choose yes option for FSA insurance Benefit
#    When employee choose yes option for the first question of FSA Benefit
#    Then Verify he should be able to see second question of FSA Benefit when choose yes option
#    When employee fill valid data in contribution field for the second question of FSA Benefit
#    Then Verify he should be able to see third question of FSA Benefit when choose yes option
#    Then Verify correct information should be displayed in terms and condition field for fsa benefit
#    Then Verify terms and condition box should be checked
##
#  Scenario: employee verify fsa Plan detail
#    Then Verify employee should be able to see FSA insurace plan details on plan container
#    When employee access more information for FSA insurance
#    Then Verify correct information should be display on more information popup for FSA insurance Benefit
#    When employee close more information popup for FSA insurance Benefit
##
#  Scenario: employee access previous option on FSA screen
#    When employee access previous option on FSA screen
#    Then verify alert should be display to employee when access previuos option on FSA screen
#    When employee access yes option on the alert display for FSA insurance Benefit
#
#  Scenario: employee again choose yes option on fsa benefit and fill valid data in all fields provided
#    When employee again choose yes option for the first question of FSA Benefit
#    When employee again fill valid data in contribution field for the second question of FSA Benefit
#    Then Verify save and continue button should be display in enabled state
#    When employee hit save and continue on fsa screen
#    Then Verify employee should redirect to review screen to verify all the insurance selected options as yes

  Scenario: On Review and submit enrollment screen, verify all the details when employee choose yes option for each type of benefit to enroll
    When employee verify medical insurance when employee choose yes option, on review and submit enrollment screen
    Then Verify correct info should be displayed for medical insurance when employee choose yes option, on review and submit enrollment screen
    When employee verify dental insurance when employee choose yes option, on review and submit enrollment screen
    Then Verify correct info should be displayed for dental insurance when employee choose yes option, on review and submit enrollment screen
    When employee verify vision insurance when employee choose yes option, on review and submit enrollment screen
    Then Verify correct info should be displayed for vision insurance when employee choose yes option, on review and submit enrollment screen
    When employee verify ancillary insurance when employee choose yes option, on review and submit enrollment screen
    Then Verify correct info should be displayed for ancillary insurance when employee choose yes option, on review and submit enrollment screen

  #################Please uncomment this when issues get resolved#######################################
#    When employee verify fsa insurance when employee choose yes option, on review and submit enrollment screen
#    Then Verify correct info should be displayed for fsa insurance when employee choose yes option, on review and submit enrollment screen


################Please start to write code from here################################################
  Scenario: employee wants to submit an enrollment
    When employee hit submit enrollment button
    Then Verify employee should redirect to submission successful screen
    When employee hit finish button on submission successful screen
    Then Verify employee should redirect to dashboard and you're all caught up message should be display here

  Scenario: organization admin go on dashboard and verify correct count should be display to him for that particular program
    When employee switch role as organization admin to see that on dashboard correct count should be display for that perticular program
    Then verify correct count should be display to organization admin for that Program

   Scenario: organization admin access Program to verify employee's submitted status in enrollment table
     When organization admin access same Program to see enrollment table for employee's submitted status
     Then verify organization admin should redirect to enrollment table for employee's submitted status
     When organization admin apply submitted enrollment filter
     When organization admin search for same employee to see submitted enrollment
     Then Verify correct details should be display to organization admin in enrollment table for employee's submitted status
     When Organization admin access review and submission option for that particular employee
     Then verfiy he should redirect to review and submission screen to submit enrollmet of that particular employee

   Scenario: organization admin acces submit and process option to submit enrollment of that particular employee
     When organization admin access submit and process option on review screen
     Then Verify he should redirect to organization admin dashboard

   Scenario: Benemax admin wants to process enrollment for that particular employee
     When organization admin switch role as Benemax admin to process enrollment of that particular employee
     When Benemax admin search for same organization to see enrollment table
     When Benemax admin access Programs from side bar to see enrollment table
     When Benemax admin access enrollment tab to see enrollment table
     When Benemax admin apply approved enrollment filter
     When Benemax admin search for same employee to see approved enrollment
     Then Verify correct details should be display to Benemax admin in enrollment table
     Then Verify approved status should be display in enrollment table for that particular employee

   Scenario: Benemax admin acces process option to process enrollment of that particular employee
     When Benemax admin access process option on review screen
     Then Verify he should redirect to Benemax admin dashboard
     When Benemax admin search for same organization to see enrollment table and processed status
     When Benemax admin access Programs from side bar to see enrollment table and processed status
     When Benemax admin access enrollment tab to see enrollment table and processed status
     When Benemax admin apply processed enrollment filter
     When Benemax admin search for same employee to see processed enrollment
     Then Verify correct details should be display to Benemax admin in enrollment table for processed status
     Then Verify processed status should be display in enrollment table for that particular employee

#   Scenario: employee access your benefits section to see all types of past date enrollments
#     When Benemax admin switch role as employee to see your Benefits section
#     When employee access check your Benefits option from left menu
#     Then Verify he should redirected to your Benefits section
#     Then Verify by default no Benefits available message should be display here
#     Then verify by defaault today's date should be selected on your Benefits screen
#     When I change dates of Program and Benefits from database so that it can be visible under your Benefits
#     Then all the Benefits should be visible under your Benefits section
#     Then Verify correct details should be display for medical insurance Benefit under your Benefit section
#     Then Verify correct details should be display for dental insurance Benefit under your Benefit section
#     Then Verify correct details should be display for vision insurance Benefit under your Benefit section
#     Then Verify correct details should be display for ancillary insurance Benefit under your Benefit section
#     Then Verify correct details should be display for fsa insurance Benefit under your Benefit section


















