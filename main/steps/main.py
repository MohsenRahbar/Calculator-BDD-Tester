"""
    Check all functionalities all at once
"""
from behave import given, when, then
import addition , subtraction

# First step :
@given(u'I have two numbers')
def set_numbers(context):
    """
        set result
    """

    context.first_number = 10
    context.second_number = 4

# Second step :
@when(u'I add and subtract the numbers')
def perform_operations(context):
    """
        to give first number and second number
    """
    # Check addition :
    context.addition = addition.calculate_addition(context.first_number, context.second_number)

    # Check subtraction :
    context.subtraction = subtraction.calculate_subtraction(context.first_number, context.second_number)

# Third step :
@then(u'the results should be correct')
def check_results(context):
    """
        check addition
        check subtraction
    """

    assert context.addition == 14
    assert context.subtraction == 6
