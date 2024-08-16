"""
    Subtract two numbers
"""
from behave import Given , When , Then


# First step :
@Given(u'there are two numbers for subtraction')
def set_numbers(context):
   """
       The set of result Numbers
   """

   context.first_number = 10
   context.second_number = 4


# Second step :
@When(u'subtract two numbers')
def calculate_subtraction(context):
    """
        The calculate subtract of result
    """

    context.subtract = context.first_number - context.second_number

# Third step :
@Then(u'the result equal 8')
def check_result(context):
    """
        Check result
    """
    assert context.divide == 8
