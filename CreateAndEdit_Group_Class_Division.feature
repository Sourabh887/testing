Feature: Create and Edit Group Class and Division For Benemax admin owner and Edit Permission

    Scenario: When Benemax admin with owner permission want to create Group
        When Benemax admin with owner permission Login and want to create an organization
        Then Verify Organization created and search for same organization
        When admin access same searched organization and Groups for that organization
        Then Verify admin with owner permission should be able to see Create Group option
        When I open Create Group modal and verify correct modal should be open
        When I enter valid data in group name and Direct Id
        Then Verify success message should be displayed for created group
        Then Verify Created Group should be displayed in table view
        When I again open create group and enter same Group name for same organization
        Then Verify error message should be displayed
        When i close Create Group modal


    Scenario: When Benemax admin with owner permission want to Edit Group
        When Benemax admin with owner permission access Edit Group option
        Then Verify Edit Group modal should be displayed
        When I again enter valid data in group name and Direct Id
        Then Verify success message should be displayed for updated Group
        Then Verify Updated Group should be displayed in table view

    Scenario: When Benemax admin with owner permission want to create Division
        When admin access same searched organization and division for that organization
        Then Verify admin with owner permission should be able to see Create division option
        When I open Create division modal and verify correct modal should be open
        When I enter valid data in division name and Direct Id and select valid group
        Then Verify success message should be displayed for created division
        Then Verify Created division should be displayed in table view
        When I again open create division and enter same division name for same organization
        Then Verify error message should be displayed for create division
        When i close Create Division modal

    Scenario: When Benemax admin with owner permission want to Edit Division
        When Benemax admin with owner permission access Edit Division option
        Then Verify Edit Division modal should be displayed
        When I again enter valid data in division name and Direct Id
        Then Verify success message should be displayed for updated division
        Then Verify Updated division should be displayed in table view

    Scenario: When Benemax admin with owner permission want to create class
        When admin access same searched organization and Class for that organization
        Then Verify admin with owner permission should be able to see Create Class option
        When I open Create Class modal and verify correct modal should be open
        When I enter valid data in Class name and Direct Id
        Then Verify success message should be displayed for created Class
        Then Verify Created Class should be displayed in table view
        When I again open create Class and enter same Class name for same organization
        Then Verify error message should be displayed for create Class
        When i close Create Class modal

    Scenario: When Benemax admin with owner permission want to Edit Class
        When Benemax admin with owner permission access Edit Class option
        Then Verify Edit Class modal should be displayed
        When I again enter valid data in Class name and Direct Id
        Then Verify success message should be displayed for updated Class
        Then Verify Updated Class should be displayed in table view


###########################################################################################################

    Scenario: When Benemax admin with edit permission want to create Group
        When I Create Benemax admin with edit permission and that admin complete claim account process
        When Benemax admin with edit permission Login and want to create an organization
        Then Verify Organization should be created and search for same organization
        When admin with edit permission access same searched organization and Groups for that organization
        Then Verify admin with edit permission should be able to see Create Group option
        When admin with edit permission open Create Group modal and verify correct modal should be open
        When admin with edit permission enter valid data in group name and Direct Id
        Then Verify success message should be displayed to admin with edit permission for created group
        Then Verify Created Group should be displayed in table view for admin with edit permission
        When admin with edit permission again open create group and enter same Group name for same organization
        Then Verify error message should be displayed for admin with edit permission
        When admin with edit permission close Create Group modal


    Scenario: When Benemax admin with edit permission want to Edit Group
        When Benemax admin with edit permission access Edit Group option
        Then Verify Edit Group modal should be displayed for admin with edit permission
        When admin with edit permission again enter valid data in group name and Direct Id
        Then Verify success message should be displayed for updated Group for admin with edit permission
        Then Verify Updated Group should be displayed in table view for admin with edit permission

    Scenario: When Benemax admin with edit permission want to create Division
        When admin with edit permission access same searched organization and division for that organization
        Then Verify admin with edit permission should be able to see Create division option
        When admin with edit permission open Create division modal and verify correct modal should be open
        When admin with edit permission enter valid data in division name and Direct Id and select valid group
        Then Verify success message should be displayed for created division for admin with edit permission
        Then Verify Created division should be displayed in table view for admin with edit permission
        When admin with edit permission again open create division and enter same division name for same organization
        Then Verify error message should be displayed for create division for admin with edit permission
        When admin with edit permission close Create Division modal

    Scenario: When Benemax admin with edit permission want to Edit Division
        When Benemax admin with edit permission access Edit Division option
        Then Verify Edit Division modal should be displayed for admin with edit permission
        When admin with edit permission again enter valid data in division name and Direct Id
        Then Verify success message should be displayed for updated division for admin with edit permission
        Then Verify Updated division should be displayed in table view for admin with edit permission

    Scenario: When Benemax admin with edit permission want to create class
        When admin with edit permission access same searched organization and Class for that organization
        Then Verify admin with edit permission should be able to see Create Class option
        When admin with edit permission open Create Class modal and verify correct modal should be open
        When admin with edit permission enter valid data in Class name and Direct Id
        Then Verify success message should be displayed for created Class for admin with edit permission
        Then Verify Created Class should be displayed in table view for admin with edit permission
        When admin with edit permission again open create Class and enter same Class name for same organization
        Then Verify error message should be displayed for create Class for admin with edit permission
        When admin with edit permission close Create Class modal

    Scenario: When Benemax admin with edit permission want to Edit Class
        When Benemax admin with edit permission access Edit Class option
        Then Verify Edit Class modal should be displayed for admin with edit permission
        When admin with edit permission again enter valid data in Class name and Direct Id
        Then Verify success message should be displayed for updated Class for admin with edit permission
        Then Verify Updated Class should be displayed in table view for admin with edit permission


