Feature: Forgot and Reset Password

    Scenario: When User forgot his Password and want to get link on Email to reset his Password
        When I Create an user and complete claim account process
        Then I access Login and want to access forgot Password link
        When I enter registered email to get reset password link on provided email
        Then Success message should be displayed and link is sent on provided email

    Scenario: When User Reset his Password and Login with old Password
        When User access reset Password link sent on his email
        Then User should be able to reset his Password
        Then Verify success message should be displayed
        When User want to Login with old Password
        Then Verify error message should be displayed and User is not able to Login


    Scenario: When User Reset his Password and Login with newly updated Password
        When User want to Login with newly updated password
        Then Verify User should be able to Login and redirected on dashboard

