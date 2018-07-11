Feature: Benemax admin create, Edit, activate and deactivate Benefit
  Scenario: When Benemax admin with owner permission create Benefit in Pending State
    When Benemax admin with owner permission create an organization in pending state to create Benefit and access it
    When Benemax admin with owner permission create group, class and division to create Benefit for that pending state organization
    When Benemax admin with owner permission access Program for that pending state organization to create Benefit
    When Benemax admin with owner permission access Create Program for that pending state organization to create Benefit
    Then Verify correct create program modal should be open for Benemax admin with owner permission to create Benefit
    When Benemax admin with owner permission Create Pending state Program for that pending state organization to create Benefit
    Then Verify success message should be displayed after Program creation for Benemax admin with owner permission to create Benefit
    Then Verify Program should be displayed in Pending state to Benemax admin with owner permission and it's status should be Active in table view to create Benefit
    When Benemax admin with owner permission access that Pending state Program to create Benefit
    Then Verify Benemax admin with owner permission should redirect to Benefit Dashboard
    When Benemax admin with owner permission access create a benefit option
    Then Verify correct create a benefit modal should be open for Benemax admin with owner permission
    When Benemax admin with owner permission create benefit in which line of coverage type is medical
    Then Verify success message should be displayed after Benefit creation in which loc type is medical for Benemax admin with owner permission
    Then Verify Benefit in which loc type is medical should be displayed in Pending state to Benemax admin with owner permission and it's status should be Active in table view and loc should be medical insurance
    When Benemax admin with owner permission deactivate that Pending state Benefit in which loc type is medical
    Then Verify Benefit in which loc type is medical should be displayed from pending state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view
    When Benemax admin with owner permission activate Benefit in which loc type is medical from deactivate state which is previously in Pending state
    Then Again Verify Benefit in which loc type is medical should be displayed in Pending state and medical insurance type benefit to Benemax admin with owner permission

