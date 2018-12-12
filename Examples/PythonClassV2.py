# Program Description:     Classes and Objects
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015


class Agent:
    # Create a class variable
    agentclassmessage = 'It is an Agent class and I am a class variable!'

    # Create a constructor
    def __init__(self, agenttype):
        self.typeofagent = agenttype

    # Create a instance method
    def agentwelcomemessage(self):
        # If we use print instead of return we still get output but it also says None
        return ("Welcome, you are a method of the Agent class")


# Creat an instance of the Agent class
myagent = Agent('Gold Agent')

# Display the type of agent for the instance of the class I have created
print('The agent type is - ' , myagent.typeofagent)

# Display the output from method agent welcome message for the instance of the class I have created
print('The static attribute, agentmessageclass, is the string - ', myagent.agentwelcomemessage())
