
class Bank:

    def __init__ (self, name, holding):

        self.name = name
        self.holding = holding

    def bal_check(self):
        print(self.holding)

    def deposit(self, val):
        if isinstance(val, int) and val > 0:
            self.holding = self.holding + val
        else:
            print("Error, cannot deposit")

    def withdrawl(self, amount_withdrawn):
        if isinstance(amount_withdrawn, int) and amount_withdrawn > 0 and self.holding >= amount_withdrawn:
            self.holding = self.holding - amount_withdrawn
            print(f'Withdrawn {amount_withdrawn} pounds. New balance {self.holding} pounds')
            
        else:
            print("Error, could not wtihdraw")

        
a1 = Bank("alex", 500)
a1.bal_check()
a1.deposit(250)
a1.bal_check()
a1.withdrawl(400)
