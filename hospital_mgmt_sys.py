import pandas as pd
from datetime import datetime
import csv

patient_data = pd.read_csv("patient.csv")
staff_data = pd.read_csv("staff.csv")

print(patient_data)
print(staff_data)
class Staff():
    
    #creating a staff class
    def __init__(self, name, role, department):
        self.name = name
        self.role = role
        self.department = department

    def add_staff(self, name, role, department):
        #function which adds staff to file containing data

        with open ('staff.csv', mode='a', newline='\n') as file:
            
            #create a csv writer
            csv_write = csv.writer(file)

            #append the data
            data_to_append = [name, role, department]
            csv_write.writerow(data_to_append)
        
        print("Data appended succesfully")

    def remove_staff(self, fname, lname, role, department):
        pass

class Patient():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def add_patient (self, fname, lname, id):
        new_data = {'ID': id, 'First_name': fname, 'Last_name':lname }
        patient_data.loc[len(patient_data)] = new_data

    def remove_patient(self, fname, lname, deaprtment):
        pass
class Appointment():

    def __init__(self, time_start, time_finish, date, staff_ID, patient_ID):
        self.time_start = time_start
        self.time_finish = time_finish
        self.date = date
        self.staff_ID = staff_ID
        self.patient_ID = patient_ID
        


    def book_appt(self, time, date, department, doctor):
        pass

#new_P = Patient('Alex', 'Tkachenko', 1000)
#new_P.add_patient('Alex', 'Tkachenko', 1000)
new_staff = Staff('Brando Tye', 'Physiotherapist', 1004)
new_staff.add_staff('Brando Tye', 'Physio', 1004)

print(staff_data)