#
  Scenario: When Benemax admin with owner permission Edit Benefit in which loc type is medical
    When Benemax admin with owner permission access Edit Benefit option for the Benefit in which loc type is medical
    Then Verify correct edit benefit modal should be open for Benemax admin with owner permission in which loc type is medical
    When Benemax admin with owner permission edit Benefit on first slide in which loc type is medical
    Then Verify success message should be displayed on first slide for Benefit in which loc type is medical
    When Benemax admin with owner permission edit Benefit on second slide in which loc type is medical
    Then Verify success message should be displayed on second slide for Benefit in which loc type is medical
    When Benemax admin with owner permission edit Benefit on third slide in which loc type is medical
    Then Verify success message should be displayed on third slide for Benefit in which loc type is medical
    When Benemax admin with owner permission edit Benefit on fourth slide in which loc type is medical
    Then Verify success message should be displayed on fourth slide for Benefit in which loc type is medical
    When Benemax admin with owner permission close Edit Benefit modal for medical insurance type of Benefit


  Scenario: When Benemax admin with owner permission Edit Program and Assign it into Open enrollment state and then create Benefit in it
    When Benemax admin with owner permission edit that Pending state Program and assign it to open enrollment state to create Benefit
    Then Verify Program should be displayed in Open Enrollment state to Benemax admin with owner permission and it's status should be Active in table view to create Benefit
    When Benemax admin with owner permission access that open enrollment state Program to create Benefit
    Then Verify Benemax admin with owner permission should redirect to Benefit Dashboard to create Dental Insurance type of Benefit
    When Benemax admin with owner permission access create a benefit option to create Dental Insurance type of Benefit
    Then Verify correct create a benefit modal should be open for Benemax admin with owner permission to create Dental Insurance type of Benefit
    When Benemax admin with owner permission create benefit in which line of coverage type is Dental
    Then Verify success message should be displayed after Benefit creation in which loc type is Dental for Benemax admin with owner permission
    Then Verify Benefit in which loc type is Dental should be displayed in Dental Insurance state to Benemax admin with owner permission and it's status should be Active in table view
    When Benemax admin with owner permission deactivate that Dental Insurance state Benefit in which loc type is Dental
    Then Verify Benefit in which loc type is Dental should be displayed Dental Insurance state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view
    When Benemax admin with owner permission activate Benefit in which loc type is Dental from deactivate state
    Then Again Verify Benefit in which loc type is Dental should be displayed in Dental insurance type benefit to Benemax admin with owner permission

  Scenario: When Benemax admin with owner permission Edit Benefit in which loc type is Dental
    When Benemax admin with owner permission access Edit Benefit option for the Benefit in which loc type is Dental
    Then Verify correct edit benefit modal should be open for Benemax admin with owner permission in which loc type is Dental
    When Benemax admin with owner permission edit Benefit on first slide in which loc type is Dental
    Then Verify success message should be displayed on first slide for Benefit in which loc type is Dental
    When Benemax admin with owner permission edit Benefit on second slide in which loc type is Dental
    Then Verify success message should be displayed on second slide for Benefit in which loc type is Dental
    When Benemax admin with owner permission edit Benefit on third slide in which loc type is Dental
    Then Verify success message should be displayed on third slide for Benefit in which loc type is Dental
    When Benemax admin with owner permission edit Benefit on fourth slide in which loc type is Dental
    Then Verify success message should be displayed on fourth slide for Benefit in which loc type is Dental
    When Benemax admin with owner permission close Edit Benefit modal for Dental insurance type of Benefit

  Scenario: When Benemax admin with owner permission Edit Program and Assign it into Active state and then create Benefit in it
    When Benemax admin with owner permission edit that Open enrollment state Program and assign it to Active state to create Benefit
    Then Verify Program should be displayed in Active state to Benemax admin with owner permission and it's status should be Active in table view to create Benefit
    When Benemax admin with owner permission access that Active state Program to create Benefit
    Then Verify Benemax admin with owner permission should redirect to Benefit Dashboard to create Vision Insurance type of Benefit
    When Benemax admin with owner permission access create a benefit option to create Vision Insurance type of Benefit
    Then Verify correct create a benefit modal should be open for Benemax admin with owner permission to create Vision Insurance type of Benefit
    When Benemax admin with owner permission create benefit in which line of coverage type is Vision
    Then Verify success message should be displayed after Benefit creation in which loc type is Vision for Benemax admin with owner permission
    Then Verify Benefit in which loc type is Vision should be displayed in Vision Insurance state to Benemax admin with owner permission and it's status should be Active in table view
    When Benemax admin with owner permission deactivate that Vision Insurance state Benefit in which loc type is Vision
    Then Verify Benefit in which loc type is Vision should be displayed Vision Insurance state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view
    When Benemax admin with owner permission activate Benefit in which loc type is Vision from deactivate state
    Then Again Verify Benefit in which loc type is Vision should be displayed in Vision insurance type benefit to Benemax admin with owner permission

  Scenario: When Benemax admin with owner permission Edit Benefit in which loc type is Vision
    When Benemax admin with owner permission access Edit Benefit option for the Benefit in which loc type is Vision
    Then Verify correct edit benefit modal should be open for Benemax admin with owner permission in which loc type is Vision
    When Benemax admin with owner permission edit Benefit on first slide in which loc type is Vision
    Then Verify success message should be displayed on first slide for Benefit in which loc type is Vision
    When Benemax admin with owner permission edit Benefit on second slide in which loc type is Vision
    Then Verify success message should be displayed on second slide for Benefit in which loc type is Vision
    When Benemax admin with owner permission edit Benefit on third slide in which loc type is Vision
    Then Verify success message should be displayed on third slide for Benefit in which loc type is Vision
    When Benemax admin with owner permission edit Benefit on fourth slide in which loc type is Vision
    Then Verify success message should be displayed on fourth slide for Benefit in which loc type is Vision
    When Benemax admin with owner permission close Edit Benefit modal for Vision insurance type of Benefit
