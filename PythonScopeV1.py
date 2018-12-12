# Program Description:     Python Scope and Namespaces
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015


def outside():
    mymessage = "My message from the outer part"
    def inside():
        nonlocal mymessage
        mymessage = "My message from the inner part"
        print(mymessage)
    inside()
    print(mymessage)

outside()