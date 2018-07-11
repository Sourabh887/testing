Feature: Create Admin

    Scenario: When Benemax admin want to create another Benemax admin with same permission that he has
        When I open create admin modal
        Then Verify correct admin modal should be open
        When I enter correct data in all fields  and submit details
        Then Verify admin should be created and displayed in table view
        Then Verify admin should be created as in Pending state
        When Admin signuot from existing account
        When Admin create another Benemax admin with inactive status
        Then that created admin complete claim account process
        Then verify that created admin should show in table view
        Then verify that created admin should show in active state

     Scenario: When Benemax admin deactivate already active admin who has same permission as Benemax admin
         When Admin with owner permission deactivate already active admin
         Then Verify admin should still show in table view
         Then Verify admin should be show as Inactive state
