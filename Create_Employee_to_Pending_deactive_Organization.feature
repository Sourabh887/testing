Feature: Benemax admin with owner permission create Employee and Organization admin for Pending orgnization

  Scenario:Benemax admin with owner permission create an employee for Pending Organization
    When Benemax admin with owner permission create an organzation and search it in Pending filter
    When Benemax admin with owner permission access same pending organization and create group class and division for that organization
    Then Verify Create an Employee option should be visible for pending organization if admin access employee tab
    When Benemax admin access create an employee option for pending organization
    Then Verify correct modal should be displayed to create an employee for pending organization
    When Benemax admin create an employee for pending organization
    When i search for same employee and select pending filter for pending organization
    Then Veirfy employee should be displayed in table view and status should be Pending for pending organization


  Scenario:Benemax admin with owner permission create an organization admin for Pending Organization
    When Benemax admin access create an employee option to create organization admin for pending organization
    Then Verify correct modal should be displayed to create an organization admin for pending organization
    When Benemax admin with owner permission again create Organization admin for for pending organization
    When i search for same organization admin and select pending filter for pending organization
    Then Veirfy organization admin should be displayed in table view and status should be Pending for pending organization


  Scenario:Benemax admin with owner permission create an organization admin and Employee for Pending Organization
    When Benemax admin access create an employee option to create organization admin and Employee for pending organization
    Then Verify correct modal should be displayed to create an employee and organization admin for pending organization
    When Benemax admin with owner permission again create Organization admin and Employee for for pending organization
    When i search for same organization admin and employee and select pending filter for pending organization
    Then Veirfy organization admin and admin should be displayed in table view and status should be Pending for pending organization

  Scenario:Benemax admin with owner permission Edit Employee for Pending Organization
    When Benemax admin access Edit employee option to Edit organization admin and Employee for pending organization
    Then Verify correct modal should be displayed to Edit employee and organization admin for pending organization
    When Benemax admin with owner permission Edit User and give up his permission from Organization admin for pending organization
    Then Verify Employee status should be displayed in pending in table view for Pending Organization


  #################################################################################################################

  Scenario:Benemax admin with owner permission create an employee for deactivate Organization
    When Benemax admin go back and search same Organization and activate it
    When Benemax admin search Organization in active filter and deactivate it and access it
    Then Verify Create an Employee option should be visible for deactivate Organization if admin access employee tab
    When Benemax admin access create an employee option for deactivate Organization
    Then Verify correct modal should be displayed to create an employee for deactivate Organization
    When Benemax admin create an employee for deactivate Organization
    When i search for same employee and select pending filter for deactivate Organization
    Then Veirfy employee should be displayed in table view and status should be Pending for deactivate Organization


  Scenario:Benemax admin with owner permission create an organization admin for deactivate Organization
    When Benemax admin access create an employee option to create organization admin for deactivate Organization
    Then Verify correct modal should be displayed to create an organization admin for deactivate Organization
    When Benemax admin with owner permission again create Organization admin for for deactivate Organization
    When i search for same organization admin and select pending filter for deactivate Organization
    Then Veirfy organization admin should be displayed in table view and status should be Pending for deactivate Organization


  Scenario:Benemax admin with owner permission create an organization admin and Employee for deactivate Organization
    When Benemax admin access create an employee option to create organization admin and Employee for deactivate Organization
    Then Verify correct modal should be displayed to create an employee and organization admin for deactivate Organization
    When Benemax admin with owner permission again create Organization admin and Employee for for deactivate Organization
    When i search for same organization admin and employee and select pending filter for deactivate Organization
    Then Veirfy organization admin and admin should be displayed in table view and status should be Pending for deactivate Organization

  Scenario:Benemax admin with owner permission Edit Employee for deactivate Organization
    When Benemax admin access Edit employee option to Edit organization admin and Employee for deactivate Organization
    Then Verify correct modal should be displayed to Edit employee and organization admin for deactivate Organization
    When Benemax admin with owner permission Edit User and give up his permission from Organization admin for deactivate Organization
    Then Verify Employee status should be displayed in pending in table view for deactivate Organization


