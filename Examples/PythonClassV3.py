class Customer(object):
    """Customer bank account.
    Customers have the following properties:

    Attributes:
        name:       A string value that represents the customer's name.
        balance:    A float value for maintaining the current balance of the customer's account.
    """

    def __init__(self, customername, openingbalance=0.0):
        """Construct a Customer object whose:
                name is the name passed in from the calling statement and
                opening balance is the balance passed in (or defaulted to 0)."""
        self.name = customername
        self.balance = openingbalance

    def withdraw(self, withdrawalamount):
        """Return the balance in the customer account after withdrawing the passed in amount"""
        if withdrawalamount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= withdrawalamount
        return self.balance

    def deposit(self, depositamount):
        """Return the balance in the customer account after depositing the passed in amount"""
        self.balance += depositamount
        return self.balance


myCustomer = Customer('Gerry Byrne', 1000)

print(myCustomer.withdraw(100))

print(myCustomer.deposit(600))

print(Customer.withdraw(myCustomer, 500))

print(Customer.deposit(myCustomer, 1000))


class Account(object):

    overdraft = 1000
    onlinestatements = False

    @staticmethod
    def allowinterest():
        interestrate = 0.05
        return "The interest rate for this account is now: ", interestrate

    @classmethod
    def allowonlinestatements(cls,onlinestatements):
        if(onlinestatements):
            return "account requires an online statement"
        else:
            return "account requires a hard copy statement"


    def __init__(self, typeofaccount, interestpayable):
        self. typeofaccount = typeofaccount
        self. interestpayable = interestpayable


studentaccount = Account('Current Account', 'No')

print('The studentaccount instance of the class has an overdraft facility of: £', studentaccount.overdraft)

print('The class has an overdraft facility of: £', Account.overdraft)


print('The statement status for this account is - ', Account.allowonlinestatements(True))

print('The statement status for this account is - ', Account.allowonlinestatements(False))