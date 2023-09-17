#Creating a hospital management system
#First goal: track who is coming in and out of hospital (manage appointment)
#Second goal: manage doctors and nurses
#Thrid goal: manage patient
class Staff():

    def __init__(self, fname, lname, role, department):
        self.fname = fname
        self.lname = lname
        self.role = role
        self.department = department

    def dept_staff():
        #List through all staff of a particular department
        pass

class Patient():

    def __init__(self, fname, lname, department):
        pass


class Appointment():

    def __init__(self, time, date, department):

        self.time = time
        self.date = date
        self.department = department


#by changing function in parent class, it doesn't affect the parent class (we wont have to worry about breaking the parent class)

