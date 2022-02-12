"""A Lambda Function in Python programming is an anonymous function or a function having no name.
It is a small and restricted function having no more than one line.Just like a normal function, 
a Lambda function can have multiple arguments with one expression.
"""

### Definition example ###
"""Normal python function"""
def a_name(x):
    return x + x

"""Lambda function"""
lambda x: x + x

"""Let's see the example with scalar values, this is when 
you execute a lambda function on a single value
"""
(lambda x: x * 2)(12)  # 24


### Working with map() ###
"""In lambda functions we can use if and else statemets.The syntax of
lambda functions with conditional statements is:
lambda < argument >: < value1 > if < condtion1 > else < value2 > 
So, if condition 1 is True function'll return value1, otherwise it'll return value2

Let's write some lambda function with conditional statements
"""
list_numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, list_numbers)
print(list(squares))  # [1, 4, 9, 16]

### Working with conditional statements ###
"""In lambda functions we can use ifand else statemets.The syntax of
lambda functions with conditional statements is:
lambda <argument>: <value1> if <condtion1> else <value2> 
So, if condition 1 is True function'll return value1, otherwise it'll return value2

Let's write some lambda function with conditional statements
"""
check_number = lambda x: "Is positive or 0" if x >= 0 else "is negative"
print(check_number(1))  # Is positive or 0
print(check_number(-1))  # is negative


"""Elif - If you want to write elif,you should write nested else"""
check_number = (
    lambda x: "Is positive" if x > 0 else ("Is 0" if x == 0 else "Is negative")
)
print(check_number(1))  # Is positive or 0
print(check_number(-1))  # Is negative
print(check_number(0))  # Is 0

### Lambda functions with 2+ arguments ###
"""Lambda functions can have more than one argument, let's see the example"""
full_name = (
    lambda first_name, last_name: f"Full name: {first_name.title()} {last_name.title()}"
)
full_name("Sasha", "Ajintarev") # Full name: Sasha Ajintarev

