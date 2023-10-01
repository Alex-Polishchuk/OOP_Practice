#Creating a hospital management system
#First goal: track who is coming in and out of hospital (manage appointment)
#Second goal: manage doctors and nurses
#Thrid goal: manage patient
import pandas as pd

#patient data dataframe
patient_data = pd.DataFrame(columns=["ID", "First_name", "Last_name"])
print(patient_data)


class Staff():

    def __init__(self, fname, lname, role, department):
        self.fname = fname
        self.lname = lname
        self.role = role
        self.department = department

    def add_staff(self, fname, lname, role, department):
        #takes all the above and adds it to SQL db 
        pass

    def remove_staff(self, fname, lname, role, department):
        pass

class Patient():

    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id

    def add_patient (self, fname, lname, id):
        new_data = {'ID': id, 'First_name': fname, 'Last_name':lname }
        patient_data.loc[len(patient_data)] = new_data

    def remove_patient(self, fname, lname, deaprtment):
        pass
class Appointment():

    def __init__(self, time, date, department, doctor):

        self.time = time
        self.date = date
        self.department = department
        self.doctor = doctor

    def book_appt(self, time, date, department, doctor):
        pass

new_P = Patient('Alex', 'Tkachenko', 1000)
new_P.add_patient('Alex', 'Tkachenko', 1000)
print(patient_data)