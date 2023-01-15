"""
Program: variable_assignment.py
Author: Lily B Ellison
Last date modified: 01/14/2023
The purpose of this program is set variables and print statement.
Constant value is imported from constants.py.

"""
#Module01 Topic02 Variable Assignment
#Declare 3 varibles: quantity (int), item (string), and size (float) and print quantity item "size" size
#Lily Ellison

#import value for constant (PRICE)
import constants

#set values for variables
quantity = int(13)
item = str('shoes')
size = float(10.5)

#print statement with variables cast as strings
print(str(quantity) + ' ' + item + ' size ' + str(size) + '.')

#print statement with variables and constant cast as strings
print(item + ' are $' +str(constants.PRICE) + '.')