#
  Scenario: When Benemax admin with owner permission Edit Program and Assign it into Active state and then create Ancillary Benefit in it
    When Benemax admin with owner permission edit that Open enrollment state Program and assign it to Active state to create Ancillary Benefit
    Then Verify Program should be displayed in Active state to Benemax admin with owner permission and it's status should be Active in table view to create Ancillary Benefit
    When Benemax admin with owner permission access that Active state Program to create Ancillary Benefit
    Then Verify Benemax admin with owner permission should redirect to Benefit Dashboard to create Ancillary Insurance type of Benefit
    When Benemax admin with owner permission access create a benefit option to create Ancillary Insurance type of Benefit
    Then Verify correct create a benefit modal should be open for Benemax admin with owner permission to create Ancillary Insurance type of Benefit
    When Benemax admin with owner permission create benefit in which line of coverage type is Ancillary
    Then Verify success message should be displayed after Benefit creation in which loc type is Ancillary for Benemax admin with owner permission
    Then Verify Benefit in which loc type is Ancillary should be displayed in Ancillary Insurance state to Benemax admin with owner permission and it's status should be Active in table view
    When Benemax admin with owner permission deactivate that Ancillary Insurance state Benefit in which loc type is Ancillary
    Then Verify Benefit in which loc type is Ancillary should be displayed in Ancillary Insurance state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view
    When Benemax admin with owner permission activate Benefit in which loc type is Ancillary from deactivate state
    Then Again Verify Benefit in which loc type is Ancillary should be displayed in Ancillary insurance type benefit to Benemax admin with owner permission

  Scenario: When Benemax admin with owner permission Edit Benefit in which loc type is Ancillary
    When Benemax admin with owner permission access Edit Benefit option for the Benefit in which loc type is Ancillary
    Then Verify correct edit benefit modal should be open for Benemax admin with owner permission in which loc type is Ancillary
    When Benemax admin with owner permission edit Benefit on first slide in which loc type is Ancillary
    Then Verify success message should be displayed on first slide for Benefit in which loc type is Ancillary
    When Benemax admin with owner permission edit Benefit on second slide in which loc type is Ancillary
    Then Verify success message should be displayed on second slide for Benefit in which loc type is Ancillary
    When Benemax admin with owner permission edit Benefit on third slide in which loc type is Ancillary
    Then Verify success message should be displayed on third slide for Benefit in which loc type is Ancillary
    When Benemax admin with owner permission close Edit Benefit modal for Ancillary insurance type of Benefit


###################################################################################################################################

  Scenario: When Benemax admin with edit permission Edit Program and Assign it into Active state and then create fsa Benefit in it
    When Benemax admin with edit permission edit that Open enrollment state Program and assign it to Active state to create fsa Benefit
    Then Verify Program should be displayed in Active state to Benemax admin with edit permission and it's status should be Active in table view to create Ancillary Benefit
    When Benemax admin with edit permission access that Active state Program to create fsa Benefit
    Then Verify Benemax admin with owner permission should redirect to Benefit Dashboard to create fsa Insurance type of Benefit
    When Benemax admin with edit permission access create a benefit option to create fsa Insurance type of Benefit
    Then Verify correct create a benefit modal should be open for Benemax admin with edit permission to create fsa Insurance type of Benefit
    When Benemax admin with edit permission create benefit in which line of coverage type is fsa
    Then Verify success message should be displayed after Benefit creation in which loc type is fsa for Benemax admin with edit permission
    Then Verify Benefit in which loc type is fsa should be displayed in fsa Insurance state to Benemax admin with edit permission and it's status should be Active in table view
    When Benemax admin with edit permission deactivate that fsa Insurance state Benefit in which loc type is fsa
    Then Verify Benefit in which loc type is fsa should be displayed fsa Insurance state to deactive state for Benemax admin with edit permission and it's status should be deactive in table view
    When Benemax admin with edit permission activate Benefit in which loc type is fsa from deactivate state
    Then Again Verify Benefit in which loc type is fsa should be displayed in fsa insurance type benefit to Benemax admin with edit permission

  Scenario: When Benemax admin with edit permission Edit Benefit in which loc type is fsa
    When Benemax admin with edit permission access Edit Benefit option for the Benefit in which loc type is fsa
    Then Verify correct edit benefit modal should be open for Benemax admin with edit permission in which loc type is fsa
    When Benemax admin with edit permission edit Benefit on first slide in which loc type is fsa
    Then Verify success message should be displayed on first slide for Benefit in which loc type is fsa
    When Benemax admin with owner permission edit Benefit on second slide in which loc type is fsa
    Then Verify success message should be displayed on second slide for Benefit in which loc type is fsa
    When Benemax admin with owner permission edit Benefit on third slide in which loc type is fsa
    Then Verify success message should be displayed on third slide for Benefit in which loc type is fsa
    When Benemax admin with edit permission close Edit Benefit modal for fsa insurance type of Benefit