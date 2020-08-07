Feature: Test Calculator

  Scenario: Verify the addition of calculation
    Given user open calculator app
    When user input two numbers
    Then result is right


  Scenario: Verify the subtraction of calculation
    Given user open calculator app
    When user input number 100
    And user use minus
    And user input number 89
    And user calculate result
    Then result should be 11


  Scenario: Verify the multiplication of calculation
    Given user open calculator app
    When user input number 3
    And user use multiply
    And user input number 12
    And user calculate result
    Then result should be 36


  Scenario: Verify the division of calculation
    Given user open calculator app
    When user input number 36
    And user use divide
    And user input number 12
    And user calculate result
    Then result should be 3

   @test
   Scenario Outline: Verify the all kinds of calculation
    Given user open calculator app
    When user input number <numberA>
    And user use <operate>
    And user input number <numberB>
    And user calculate result
    Then result should be <resultNumber>

     Examples: addMinusDataTable
       | numberA | operate  | numberB | resultNumber|
       | 2       | add      | 3       | 5           |
       | 1       | add      | 3       | 4           |


     Examples: multiplyDivideDataTable
       | numberA | operate  | numberB | resultNumber|
       | 2       | multiply      | 3       | 6           |
       | 6       | divide      | 3       | 2           |
