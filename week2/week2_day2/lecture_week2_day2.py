
class EmptyClass():
    pass

class Position():

    def __init__(self, ticker, amount):
        self.ticker = ticker
        self.shares = amount

    def buy(self, amount):
        self.shares = self.shares + amount

    def sell(self, amount):
        if self.shares <= amount:
            self.shares = self.shares - amount
        else:
            print("not enough")

    def getprice(self):
        # getneworkprice(self.ticker)
        return 3.50

    def value(self):
        return self.getprice() * self.shares

    def __str__(self):
        return "{} shares of {} at {}".format(self.shares, self.ticker, self.getprice())


class ParentClass():
    def __init__(self, x):
        self.x = x

    def hello(self):
        print("hello, my x value is {}".format(self.x))

class CreditCard():
    
    def __init__(self, ccnumber):
        self.cardtype = None
        self.validate()

    def validate(self):
        if valid:
            self.cardtype = "VISA" #etc.


card = CreditCard(register.readcard())

if CreditCard.cardtype:
    