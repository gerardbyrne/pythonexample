# Program Description:     Python MAny Examples
# Author:                  Gerry Byrne
# Date of creation:        16/11/2017

#################################################
#     These example programs run on Python 3.   #
#################################################


#################################
# READ THE FOLLOWING PARAGRAPH...

# There are some significant differences between Python 3 and earlier versions.
# For beginner Python programmers, the main ones are that
#   -   the print statement of Python 2.x is now a print function in Python 3
#       (brackets are required after the word print
#
#        >>> # Python 2
#        >>> print "Hello"
#
#       # Python 3
#       print("Hello", end="")

#   -   the raw_input function in Python 2.x is replaced by the input function in Python 3
#
#       >>> # Python 2
#       >>> name = raw_input()
#
#       >>> # Python 3
#       >>> name = input()

#   -   an integer division such as 2/3 in Python 2.x is now a real division in Python 3.
#
#       >>> # Python 2
#       >>> 25.0 / 8
#           3.125
#       >>> 25 / 8.0
#           3.125
#
#       >>> # Python 2
#       >>> 25 / 8
#           3
#       >>> # Python 3
#       >>> 25 / 8
#           3.125

# For experienced programmers we have the range() and string formatting differences
# In Python 2, the range() function returns an actual list with the integers.
# In Python 3, the range() function returns a "range object".
# Both can be used exactly the same way in for loops:
#
#       Python 3
#       listOfInts = list(range(10))
#       print(listOfInts)
#
# Python 3 adds a new string method called format().
# This string lets you provide a list of arguments as parameters to format().
# Instead of %s, you use {0} and {1} and {2} and so on:
#
# Python 3
#   >>> 'My name is {0} and I am from {1}.'.format('Al', 'Houston')
#       'My name is Al and I am from Houston.'
#
#

###################################################################

#                   Examples - Print                              #
#                       Python 3                                  #

###################################################################


print("Hello World!")


nameOfCustomer= input("Please enter the customers full name \n")
print("The customer name is: ")
print(nameOfCustomer)


###################################################################

#               Examples - Numeric Types                          #
#                       Python 3                                  #

###################################################################

totalValueOfPolicies    = 0.0

policyValueOne          = float(input("Enter the first policy value: "))

policyValueTwo          = float(input("Enter the second policy value: "))

policyValueThree        = float(input("Enter the third policy value: "))

totalValueOfPolicies    = policyValueOne  + policyValueTwo + policyValueThree

averageValueOfPolicies  = totalValueOfPolicies / 3

print("The average value of the three policies is " + str(averageValueOfPolicies))


###################################################################

#                 Examples - Iteration                            #
#                       Python 3                                  #

###################################################################

totalValueOfPolicies = 0.0
countOfPoliciesEntered = 0

while countOfPoliciesEntered < 3:
    policyValue = float(input("Enter the policy value: "))
    countOfPoliciesEntered = countOfPoliciesEntered + 1
    totalValueOfPolicies = totalValueOfPolicies + policyValue
averageValueOfPolicies = totalValueOfPolicies / 3
print("The average value of the three policies is " + str(averageValueOfPolicies))


###################################################################

#               Examples - Miscellaneous                          #
#                       Python 3                                  #

###################################################################

# Int data type
totalValueOfPolicies = 100000
print(totalValueOfPolicies)
print(type(totalValueOfPolicies))

# Float data type
totalValueOfPolicies = 100000.99
print(totalValueOfPolicies)
print(type(totalValueOfPolicies))


