# Program Description:     Python Data Functions
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015

# Setup an array
myClaimValues = (2000, 3000, 5000, 1500, 1900, 1000)


# Setup a function that returns a value - a value function
def readordernumber():
    """Ask the user to input the first Order number"""
    print('')
    ordernumber = input('What is the Order number:  ')

    # Return a value
    return ordernumber


# Setup a function that returns a value - a value function
def claimvaluetotal():
    totalofclaims = 0
    for claimvalue in myClaimValues:
        totalofclaims = totalofclaims + claimvalue

    # Return the value for the total of the claims
    return totalofclaims


# We will call the function and assign the returned value to a variable
indexNumberOfRequest = int(readordernumber())

print("The value of the order is: %d " % myClaimValues[indexNumberOfRequest])

print("The total value of the claims is: %d " % claimvaluetotal())
