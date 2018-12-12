# Program Description:     Python Data Functions
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015

# Setup a function that takes in two values
def addtwonumbers(numberonepassedin, numbertwopassedin):

    # Return the sum of the two numbers
    return numberonepassedin + numbertwopassedin



# Setup a function that takes in variadic parameters
def addtwonumbers(*numberspassedin):
    total = 0
    # Iterate the numbers passed in and total their values
    for numberin in numberspassedin:
        total = total + numberin

    # Return the sum of the numbers passed in
    return total


print('The sum of the numbers 100 and 200 is: %d' % addtwonumbers(100, 200))
print('The sum of the numbers -100, -200 and 300 is: %d' % addtwonumbers(-100, -200, 300))
print('The sum of the numbers -100, 200, 300 and 600 is: %d' % addtwonumbers(-100, 200, 300, 600))