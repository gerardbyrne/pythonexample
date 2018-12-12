# Program Description:     Python Data Functions
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015

# Setup an array
myClaimValues = [2000, 3000, 5000, 1500, 1900, 1000, 6600]


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


# Setup a function that returns accepts a parameter and returns a value
def averageclaimvalue(totalofclaims, numberofclaims):
    averageclaimvalue = 0
    averageclaimvalue = totalofclaims / numberofclaims

    # Return the value for the total of the claims
    return averageclaimvalue


# We will call the function to find the average. We will pass in the
# two values reuired by the function
averagevalueofmyclaims = averageclaimvalue(14400, 6)

print("The average value of the claims is: %d " % averagevalueofmyclaims)


# Setup a function that returns accepts a parameter and returns a value
def averageclaimvaluedynamic(totalofclaims, numberofclaims):
    averageclaimvaluedynamically = 0
    averageclaimvaluedynamically = totalofclaims / numberofclaims

    # Add a new item to the array
    # Return the value for the total of the claims
    return averageclaimvaluedynamically


# We will call the function to find the average. We will pass in the
# actual array
averagevalueofmyclaimsdynamically = averageclaimvaluedynamic(claimvaluetotal(), len(myClaimValues))

print("The average value of the claims is: %d " % averagevalueofmyclaimsdynamically)



# Setup a function that accepts the array as a parameter and amends the array
def averageclaimvaluebyreference(myClaimValues):
    claimstotal = 0
    for claimvalue in myClaimValues:
        claimstotal = claimstotal + claimvalue
    print("The array list total before changing is: %d " % claimstotal)

    # Add a new item to the array
    myClaimValues.append(10000)
    claimstotalnew = 0
    for claimvalue in myClaimValues:
        claimstotalnew = claimstotalnew + claimvalue
    print("The array list total after changing is: %d " % claimstotalnew)

# We will call the function that will add the new item to the array.
averageclaimvaluebyreference(myClaimValues)
print("The array has been changed and is now: ", myClaimValues);


# Setup a function that accepts a variable number of paremeters
def averageclaimvaluefromvariabeparameters(value1, *othervalues):
    claimstotal = 0
    claimsarray = []

    claimsarray.append(value1)
    for claimvalue in othervalues:
        claimsarray.append(claimvalue)

    for claimvalue in claimsarray:
        claimstotal = claimstotal + claimvalue
    print("The total value of the items in the array made from the variable array list is: %d " % claimstotal)

# We will call the function with a variable list .
averageclaimvaluefromvariabeparameters(100, 200, 300, 400)

# We will call the function with a variable list .
averageclaimvaluefromvariabeparameters(100, 200, 300, 400, 500)