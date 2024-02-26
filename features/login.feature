Feature: Logging API
  An API to handle all of your logging needs

  Scenario: Getting Application ID
    Given I am a Logging user
    And I have an application name
    When I request an application ID
    Then I should get an application ID