Feature: When User wants to update his details from account details option

  Scenario: When Benemax admin update his details from account details option
    When I create new Benemax admin and he completes claim account process
    When Benemax admin access account details option from dropdown
    Then verify correct modal should be open to Benemax admin
    When Benemax admin enter valid details in all fields and change his email and update his details
    Then verify Username should be updated on header for benemax admin

  Scenario: When Benemax admin wants to Login with old email
    When Benemax admin signout from existing account and wants to Login with old email
    Then verify error message should be displayed for Benemax admin
    When Benemax admin wants to Login with newly updated Email
    Then veriy Benemax admin should be able to Login with newly updated Email

  Scenario: When Organization admin update his details from account details option
    When I create new Organization admin and he completes claim account process
    When Organization admin access account details option from dropdown
    Then verify correct modal should be open to Organization admin
    When Organization admin enter valid details in all fields and change his email and update his details
    Then verify Username should be updated on header for Organization admin

  Scenario: When Organization admin wants to Login with old email
    When Organization admin signout from existing account and wants to Login with old email
    Then verify error message should be displayed for Organization admin
    When Organization admin wants to Login with newly updated Email
    Then veriy Organization admin should be able to Login with newly updated Email
#
  Scenario: When Employee update his details from account details option
    When I create new Employee and he completes claim account process
    When Employee access account details option from dropdown
    Then verify correct modal should be open to Employee
    When Employee enter valid details in all fields and change his email and update his details
    Then verify Username should be updated on header for Employee

  Scenario: When Employee wants to Login with old email
    When Employee signout from existing account and wants to Login with old email
    Then verify error message should be displayed for Employee
    When Employee wants to Login with newly updated Email
    Then veriy Employee should be able to Login with newly updated Email


