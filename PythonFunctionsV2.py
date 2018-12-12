# Program Description:     Python Data Functions
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015 

from array import *

myOrders = [2001,2005,2050,3165];

orderNumberInput = 0;
  
def GetOrderDetails():
    """ Prints All Order Numbers"""
    # Display order numbers in the array.
    for theOrder in myOrders:
        print(theOrder);
        

GetOrderDetails();
