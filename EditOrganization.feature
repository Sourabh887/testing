Feature: Edit Organization

    Scenario: When Benemax admin want to edit an organization
        When I create an organization with pending state
        When I search for an orgaization which is pending
        When I open edit organization modal
        Then Verify edit organization modal should be open
        When I enter correct data in all fields on first section and go to second section
        When I enter Organization display name and go on third section
        When I enter correct data in all fields on third section and save changes
        Then Verify Organization should be updated successfully

    Scenario: When Benemax admin activate or deactivate any Organization
         When I open Activate/Deactivate organization modal to activate an Organization
         Then Verify Activate/Deactivate modal should be open
         When I choose Yes option to activate an Organization
         Then organization should be activated Successfully
         Then verify Organization status should be show as active in list
         When I again open Activate/Deactivate organization modal to deactivate an organization
         Then Verify cctivate/deactivate modal should be open
         When I choose Yes option to deactivate an Organization
         Then organization should be deactivated Successfully
         Then verify Organization status should be show as deactive in list


