Feature: When User wants to change his Password
  Scenario: User wants to update his Password via Change Password option
    When I create Benemax admin with owner permission and he completes claim account process to change password
    When User access Change Password option
    When User enter valid data in all fields and update his Password
    Then Verify success message should be displayed to User when password updated successfully

  Scenario: User wants to Login with old Password
    When User wants to Login with old Password
    Then Verify error message should be displayed to User when he wants to Login with Old Password

  Scenario: User wants to Login with newly updated Password
    When User wants to Login with newly updated Password
    Then Verify User should be redirected on Admin dashboard