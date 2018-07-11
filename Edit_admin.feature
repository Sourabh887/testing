Feature: Edit Admin

    Scenario: When Benemax admin want to edit another Benemax admin with same permission that he has
        Given I create Benemax admin with owner permission
        When Created Benemax admin complete claim account process
        Then Verify admin should be redirected to Dashboard view
        When I Signout from existing admin accuont and again login as Benemax admin with owner permission
        When I search for an admin with owner permission
        When I edit details of benemax admin with owner permission and without changing permission enter correct data in all fields and submit details
        Then Verify admin should be edited and displayed in table view
        Then Verify admin should be edited as in activate state
        When admin signout from existing account and wants to Login with old email
        Then verify admin should not be able to Login
        When admin wants to Login with newly updated email and password
        Then verify admin should be able to Login with newly updated email and Password

    Scenario: When Benemax admin want to edit another Benemax admin with owner permission and change his permission to edit
        When Benemax admin Login and search for an admin with owner permission
        When I open edit modal to change permission of already existing admin from owner to edit
        Then Verify correct edit modal for admin should be open
        When admin edit details and change admin permission from owner to edit
        Then Verify admin should be still displayed in table view
        When I Signout from existing admin accuont and again login as Benemax admin with edit permission
        Then Verify only organization view should be displayed to admin and administrator view should not be displayed
        When Benemax admin with edit permission signout from existing account
        Then Benemax admin with owner permission again Login to change permission of another admin who has edit permission

    Scenario: When Benemax admin want to edit another Benemax admin with edit permission and change his permission to read
        When Benemax admin Login and search for an admin with edit permission
        When I open edit modal to change permission of already existing admin from edit to read
        Then Verify correct edit modal for admin with edit permission should be open
        When admin edit details and change admin permission from edit to read
        Then Verify admin should be still displayed in table view with active status
        When I Signout from existing admin accuont and again login as Benemax admin with read permission
        Then Verify only organization view should be displayed to admin



