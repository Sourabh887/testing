Feature: Benemax admin with owner permission create Employee and Organization admin for an active orgnization

  Scenario:Benemax admin with owner permission create an employee
    When Benemax admin with owner permission create an organzation and activate it
    When Benemax admin with owner permission access same organization and create group class and division for that organization
    Then Verify Create an Employee option should be visible if admin access employee tab
    When Benemax admin access create an employee option
    Then Verify correct modal should be displayed to create an employee
    When Benemax admin create an employee
    When i search for same employee and select pending filter
    Then Veirfy employee should be displayed in table view and status should be Pending
    Then that created employee completed claim account process
    Then Employee access switch role and verify Employee role should be visible
    When Employee signout from existing account and Benemax admin with owner permission again login
    Then Benemax admin with owner permission again access same active organization for Employee
    Then Verify Employee status should be show as Active


  Scenario:Benemax admin with owner permission create an organization admin
    When Benemax admin access create an employee option to create organization admin
    Then Verify correct modal should be displayed to create an organization admin
    When Benemax admin with owner permission again create Organization admin for same active organization
    When i search for same organization admin and select pending filter
    Then Veirfy organization admin should be displayed in table view and status should be Pending
    Then that created organization admin completed claim account process
    Then Organization admin access switch role and verify Organization admin role should be visible
    When Organization admin signout from existing account and Benemax admin with owner permission again login
    Then Benemax admin with owner permission again access same active organization for Organization admin
    Then Verify Organization admin status should be show as Active

  Scenario:Benemax admin with owner permission create an organization admin and Employee
    When Benemax admin access create an employee option to create organization admin and Employee
    Then Verify correct modal should be displayed to create an employee and organization admin
    When Benemax admin with owner permission again create Organization admin and Employee for same active organization
    When i search for same organization admin and employee and select pending filter
    Then Veirfy organization admin and admin should be displayed in table view and status should be Pending
    Then that created organization admin and Employee completed claim account process
    Then Organization admin and Employee access switch role and verify Organization admin and employee both role should be visible
    When Organization admin and Employee signout from existing account and Benemax admin with owner permission again login
    Then Benemax admin with owner permission again access same active organization for organization admin and Employee
    Then Verify Organization admin and Employee status should be show as Active

  Scenario: Benemax admin with owner permission Edit Employee role and deactivate him for active organization
    When Benemax admin with owner permission Edit that Employee and give up his permission from Organization admin and make him only as Employee
    When Benemax admin with owner permission logout and edited employee Login and verify his role in switch role
    When Benemax admin with owner permission deactivate that Edited Employee
    Then Verify employee should show in deactivate state

  Scenario: When Benemax admin with owner permission associate same Employee to any active organization
    When Benemax admin with owner permission Create new Organization and activate it and signout from existing account
    When Benemax admin with owner permission create same Employee to Organization admin and Employee for an active organization
    When Created employee and Organization admin switch role and verify Organization name in header
    When Benemax admin with owner permission again Login and activate employee for previous organization and verify his status as active
    When Benemax admin with owner permission go back and deactivate second organization in which user is associated
    Then Edited Employee Login and access switch role,Verify only Employee role should be visible and in header correct organization should be visible
    When Benemax admin with owner permission deactivate previous organization

  Scenario: When Employee try to Login and both organizations are deactivated in which he is associated
    When Employee try to Login for the condition in which both the organizations are deactivated
    Then verify error message should be displayed and employee should not be able to Login