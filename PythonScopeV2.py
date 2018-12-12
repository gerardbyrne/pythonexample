# Program Description:     Python Array Data Structure
# Author:                             Gerry Byrne
# Date of creation:             15/06/2015


# Define a function with three embedded functions
def scope_test():
    # Embedded function one with a variable called spam
    def do_local():
        spam = "local spam"

# Embedded function two with a nonlocal variable called spam
# The nonlocal statement indicates that particular variables
# live in an enclosing scope and should be rebound there.

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

# Embedded function three with a global variable called spam
# The global statement can be used to indicate that particular
# variables live in the global scope and should be rebound there.
    def do_global():
        global spam
        spam = "global spam"

    # the variable spam is defined - not the same as the one in do_local function
    spam = "test spam"

    # the function is called and the local spam variable is defined
    do_local()
    # The spam variable here is the one that says test spam
    print("After local assignment:",spam)

    # the function is called and the nonlocal spam variable is defined
    do_nonlocal()
    # The spam variable here is the one that says nonlocal spam
    print("After nonlocal assignment:", spam)

    # the function is called and the global spam variable is defined
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)