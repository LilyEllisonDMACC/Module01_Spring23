"""
Program: casting_assignment.py
Author: Lily B Ellison
Last date modified: 01/14/2023
The purpose of this program is to accept any input,
convert to an integer type and output the integer.

"""

#Accepts user input as string
user_input = input('Please enter a number: ')

#Casts user input to a float - When I tried skipping this step, I got an error when I entered '6.7'
input_to_float = float(user_input)

#Casts float to an integer
float_to_integer = int(input_to_float)

#Outputs the input as an integer
print(float_to_integer)


# Input   Expected Output  Actual Output
#    5          5                5
#   6.7         6                6
#  'somestr'   Error            ValueError: could not convert string to float: 'somestr'
#    -5         -5               -5
#   3.14         3                3
#  'a number'   Error            ValueError: could not convert string to float: 'a number'
#     0           0                0