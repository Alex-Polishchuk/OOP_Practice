#Creating a hospital management system
#First goal: track who is coming in and out of hospital (manage appointment)
#Second goal: manage doctors and nurses
#Thrid goal: manage patient
class Hosipital():

    def __init__(self, hspt_name, hspt_cap):
        self.hspt_name = hspt_name
        self.hspt_cap = hspt_cap

    def hospital_attr(self):
        print(f"{self.hspt_name} has a capacity of {self.hspt_cap}")

class Department(Hosipital):

    def __init__(self, dept_name, dept_cap, hspt_name, hspt_cap):
        self.dept_name = dept_name
        self.dept_cap = dept_cap

        #inherit attributes from parent class
        super().__init__(hspt_name, hspt_cap)

    def capacity_change(self, value, dept_cap):

        if isinstance(value, int):
            self.dept_capt = self.dept_cap + value

        else:
            print("Error")


class Patient(Department):
    
    def __init__(self,fname, lname,status, dept_name, dept_cap, hspt_name, hspt_cap):
        self.fname = fname
        self.lname = lname
        self.status = status

        #inherit attributes from parent class 
        super().__init__(dept_name, dept_cap, hspt_name, hspt_cap)

hosp1 = Hosipital("QMUL", 200)
radiology = Department("Radiology", 40, "QMUL", 200)

print(radiology.hspt_cap)

#AlexT = Patient("Alex", "Tkachenko", "Sick", radiology)

#by changing function in parent class, it doesn't affect the parent class (we wont have to worry about breaking the parent class)

