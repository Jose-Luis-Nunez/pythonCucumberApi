Feature: Caratlane Login

  Scenario: Login to caratlane with valid parameters
    Given Launching chrome browser
    When Open caratlane Login page
    And  Enter userName "xxxxxxxx6@caratlane.com"
    And  click continue to login button
    And  Enter Password "YYYYYY"
    And  click on the Login button
    Then User must logined successfully