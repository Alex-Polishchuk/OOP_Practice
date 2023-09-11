#Creating a hospital management system
#First goal: track who is coming in and out of hospital
#Second goal: track capacity and whether we're over capacity
#Thrid goal: create multiple departments and track their capacity

class Hosipital():

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def hospital_attr(self):
        print(f"{self.name} has a capacity of {self.capacity}")

class Department(Hosipital):

    def __init__(self, dept_name, dept_capacity):
        self.dept_name = dept_name
        self.dept_capacity = dept_capacity

    