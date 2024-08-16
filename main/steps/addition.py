"""
    Addition two number
"""
from behave import given , when , then


# First steps :
@given(u'there are two  numbers')
def set_numbers(context):
    """
	    The set of result Numbers
    """

    context.first_number = 10
    context.second_number = 4


# Second steps :
@when(u'addition two numbers for addition')
def calculate_addition(context):
    """
	    The calculate addition of result
    """

    context.sum = context.first_number + context.second_number

# Third step :

@then(u'the result equal 14')
def check_result(context):
    """
	    Check result
    """

    assert context.sum == 14
