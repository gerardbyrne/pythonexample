# Program Description:     Python Array Data Structure
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015

# Create a function
def calculatecommission(policyamount):
    if policyamount <=0:
        # Raise an exception if the value is less than or equal to 0
        # The string message will be appended to the ValueError message text
        raise ValueError("your value is outside the lower limit")

    if policyamount > 100000:
        commissionearned =  policyamount * 0.10
        print("Commission Rate for this policy is 10% and the commission is %d", commissionearned)

    else:
        commissionearned = policyamount * 0.05
        print("Commission Rate for this policy is 5% and the commission is %d", commissionearned)

# Use the try statement and see if we get the ValueError or another error
try:
    policyamount = int(input("What is the value of the policy: "))
    calculatecommission(policyamount)

except ValueError as err:
    print("Error - Policy value must be greater than zero - %s" % err)
except:
    print("something is wrong")