###########################################################################################################

    Scenario: When Organization admin with edit permission want to create Group
        When I Create Organization admin with edit permission and that admin complete claim account process
        When Organization admin with edit permission access People option
        When Organization admin with edit permission access same searched organization and Groups for that organization
        Then Verify Organization admin with edit permission should be able to see Create Group option
        When Organization admin with edit permission open Create Group modal and verify correct modal should be open
        When Organization admin with edit permission enter valid data in group name and Direct Id
        Then Verify success message should be displayed to Organization admin with edit permission for created group
        Then Verify Created Group should be displayed in table view for Organization admin with edit permission
        When Organization admin with edit permission again open create group and enter same Group name for same organization
        Then Verify error message should be displayed for Organization admin with edit permission
        When Organization admin with edit permission close Create Group modal


    Scenario: When Organization admin with edit permission want to Edit Group
        When Organization admin with edit permission access Edit Group option
        Then Verify Edit Group modal should be displayed for Organization admin with edit permission
        When Organization admin with edit permission again enter valid data in group name and Direct Id
        Then Verify success message should be displayed for updated Group for Organization admin with edit permission
        Then Verify Updated Group should be displayed in table view for Organization admin with edit permission

    Scenario: When Organization admin with edit permission want to create Division
        When Organization admin with edit permission access same searched organization and division for that organization
        Then Verify Organization admin with edit permission should be able to see Create division option
        When Organization admin with edit permission open Create division modal and verify correct modal should be open
        When Organization admin with edit permission enter valid data in division name and Direct Id and select valid group
        Then Verify success message should be displayed for created division for Organization admin with edit permission
        Then Verify Created division should be displayed in table view for Organization admin with edit permission
        When Organization admin with edit permission again open create division and enter same division name for same organization
        Then Verify error message should be displayed for create division for Organization admin with edit permission
        When Organization admin with edit permission close Create Division modal

    Scenario: When Organization admin with edit permission want to Edit Division
        When Organization admin with edit permission access Edit Division option
        Then Verify Edit Division modal should be displayed for Organization admin with edit permission
        When Organization admin with edit permission again enter valid data in division name and Direct Id
        Then Verify success message should be displayed for updated division for Organization admin with edit permission
        Then Verify Updated division should be displayed in table view for Organization admin with edit permission

    Scenario: When Organization admin with edit permission want to create class
        When Organization admin with edit permission access same searched organization and Class for that organization
        Then Verify Organization admin with edit permission should be able to see Create Class option
        When Organization admin with edit permission open Create Class modal and verify correct modal should be open
        When Organization admin with edit permission enter valid data in Class name and Direct Id
        Then Verify success message should be displayed for created Class for Organization admin with edit permission
        Then Verify Created Class should be displayed in table view for Organization admin with edit permission
        When Organization admin with edit permission again open create Class and enter same Class name for same organization
        Then Verify error message should be displayed for create Class for Organization admin with edit permission
        When Organization admin with edit permission close Create Class modal

    Scenario: When Organization admin with edit permission want to Edit Class
        When Organization admin with edit permission access Edit Class option
        Then Verify Edit Class modal should be displayed for Organization admin with edit permission
        When Organization admin with edit permission again enter valid data in Class name and Direct Id
        Then Verify success message should be displayed for updated Class for Organization admin with edit permission
        Then Verify Updated Class should be displayed in table view for Organization admin with edit permission

