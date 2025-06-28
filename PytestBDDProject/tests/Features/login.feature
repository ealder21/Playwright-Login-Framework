
Feature: Login to try testing this app

  Scenario: Login with valid credentials

    Given The user has launched the browser and is on the login page
    When The users enters a valid username
    When The user enters a valid password
    When The user clicks on the login button
    Then The user should be logged in and be on the successful login screen