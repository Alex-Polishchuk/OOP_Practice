
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
        
    def withdrawl(self, val):
        if isinstance(val, int) and val > 0 and val <= self.holding:
            self.holding = self.holding - val

            print(f'You have withdrawn {val}. New balance is {self.holding}')

        else:
            print("Error")

a1 = Bank("alex", 500)
a1.bal_check()
a1.deposit(250)
a1.bal_check()
a1.withdrawl(400)
a1.bal_check()