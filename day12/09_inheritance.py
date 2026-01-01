# overriding methods
class Bank:
    def rate_of_interest(self):
        return 0
class x_bank(Bank):
    def rate_of_interest(self):
        return 10.5
class y_bank(Bank):
    def rate_of_interest(self):
        return 5

x=x_bank()
print(x.rate_of_interest())

y=y_bank()
print(y.rate_of_interest())


