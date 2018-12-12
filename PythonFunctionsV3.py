# Program Description:     Python Data Functions
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015 

from array import *

myOrders = [20000,30000,40000,50000];
orderNumberInput = 0;
  
def GetOrderDetails():
    """ Prints All Order Numbers"""
    # Display order numbers in the array.
    for theOrder in myOrders:
        print(theOrder);
    orderNumberInput = input('Enter the order number:  ');
    
    for theOrder in myOrders:
        # In the next kline we convert the string input to an int
        # We use the input value to print only the array item that matches this value
       if theOrder == int(orderNumberInput):
            print(theOrder);       

GetOrderDetails();
