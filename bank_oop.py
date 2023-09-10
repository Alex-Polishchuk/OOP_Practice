

class User:
    
    def __init__ (self, first_name, last_name, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_day = birth_day

    def person_details(self):
        print("Here are your details")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Birthday: {self.birth_day}")

class Bank(User):

    def __init__ (self, holding, first_name, last_name, birth_day):

        self.holding = holding
        super().__init__(first_name, last_name, birth_day)
    

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

alex_t = Bank(600, "Alex", "Tkachenko", "16/03/2000")
alex_t.person_details()

alex_t.bal_check()