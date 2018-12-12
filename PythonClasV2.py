# Program Description:     Classes and Objects
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015


class Agent:
    agentclassmessage = 'It is an Agent class and I am a class variable!'

    def __init__(self, agenttype):
        self.typeofagent = agenttype

    def agentwelcomemessage(self):
        # If we use print instead of return we still get output but it also says None
        return ("Welcome, you are a method of the Agent class")


myagent = Agent('Gold Agent')

print('The agent type is - ' , myagent.typeofagent)

print('The static attribute, agentmessageclass, is the string - ', myagent.agentwelcomemessage())
