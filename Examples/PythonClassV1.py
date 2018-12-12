# Program Description:     Classes and Objects
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015


class AgentClass:
    """My Simple Class"""

    def __init__(self, policyamount, commissionrate):
        self.valueofpolicy = policyamount
        self.rateofcommission = commissionrate

    agentid = 12345

    def agentcommission(self):
        return self.valueofpolicy * self.rateofcommission / 100


myagentclass = AgentClass(10000, 10)

print("The agentid attribute in the AgentClass is: ", myagentclass.agentid)
print("The agentcommission attribute in the AgentClass returns: ", myagentclass.agentcommission())
print("The __doc__ attribute in the AgentClass is: ", myagentclass.__doc__)