# Arithmetic data type int
print(2 + 4)
print(6 - 4)
print(6 * 3)
print(6 / 3)
print(6 % 3)
print(6 // 3)  # floor division: always truncates fractional remainders
print(-5)
print(3 ** 2)  # three to the power of 2

# Arithmetic data type float
print(2.0 + 4.0)
print(6.0 - 4.0)
print(6.0 * 3.0)
print(6.0 / 3.0)
print(6.0 % 3.0)
print(6.0 // 3.0)  # floor division: always truncates fractional remainders
print(-5.0)
print(3.0 ** 2.0)  # three to the power of 2


# Arithmetic data type mixed. When we used mixed data types the expressions
# are "converted up" which means the data type with the greater storage is used.
# So float has the greater storage (8 bytes). Int has (4 bytes).
print(2 + 4.0)
print(6 - 4.0)
print(6 * 3.0)
print(6 / 3.0)
print(6 % 3.0)
print(6 // 3.0)  # floor division: always truncates fractional remainders
print(-5.0)
print(3 ** 2.0)  # three to the power of 2


# Boolean expressions result in a value of true or false
# Python stores true as integer 1 and false as integer 0
# but outputs 'true' or 'false' from print statements
print(7 > 10)
print(4 < 16)
print(4 == 4)
print(4 <= 4)
print(4 >= 4)
print(4 != 4)

# 03-08.py

# String objects
print("Enter the first policy value: ")
print('valueOfPolicy')

# 03-09.py

# String assignments
questionOne = "Enter the first policy value: "
print(questionOne)


questionOne = "Enter the first policy value "
typeOfInsurance = "for the Auto client"
print(questionOne + typeOfInsurance)


# We cannot concatenate a string and an integer
# we must convert the integer to a string first:
valueOne = 10000
phraseOutput = questionOne + str(valueOne)
print(phraseOutput)


# Round up a floating point number to the nearest integer

valueOfPolicy = 100000.60
print(valueOfPolicy)
valueOfPolicy = round(valueOfPolicy)
print(valueOfPolicy)

# Compare this with the use of int casting
valueOfPolicy = 100000.60
valueOfPolicy = int(valueOfPolicy)
print(valueOfPolicy)


# Round a float number to 2 decimal places and output the number as $ currency
# printed with a comma after the number of thousands

valueOfPolicy = 1234.5678
print(valueOfPolicy)
valueOfPolicy = round(valueOfPolicy, 2)
print(valueOfPolicy)


# the above line rounds the number to 2 decimal places

thousands = valueOfPolicy / 1000
print(thousands)
thousands = int(thousands)
print(thousands)
remainder = valueOfPolicy % 1000
print(remainder)
pretty_output = "$" + str(thousands) + "," + str(remainder)
print(pretty_output)



###################################################################

#            Examples - Selection  If Statement                   #
#                       Python 3                                  #

###################################################################

#  The condition of the following if statement follows the word if
#  and ends with a colon (:)
#  In this example, if x has a value equal to 'spam',
#  then 'Hi spam' will be printed.

# IMPORTANT the indentation of this code matters.
# The statement(s) following the if condition (i.e. boolean expression)
# must be indented to the next tab stop. This means we must press
# the Tab key before typing the word print.
# Try removing the tab spaces and see what happens when you attempt to run.

myPhrase = 'Insurance'
if myPhrase == 'Insurance':
    print('What type of insurance?')
else:
    print('We only do insurance')


###################################################################

#            Examples - Selection  If Statement                   #
#            Multiple Statements in True section                  #
#                       Python 3                                  #

###################################################################

myPhrase = 'Insurance'
if myPhrase == 'Insurance':
    print('What type of insurance?')
    print('The insurance types are')
    print('Auto insurance')
    print('Home insurance')
    print('Renter insurance')
else:
    print('We only do insurance')


###################################################################

#            Examples - Selection  If Statement                   #
#            Multiple Statements in False section                 #
#                       Python 3                                  #

###################################################################

#  if statement with multiple statements in the false section
myPhrase = 'Insurance'
if myPhrase == 'Insurance':
    print('What type of insurance?')
    print('The insurance types are')
    print('Auto insurance')
    print('Home insurance')
    print('Renter insurance')
else:
    print('We only do insurance')
    print('and we would be very')
    print('happy to give you a quote')


###################################################################

#            Examples - Selection  If Statement                   #
#          Nested if statements (if within an if)                 #
#                       Python 3                                  #

###################################################################

valueOfPolicy = input("Enter the value of the policy: ")
valueOfPolicy = int(valueOfPolicy)
if valueOfPolicy >= 100000:
    commissionRate = '10%'
else:
    if valueOfPolicy >= 50000:
        commissionRate = '5%'
    else:
        commissionRate = '0%'
print("\n\nThe commission rate for this policy is: " + commissionRate)




###################################################################

#            Examples - Selection  If Statement                   #
#                  Using the if/elif/else                         #
#                       Python 3                                  #

###################################################################

valueOfPolicy = input("Enter the value of the policy: ")
valueOfPolicy = int(valueOfPolicy)
if valueOfPolicy >= 100000:
    commissionRate = '10%'
elif valueOfPolicy >= 90000:
        commissionRate = '9%'
elif valueOfPolicy >= 80000:
        commissionRate = '8%'
elif valueOfPolicy >= 70000:
        commissionRate = '7%'
else:
        commissionRate = '0%'
print("\n\nThe commission rate for this policy is: " + commissionRate)




###################################################################

#            Examples - Selection  If Statement                   #
#            Using AND and OR to link conditions                  #
#                       Python 3                                  #

###################################################################

age = input("Enter your age: ")
age = int(age)
have_own_car = input("Do you own your own car (y/n): ")

if (age > 21) and (have_own_car == 'y'):
    print("You are over 21 years old and own your own car")

if (age > 21) and (have_own_car == 'n'):
    print("You are over 21 years old and you do NOT own your own car")

if (age == 21) and (have_own_car == 'y'):
    print("You are 21 years old and you own your own car")

if (age == 21) and (have_own_car == 'n'):
    print("You are 21 years old and you DO NOT own your own car")

if (age < 21) and (have_own_car == 'y'):
    print("You are younger than 21 and you own your own car")

if (age < 21) and (have_own_car == 'n'):
    print("You are younger than 21 and you DO NOT own your own car")

salary = float(input("Enter your annual salary, (e.g. 50000): "))

if (salary > 50000) or (age > 21):
    print("you can join our club because you earn more than $50000 OR you are over 21 (or both)")
else:
    print("you need to be earning more than 50000 OR be over 21 (or both) to join our club")



###################################################################

#                    Examples - Iteration                         #
#                        While Loops                              #
#                         Python 3                                #

###################################################################

#  IMPORTANT - remember to indent the statements to be repeated.
#  They must be repeated to the same level.
#  Use the Tab key to indent. The space bar can be used.
#  The while loop, as used in this example, is said to be 'counter-controlled'.
#  In this program, maximumNumberOfPolicies is acting as a counter.

maximumNumberOfPolicies = 0
while maximumNumberOfPolicies < 5:
    print('Enter another policy value')
    maximumNumberOfPolicies = maximumNumberOfPolicies + 1
print('You have reached the maximum number of policies that can be entered')



maximumNumberOfPolicies = 0
while maximumNumberOfPolicies < 5:
    print('Enter another policy value')
    maximumNumberOfPolicies = maximumNumberOfPolicies + 1
print('You have reached the maximum number of policies that can be entered')
print('You can enter more policy values after 5 minutes')


###################################################################

#                    Examples - Iteration                         #
#                 While Loops with continue                       #
#                         Python 3                                #

#  An infinite loop.                                              #
#  Remember that 1 (or any value other than 0) represents true.   #
#  Press Ctrl-C to interrupt this program run.                    #

###################################################################

while 1:
    print('Do you want to enter another policy value')
    answer = input('Press y for yes ')
    if answer == 'y':
        print('OK you can now enter more policy values ')
        continue
    answer = input('Are you finished yet? ')
    if answer == 'y':
        break
print('That was a lot of policies ')
print('enjoy the commission you have earned!')



###################################################################

#                    Examples - Iteration                         #
#                        While Loops                              #
#                         Python 3                                #

#  An infinite loop.                                              #
#  Remember that 1 (or any value other than 0) represents true.   #
#  Press Ctrl-C to interrupt this program run.                    #

###################################################################



# Initialization phase
totalValueOfPolicies = 0  # sum of policy values
numberOfPoliciesEntered = 0  # number of policiy values entered

# Processing phase
valueOfPolicy = input("Enter the value of the policy, (Enter -9 to end): ")  # get one value
valueOfPolicy = int(valueOfPolicy)  # convert string to an integer

while valueOfPolicy != -9:  # -9 is used as a sentinel ( a lookout or sentry value )
    totalValueOfPolicies = totalValueOfPolicies + valueOfPolicy
    numberOfPoliciesEntered = numberOfPoliciesEntered + 1
    valueOfPolicy = input("Enter the value of the policy, (Enter -9 to end): ")
    valueOfPolicy = int(valueOfPolicy)

# Termination phase
if numberOfPoliciesEntered != 0:  # division by zero would be a run-time error
    averageValueOfPolicies = float(totalValueOfPolicies) / numberOfPoliciesEntered
    print("The average of the policies you have entered is", averageValueOfPolicies)
else:
    print("No policy values were entered")





###################################################################

#                    Examples - Math Library                      #
#                                                                 #
#                         Python 3                                #

#  Using the built-in square root function math.sqrt              #
#  To use any math function we need to include the statement:     #
#  import math                                                    #
#  in the program - usually at the top, but can be anywhere.      #

###################################################################


import math

print(math.sqrt(16))
print(math.sqrt(16.5))
x = 144
print(math.sqrt(x))


###################################################################

#                    Examples - Math Library                      #
#                                                                 #
#                         Python 3                                #

#  Using the dir function to list out the names of the            #
#  functions available in the math module.                        #

###################################################################
import math

print(math)
print(dir(math))




###################################################################

#                    Examples - Functions                         #
#             Functions with no return statement                  #
#                         Python 3                                #

###################################################################

def welcomemessage():
    print("Thank you for letting us give you an insurance quote")

welcomemessage()



def manywelcomemessages(numberoftimes):
    for item in range(numberoftimes):
        print("Thank you for letting us give you an insurance quote")

manywelcomemessages(10)



def manywelcomemessages(numberoftimes, nameofcustomer):
    for item in range(numberoftimes):
        print(nameofcustomer + " - thank you for letting us give you an insurance quote")

manywelcomemessages(10, 'Gerry')





###################################################################

#                    Examples - Functions                         #
#             Functions with no return statement                  #
#                         Python 3                                #

###################################################################

# start of function definition
def commisionearned(valueofpolicy):
    return valueofpolicy * 0.10


# end of function definition

# prints the commission for the values
# from 100000 to 100010
for itemvalue in range(100000, 100010):
    print(commisionearned(itemvalue))

# the last value of itemvalue is 100010
print("last value of itemvalue is:", itemvalue)



###################################################################

#                    Examples - Functions                         #
#             Functions with 2 return statements                  #
#                         Python 3                                #

###################################################################



def division(valueone, valuetwo):
    if (valuetwo == 0):
        print("division by zero not allowed")
        return
    else:
        print(" returning %f divided by %f " % (valueone, valuetwo))
        return valueone / valuetwo


print(" 5.0 / 2  returns:")
result = division(5.0, 2)
print(result)

print(" 5.0 / 0  returns:")
result = division(5.0, 0)
print(result)















#  File:       06-11.py
#  Purpose:    Example: the scope of a variable
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 15th October 2016, 9:26 PT

#  program demonstrating the scope of a variable
# (i.e. where it can be used)

def my_function(n):
    print("n in function: ", n)
    print("number in function: ", number)


number = 10
print("number in main program: ", number)
my_function(number)
# print(n)

# Uncomment the line above and try to run.
# You will get an error, because....
# n is not known outside of the function my_function.
# Notice however that number is known in the function
# as well as in the main program!
# We say that number has global scope, but n has local scope.
# Local scope means the variable is only available
# in the function where it is defined
# Global scope means the variable is available everywhere in the code.









#  File:       06-12.py
#  Purpose:    Demonstrates the use of Python functions
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Sunday 29th October 2006, 12:48 PT



'''
    Thanks to HW for the idea behind this program.

    Note that this is a multi-line comment which starts and ends with
    three single quote marks (')

    Note that functions can be defined anywhere,
    as long as they're defined before they're called.

    Note the use in this program of a simple pause function,
    to pause a program until a key is pressed.

    Note that when a function is called, all the lines in the
    function definition (def) are executed in order,
    then the program resumes at the point after the function call.

    Note that this program script starts executing at the line:
    startMessage()
    followed by the line:
    clearScreen()
    followed by the line:
    print ("Testing this program")
'''


def pause():
    input("\n\nPress any key to continue...\n\n")


def quitMessage():
    print("Thank you for using this program")
    print("Goodbye")


def printThreeLines():
    for i in range(1, 4):
        print('this is line ' + str(i))


def printNineLines():
    for i in range(1, 4):
        printThreeLines()


def startMessage():
    print("This program demonstrates the use of Python functions")
    pause()


def blank_Line():
    print()


def clearScreen():
    for i in range(1, 26):
        blank_Line()


startMessage()
clearScreen()
print("Testing this program")
printNineLines()
pause()
clearScreen()
printNineLines()
blank_Line()
printNineLines()
pause()
clearScreen()
quitMessage()

#  File:       07-01.py
#  Purpose:    Example: creating and using a Python list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:02 PT

result = [0, 0, 0, 0, 0, 0, 0, 0]
print(result)
result[0] = 75
result[1] = 90
result[4] = 72
print(result)
print(result[0])
print(result[1])
print(result[2])
print(result[3])
print(result[4])
print(result[5])
print(result[6])
print(result[7])

#  File:       07-02.py
#  Purpose:    Example: creating and printing an empty list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:15 PT

list1 = []
print(list1)

# the following statement would generate an error
# print (list1[0])













#  File:       07-03.py
#  Purpose:    Example: appending to an empty list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:17 PT

list1 = []
print(list1)
list1.append(67)
print(list1[0])
list1.append("spam")
print(list1)
print(list1[0])
print(list1[1])
# the following statement would generate an out-of-range error
# print (list1[2])










#  File:       07-04.py
#  Purpose:    Example: a list of lists
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:22 PT

list1 = [1, 2, 3]
print(list1)
list2 = [4, 5, 6]
print(list2)
list3 = [list1, list2]
print(list3)
print(list3[0])
print(list3[1])

#  File:       07-05.py
#  Purpose:    Example: accessing the last item in a list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:27 PT

list1 = [1, 2, 3, 6, 7, 8, 9, 10]
print(list1)
print(list1[0])
print(list1[1])
print(list1[-1])
print(list1[-2])

#  File:       07-06.py
#  Purpose:    Example: deleting items from a list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 25th October 2004, 8:28 PT

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
del list1[0]
del list1[-1]
print(list1)

#  File:       07-07.py
#  Purpose:    Example: repeating lists
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 6:37 PT

list1 = [1, 2, 3]
print(list1)
print(list1 * 3)
print(list1)
list1 = list1 * 2
print(list1)

#  File:       07-08.py
#  Purpose:    Example: concatenating lists
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 6:55 PT

list1 = [1, 2, 3]
print(list1)
list2 = [4, 5, 6]
print(list2)
list1 = list1 + list2
print(list1)
list1 = list1 + list1
print(list1)

#  File:       07-09.py
#  Purpose:    Example: ist indexing
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:07 PT

list1 = ["Anne", "Dawson", 666]
print(list1[0], list1[2])

#  File:       07-10.py
#  Purpose:    Example: list indexing
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:08 PT

list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(list1[0:1], list1[5:7])

#  File:       07-11.py
#  Purpose:    Example: finding the length of a list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:20 PT

list1 = ["Anne", "was", 'here', 'testing', 1, 2, 3]
list2 = [1, 2, 3, 4]
list3 = []
print(len(list1), len(list2), len(list3))

#  File:       07-12.py
#  Purpose:    Example: list iteration
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:26 PT

list2 = [1, 2, 3, "Spam", 4, 5]
for i in list2:
    print(i, end=" ")

# File:       07-13.py
#  Purpose:    Example: list membership
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:28 PT

list2 = [1, 2, 3, "Spam", 4, 5]
print("Spam" in list2)

#  File:       07-14.py
#  Purpose:    Example: a selection of list methods
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 7:42 PT

list2 = ["B", "C", "A"]
print(list2)
list2.extend(["X", "Y"])  # extends the list
print(list2)
list2.pop()  # removes last item from the list
print(list2)
list2.pop()
print(list2)
list2.reverse()  # reverses the order of the items in the list
print(list2)
list2.append("S")
print(list2)
list2.sort()  # sorts the list into ascending order
print(list2)
list2.reverse()  # reverses the order of the items in the list
print(list2)

#  File:       07-15.py
#  Purpose:    Example: a 2D list
#  Programmer: Anne Dawson
#  Course:     CSCI120A
#  Date:       Sunday 4th November 2007, 12:15 PT

tictactoe = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(tictactoe[0])
print(tictactoe[1])
print(tictactoe[2])
print()

row = 1
column = 0
print("row " + str(row) + " column " + str(column) + " has value")
print(tictactoe[row][column])

row = 2
column = 2
print("row " + str(row) + " column " + str(column) + " has value")
print(tictactoe[row][column])

print()
print()
tictactoe[2][2] = 0
print("After changing the value at row 2 and column 2 to 0: ")
print()
print(tictactoe[0])
print(tictactoe[1])
print(tictactoe[2])

#  File:       07-16.py
#  Purpose:    Differences in range() with Python 2 and Python 3
#  Programmer: Anne Dawson
#  Course:     CSCI120A
#  Date:       Saturday 3rd January 2015, 11:51 PT
# The range() function works differently in Python 2 and Python 3.
# In Python 2, the range function returns a list,
# which may take up a large amount of memory, depending on the size and nature of the list.
# In Python 3, the range function will always take the same (small) amount of memory,
# no matter the size of the range it represents
# as it only stores the start, stop and step values,
# calculating individual items and subranges as needed.

# See: https://docs.python.org/3/tutorial/controlflow.html#the-range-function
# and for much more detail, see:
# See: https://docs.python.org/3/library/stdtypes.html?highlight=range#range

# You can always convert a range to a list by using the list function,
# as shown in the following code.

# Anne Dawson, Tuesday 28th October 2014, 7:56 PT
# Example run follows:

'''
>>>
range(0, 10)
<class 'range'>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
<class 'list'>
>>>
'''

x = range(10)
print(x)
print(type(x))
x = list(range(10))
print(x)
print(type(x))

#  File:       08-01.py
#  Purpose:    Example: strings
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 30th October 2004, 16:14 PT

print('Anne was here')
print("9396633")

# Note that you can print a string over several lines
# if you contain it within triple quotes marks:

print('''Anne was here 
     on Saturday 
     30th October 2004''')

#  File:       08-02.py
#  Purpose:    Example: using an apostrophe within a string
#              and using double quote marks within a string
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 30th October 2004, 16:14 PT

print("This is Anne's spam")
print("This is Anne's spam and these are Jake's eggs")

# You can also print a " within a string enclosed in single quotes:

print('Here is a double quote ", and "more"')

#  File:       08-03.py
#  Purpose:    Example: multiplying numbers and
#                       multiplying strings
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 30th October 2004, 16:38 PT

print(3 * 4)
print(30 * 4)
print("3" * 4)
print("30" * 4)

#  File:       08-04.py
#  Purpose:    Example: string concatenation
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Saturday 30th October 2004, 16:51 PT

print("Anne " + "was " + ("here " * 3))

#  File:       08-05.py
#  Purpose:    Example: string indexing
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 7:01 PT

s1 = "Anne Dawson"
print(s1[0], s1[5])

#  File:       08-06.py
#  Purpose:    Example: string slicing
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 7:07 PT

s1 = "Anne Dawson"
print(s1[0:1], s1[5:7])
print(s1[6:9])

#  File:       08-07.py
#  Purpose:    Example: finding the length of a string
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 7:10 PT


s1 = "Anne"
s2 = "Dawson"
s3 = ""
print(len(s1), end=" ")
print(len(s2), end=" ")
print(len(s3))

#  File:       08-08.py
#  Purpose:    Example: the %s string formatting code
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 8:00 PT


print('Python is a %s language.' % 'great')

#  File:       08-09.py
#  Purpose:    Example: finding a string within a string
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 8:11 PT


s1 = 'spamandeggs'
x = s1.find('and')
print(x)

#  File:       08-10.py
#  Purpose:    Example: finding a string within a string
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 1st November 2004, 8:34 PT


s1 = 'spam and eggs'
s1.replace('and', 'without')
print(s1)
# the above shows that strings are immutable (cannot change)

s2 = s1.replace('and', 'without')
print(s2)

#  File:       08-11.py
#  Purpose:    Example: escape sequences within a string
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 2nd November 2004, 8:29 PT


s = 'one\ntwo\tthree'
print(s)

#  File:       08-12.py
#  Purpose:    Example: an escape sequence counts as one character
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Tuesday 2nd November 2004, 8:31 PT


s = 'one\ntwo\tthree'
print(s)
print(len(s))

#  File:       08-13.py
#  Purpose:    Example: iteration and membership with strings
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 3rd November 2004, 7:35 PT


s = 'Anne was here'
for c in s:
    print(c, end=" ")
print('w' in s, end=" ")
print(' ' in s, end=" ")
print('x' in s)

# 08-14.py
# Anne Dawson
# Sunday 20th March 2005, 04:44 PT
# Demonstration of printing Unicode characters
# For explanation, see:
# http://www.network-theory.co.uk/docs/pytut/tut_17.html
# For character charts go to:
# http://www.unicode.org/charts/
# http://www.unicode.org/charts/PDF/U2580.pdf (Block Elements)
# \u2588 is a Full Block which can be used to build up a black square
str1 = "Hello\u2588out there"  # solid black block within text
print(str1)
str1 = '\u2588\u2588'  # two full block characters
print(str1)
print()
print()
print("two lines of two full blocks")
print(str1)
print(str1)
print()
print()
# Note: a space is \u0020
print('two lines of two full blocks, two spaces, two full blocks:')
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020\u0020\u0020\u2588\u2588\u2588\u2588'
print(str1)
print(str1)
print()
print()
print('two lines of two full blocks, the number 17 and two full blocks:')
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020' + '17' + '\u2588\u2588\u2588\u2588'
print(str1)
str1 = '\u2588\u2588\u2588\u2588\u0020\u0020\u0020\u0020\u2588\u2588\u2588\u2588'
print(str1)

#  File:       09-01.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 4th November 2004, 8:37 PT

file1 = open('C:\\temp\\file1.txt', 'r')
# the line above opens C:\temp\file1.txt for reading
string = file1.readline()
print(string)

#  File:       09-02.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 10:38 PT

file1 = open("C:\\temp\\tester2.txt", "w")
print(file1)  # prints out details about the file
file1.write("Today is Monday\n")
file1.write("Tomorrow is Tuesday")
file1.close()

#  File:       09-03.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 10:56 PT

file2 = open("C:\\temp\\tester2.txt", "r")
print(file2)  # prints out details about the file
string1 = file2.read()
print(string1)
file2.close()
file2 = open("C:\\temp\\tester2.txt", "r")
string1 = file2.read(5)
print(string1)
string1 = file2.read(5)
print(string1)
string1 = file2.read(5)
print(string1)
file2.close()


#  File:       09-04.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 11:31 PT

def copyFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while 1:
        text = f1.read(50)
        if text == "":
            break
        f2.write(text)
    f1.close()
    f2.close()
    return


filecopy = "C:\\temp\\tester2copy.txt"  # this file will be created
fileold = "C:\\temp\\tester2.txt"  # existing file
copyFile(fileold, filecopy)

#  File:       09-05.py
#  Purpose:    Example: a program which uses a file
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Monday 7th March 2005, 11:31 PT

filename = input('Enter a file name: ')
try:
    f = open(filename, "r")
except:
    print('There is no file named', filename)

# File:       10-01.py
#  Purpose:    Example: sequential search of a list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 11th November 2004, 14:05 PT


list1 = [11, 27, 36, 44, 51, 22, 65, 1, 78]
numbertofind = int(input("Enter a number\n"))
found = 0
for i in list1:
    if numbertofind == i:
        print(numbertofind, " at index: ", list1.index(numbertofind))
        found = 1
if found == 0:
    print("Number not found")

# File:       10-02.py
#  Purpose:    Example: sequential search of a list
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Wednesday 19th November 2008, 11:37 PT

mylist = [10, 11, 3, 4, 55, 12, 23, 14, 16]
n = len(mylist)
print(n)
for i in range(n):
    print(mylist[i], end=" ")
search = int(input("\nPlease enter a number to search for: "))
print(search)
found = False
for i in range(n):
    if mylist[i] == search:
        found = True
        index = i
print()
if found == True:
    print(str(search) + " found at index " + str(index))
else:
    print(str(search) + " not found")

# File:       bubblesort.py
#  Purpose:    Example: a program which demonstrates a bubble sort on
#              a list of 10 random integers
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Sunday 14th November 2004, 9:17 PT

import random


# define the bubble sort function
def sort(values):
    length = len(values)
    for time in range(0, length - 1):
        for position in range(0, (length - time - 1)):
            if values[position] > values[position + 1]:
                temp = values[position]
                values[position] = values[position + 1]
                values[position + 1] = temp


# generate a list of ten random numbers
numbers = []
number = 0
while number < 10:
    value = random.randint(1, 100)
    if not (value in numbers):
        numbers.append(value)
        number = number + 1

# show unsorted list, sort the list, and show sorted list
print("Before:", numbers)
sort(numbers)
print("After :", numbers)


#  File:       12-01.py
#  Purpose:    Example: a recursive function
#  Programmer: Anne Dawson
#  Course:     CSCI120A, CSCI165
#  Date:       Thursday 11th November 2004, 14:25 PT

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(" 5! has a value of: ", )
result = factorial(5)
print(result)

print(" 4! has a value of:", )
result = factorial(4)
print(result)


#  File:       13-01.py
#  Purpose:    OOP Example: How to create objects of the Person class
#              and how to inspect the state of those objects.
#  Programmer: Anne Dawson
#  Course:     CSCI120
#  Date:       Sunday 27th November 2016, 14:20 PT
#  References: http://www.annedawson.net/Python3_Intro_OOP.odp
#              http://www.annedawson.net/Python3_Prog_OOP.odp

class Person():
    '''Instantiates a Person object with given name. '''

    def __init__(self, first_name, last_name):
        '''Initializes private instance variables _firstname and _lastname. '''
        self._firstname = first_name
        self._lastname = last_name

    def __str__(self):
        '''Returns the state of the Person object. '''
        return self._firstname + " " + self._lastname


print(Person.__doc__)  # prints the docstring for the class
person1 = Person("Anne", "Dawson")
person2 = Person("Tom", "Lee")
print(person1)
print(person2)


#  File:       13-02.py
#  Purpose:    OOP Example: How to use accessor methods
#  Programmer: Anne Dawson
#  Course:     CSCI120
#  Date:       Sunday 27th November 2016, 14:30 PT
#  References: http://www.annedawson.net/Python3_Intro_OOP.odp
#              http://www.annedawson.net/Python3_Prog_OOP.odp

class Person():
    '''Instantiates a Person object with given name. '''

    def __init__(self, first_name, last_name):
        '''Initializes private instance variables _firstname and _lastname. '''
        self._firstname = first_name
        self._lastname = last_name

    def __str__(self):
        '''Returns the state of the Person object. '''
        return self._firstname + " " + self._lastname

    def getFirstname(self):  # accessor method
        '''Returns the instance variable _firstname. '''
        return self._firstname

    def getLastname(self):  # accessor method
        '''Returns the instance variable _lastname. '''
        return self._lastname


print(Person.__doc__)  # prints the docstring for the class
person1 = Person("Anne", "Dawson")
person2 = Person("Tom", "Lee")
print(person1)  # calls the __str__ method implicitly on person1 object
print(person2)  # calls the __str__ method implicitly on person2 object
print(Person.getFirstname.__doc__)  # prints the docstring for the getFirstname method
print(person1.getFirstname())
print(person1.getLastname())
print(person2.getFirstname())
print(person2.getLastname())


#  File:       13-03.py
#  Purpose:    OOP Example: How to use accessor and mutator methods
#  Programmer: Anne Dawson
#  Course:     CSCI120
#  Date:       Sunday 27th November 2016, 14:42 PT
#  References: http://www.annedawson.net/Python3_Intro_OOP.odp
#              http://www.annedawson.net/Python3_Prog_OOP.odp

class Person():
    '''Instantiates a Person object with given name. '''

    def __init__(self, first_name, last_name):
        '''Initializes private instance variables _firstname and _lastname. '''
        self._firstname = first_name
        self._lastname = last_name

    def __str__(self):
        '''Returns the state of the Person object. '''
        return self._firstname + " " + self._lastname

    def getFirstname(self):  # accessor method
        '''Returns the instance variable _firstname. '''
        return self._firstname

    def getLastname(self):  # accessor method
        '''Returns the instance variable _lastname. '''
        return self._lastname

    def setFirstname(self, newFirstname):  # mutator method
        '''Assign a value to the instance variable _firstname. '''
        self._firstname = newFirstname

    def setLastname(self, newLastname):  # mutator method
        '''Assign a value to the instance variable _lastname. '''
        self._lastname = newLastname


print(Person.__doc__)  # prints the docstring for the class
person1 = Person("Anne", "Dawson")
person2 = Person("Tom", "Lee")
print(person1)  # calls the __str__ method implicitly on person1 object
print(person2)  # calls the __str__ method implicitly on person2 object
print(Person.getFirstname.__doc__)  # prints the docstring for the getFirstname method
print(person1.getFirstname())
print(person1.getLastname())
print(person2.getFirstname())
print(person2.getLastname())
person1.setFirstname("Annie")
print(person1.getFirstname())


#  File:       13-04.py
#  Purpose:    OOP Example: How to use accessor, mutator and regular methods
#  Programmer: Anne Dawson
#  Course:     CSCI120
#  Date:       Sunday 27th November 2016, 14:50 PT
#  References: http://www.annedawson.net/Python3_Intro_OOP.odp
#              http://www.annedawson.net/Python3_Prog_OOP.odp

class Person():
    '''Instantiates a Person object with given name. '''

    def __init__(self, first_name, last_name):
        '''Initializes private instance variables _firstname and _lastname. '''
        self._firstname = first_name
        self._lastname = last_name

    def __str__(self):
        '''Returns the state of the Person object. '''
        return self._firstname + " " + self._lastname

    def getFirstname(self):  # accessor method
        '''Returns the instance variable _firstname. '''
        return self._firstname

    def getLastname(self):  # accessor method
        '''Returns the instance variable _lastname. '''
        return self._lastname

    def setFirstname(self, newFirstname):  # mutator method
        '''Assign a value to the instance variable _firstname. '''
        self._firstname = newFirstname

    def setLastname(self, newLastname):  # mutator method
        '''Assign a value to the instance variable _lastname. '''
        self._lastname = newLastname

    def reverseName(self):  # method
        '''Reverses the full name   '''
        return self._lastname + " " + self._firstname


print(Person.__doc__)  # prints the docstring for the class
person1 = Person("Anne", "Dawson")
person2 = Person("Tom", "Lee")
print(person1)  # calls the __str__ method implicitly on person1 object
print(person2)  # calls the __str__ method implicitly on person2 object
print(Person.getFirstname.__doc__)  # prints the docstring for the getFirstname method
print(person1.getFirstname())
print(person1.getLastname())
print(person2.getFirstname())
print(person2.getLastname())
person1.setFirstname("Annie")
print(person1.getFirstname())
print(person1.reverseName())


#  File:       13-05.py
#  Purpose:    OOP Example: Student class inherits from Person class
#  Programmer: Anne Dawson
#  Course:     CSCI120
#  Date:       Monday 28th November 2016, 7:22 PT
#  References: http://www.annedawson.net/Python3_Intro_OOP.odp
#              http://www.annedawson.net/Python3_Prog_OOP.odp

class Person():
    '''Instantiates a Person object with given name. '''

    def __init__(self, first_name, last_name):
        '''Initializes private instance variables _firstname and _lastname. '''
        self._firstname = first_name
        self._lastname = last_name

    def __str__(self):
        '''Returns the state of the Person object. '''
        return self._firstname + " " + self._lastname

    def getFirstname(self):  # accessor method
        '''Returns the instance variable _firstname. '''
        return self._firstname

    def getLastname(self):  # accessor method
        '''Returns the instance variable _lastname. '''
        return self._lastname

    def setFirstname(self, newFirstname):  # mutator method
        '''Assign a value to the instance variable _firstname. '''
        self._firstname = newFirstname

    def setLastname(self, newLastname):  # mutator method
        '''Assign a value to the instance variable _lastname. '''
        self._lastname = newLastname

    def reverseName(self):  # method
        '''Reverses the full name   '''
        return self._lastname + " " + self._firstname


class Student(Person):
    '''Instantiates a Student object with given name. '''

    def __init__(self, first_name, last_name, student_number=0, G_P_A=0):
        '''Initializes private instance variables _firstname, _lastname, _SN and _GPA. '''
        super().__init__(first_name, last_name)  # import base's parameters
        '''Initializes private instance variables _firstname and _lastname. '''
        self._SN = student_number
        self._GPA = G_P_A

    def __str__(self):
        '''Returns the state of the Student object. '''
        return self._firstname + " " + self._lastname + " " + str(self._SN) + " " + str(self._GPA)

    def getSN(self):  # accessor method
        '''Returns the instance variable _SN. '''
        return self._SN

    def getGPA(self):  # accessor method
        '''Returns the instance variable _GPA. '''
        return self._GPA

    def setSN(self, newSN):  # mutator method
        '''Assign a value to the instance variable _SN. '''
        self._SN = newSN

    def setGPA(self, newGPA):  # mutator method
        '''Assign a value to the instance variable _GPA. '''
        self._GPA = newGPA

    def reverseName(self):  # method
        '''Reverses the full name   '''
        return self._lastname + " " + self._firstname + " " + str(self._GPA)


print(Student.__doc__)  # prints the docstring for the class
student1 = Student("Carol", "Wong")
student2 = Student("Bill", "Wang")
print(student1)  # calls the __str__ method implicitly on person1 object
print(student2)  # calls the __str__ method implicitly on person2 object
print(Student.getFirstname.__doc__)  # prints the docstring for the getFirstname method
print(Student.getGPA.__doc__)  # prints the docstring for the getGPA method
print(student1.getFirstname())
print(student1.getLastname())
print(student2.getFirstname())
print(student2.getLastname())
student1.setFirstname("Louisa")
print(student1.getFirstname())
print(student1.reverseName())  # The reverseName method of the Student class
# overrides the same method of the Parent class.
# This is an example of polymorphism




























































