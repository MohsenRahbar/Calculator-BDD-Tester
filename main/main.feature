# check all functionalities all at once
Feature: main

  Scenario: add and subtract numbers

    Given there are two  numbers
    When perform addition and subtraction operation
    Then the results should be correct
