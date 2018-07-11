Feature: Create Program
  Scenario: When Benemax admin with owner permission create Program in Pending State
    When Benemax admin with owner permission create an organization in pending state and access it
    When Benemax admin with owner permission create group, class and division for that pending state organization
    When Benemax admin with owner permission access Program for that pending state organization
    When Benemax admin with owner permission access Create Program for that pending state organization
    Then Verify correct create program modal should be open for Benemax admin with owner permission
    When Benemax admin with owner permission Create Pending state Program for that pending state organization
    Then Verify success message should be displayed after Program creation for Benemax admin with owner permission
    Then Verify Program should be displayed in Pending state to Benemax admin with owner permission and it's status should be Active in table view
    When Benemax admin with owner permission deactivate that Pending state Program
    Then Verify Program should be displayed from pending state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view
    When Benemax admin with owner permission activate Program from deactivate state which is previously in Pending state
    Then Again Verify Program should be displayed in Pending state to Benemax admin with owner permission

  Scenario: When Benemax admin with owner permission Edit Program and Assign it into Open enrollment state
    When Benemax admin with owner permission edit that Pending state Program and assign it to open enrollment state
    Then Verify Program should be displayed in Open Enrollment state to Benemax admin with owner permission and it's status should be Active in table view
    When Benemax admin with owner permission deactivate that Open enrollment state Program
    Then Verify Program should be displayed from Open enrollment state to deactive state for Benemax admin with owner permission and it's status should be deactive in table view
    When Benemax admin with owner permission activate Program from deactivate state which is previously in Open Enrollment state
    Then Again Verify Program should be displayed in Open Enrollment state to Benemax admin with owner permission

  Scenario: When Benemax admin with owner permission assign Program to Active state
    When I open database and change Enrollment start date and Enrollment end date of recently edited Program
    Then Verify Program should be displayed in Active state to Benemax admin with owner permission and it's status should be Active in table view
    When Benemax admin with owner permission deactivate that Active state Program
    Then Verify Program should be displayed from Active to deactive state for Benemax admin with owner permission and it's status should be deactive in table view
    When Benemax admin with owner permission activate Program from deactivate state which is previously in Active state
    Then Again Verify Program should be displayed in Active state to Benemax admin with owner permission

  Scenario: When Benemax admin with owner permission archive particular program
    When I open database and change All the dates of recently edited Program
    Then Verify Program should be displayed in Archive state to Benemax admin with owner permission
    Then Verify Program status should be show as Active in table view

##################################################################################################################################


  Scenario: When Benemax admin with Edit permission create Program in Pending State
    When Benemax admin with owner permission change his permission from owner to Edit
    When Benemax admin with Edit permission access Program for that same pending state organization
    When Benemax admin with Edit permission access Create Program for that pending state organization
    Then Verify correct create program modal should be open for Benemax admin with Edit permission
    When Benemax admin with Edit permission Create Pending state Program for that pending state organization
    Then Verify success message should be displayed after Program creation for Benemax admin with Edit permission
    Then Verify Program should be displayed in Pending state to Benemax admin with Edit permission and it's status should be Active in table view
    When Benemax admin with Edit permission deactivate that Pending state Program
    Then Verify Program should be displayed from pending state to deactive state for Benemax admin with Edit permission and it's status should be deactive in table view
    When Benemax admin with Edit permission activate Program from deactivate state which is previously in Pending state
    Then Again Verify Program should be displayed in Pending state to Benemax admin with Edit permission

  Scenario: When Benemax admin with Edit permission Edit Program and Assign it into Open enrollment state
    When Benemax admin with Edit permission edit that Pending state Program and assign it to open enrollment state
    Then Verify Program should be displayed in Open Enrollment state to Benemax admin with Edit permission and it's status should be Active in table view
    When Benemax admin with Edit permission deactivate that Open enrollment state Program
    Then Verify Program should be displayed from Open enrollment state to deactive state for Benemax admin with Edit permission and it's status should be deactive in table view
    When Benemax admin with Edit permission activate Program from deactivate state which is previously in Open Enrollment state
    Then Again Verify Program should be displayed in Open Enrollment state to Benemax admin with Edit permission

  Scenario: When Benemax admin with Edit permission assign Program to Active state
    When Benemax admin with Edit permission open database and change Enrollment start date and Enrollment end date of recently edited Program
    Then Verify Program should be displayed in Active state to Benemax admin with Edit permission and it's status should be Active in table view
    When Benemax admin with Edit permission deactivate that Active state Program
    Then Verify Program should be displayed from Active to deactive state for Benemax admin with Edit permission and it's status should be deactive in table view
    When Benemax admin with Edit permission activate Program from deactivate state which is previously in Active state
    Then Again Verify Program should be displayed in Active state to Benemax admin with Edit permission

  Scenario: When Benemax admin with Edit permission archive particular program
    When Benemax admin with Edit permission open database and change All the dates of recently edited Program
    Then Verify Program should be displayed in Archive state to Benemax admin with Edit permission
    Then Verify Program status should be show as Active in table view for Benemax admin with Edit permission

