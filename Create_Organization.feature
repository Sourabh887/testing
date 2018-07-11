Feature: Create Organization

    Scenario: When Benemax admin want to create an organization
        When I open create organization modal
        Then Verify correct modal should be open
        When I enter correct data in all fields on first section and continue the process
        Then Verify I redirected on second section
        When I enter Organization display name and continue process
        Then Verify I redirected on third section
        When I enter correct data in all fields on third section and finish the process
        Then Verify Organization should be created successfully
