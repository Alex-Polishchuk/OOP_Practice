
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
        
a1 = Bank("alex", 500)
a1.bal_check()
a1.deposit()
a1.bal_check()
