Feature: When Benemax admin wants to switch his role as Organization admin and Employee

  Scenario: When Benemax admin with owner permission Edit himself and change his permission
    When I create Benemax admin with owner permission and he completes claim account process
    When Benemax admin with owner permission create new Benemax admin
    Then Verify only Edit admin option should be displayed for pending state Benemax admin
    When Benemax admin edit that pending state Benemax admin and change his name
    Then Verify name should be updated in table view
    When Benemax admin search himself and change his permission from owner to edit
    Then Verify only Organization view should be displayed to Benemax admin

  Scenario: Benemax admin make himself Organization admin and Employee for an active Organization
    When Benemax admin with Edit permission create new Organization and activate it
    When Benemax admin make himslef Employee and Organization admin with Edit permission
    Then Verify admin should show as in active state in table view
#
  Scenario: When Benemax admin switch his role as Organization admin
    When Benemax admin with Edit permission access switch role as Organization admin
    When Organization admin Create new Organization admin and Employee for his Organization
    Then Verify User should be displayed in pending state
    When Organization admin Edit him and change his permission as read for Organization admin
    When Organization admin search himself and change his permission from Edit to Read
    Then Verify Only Read view should be displayed to Organization admin
#
  Scenario: When Organization admin switch role as Benemax admin
    When another Benemax admin with Owner permission Login and change Benemax amdin permission to Read
    When Benemax admin with owner permission signout and Benemax admin with Read permission Login
    When Organization admin access switch role and switch role as Benemax admin
    When Benemax admin search same Organization
    Then Verify only View Organization option should be displayed
    When Benemax admin with Edit permission access View Organization option
    Then Verify correct modal should be displayed
#
  Scenario: When Benemax admin with permission switch role as Employee
    When Benemax admin with Read Permission access switch role
    When Benemax admin access Employee role
    Then Verify he should redirect to Employee Dashboard
