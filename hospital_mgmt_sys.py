import pandas as pd
from datetime import datetime
import csv

patient_data = pd.read_csv("patient.csv")
staff_data = pd.read_csv("staff.csv")

class Staff():
    
    #creating a staff class
    def __init__(self, name, role, department):
        self.name = name
        self.role = role
        self.department = department

    def add_staff(self):
        #function which adds staff to file containing staff data

        with open ('staff.csv', mode='a', newline='\n') as file:
            
            #create a csv writer
            csv_write = csv.writer(file)

            #append the data
            data_to_append = [self.name, self.role, self.department]
            csv_write.writerow(data_to_append)

        #when exiting with function, csv file automatically closed
        print("Data appended succesfully")

    def remove_staff(self):
        #function to remove particular staff member based on id
        staff_ID_input = str(input("Please input the staff ID number you wish to remove: "))
        match_ID = False
            
        with open('staff.csv', mode='r') as file:
            
            reader_obj = csv.reader(file)

            for row in reader_obj:
                iterr_ID = (row[3])
            
                if staff_ID_input == iterr_ID:
                    print(iterr_ID, staff_ID_input)
                    print(type(iterr_ID))
                    print(type(staff_ID_input))
                    match_ID = True
                    print("Match Found")
                    break
                else:
                    print("No match found")


class Patient():

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def add_patient (self):
        
        with open ('patient.csv', mode='a', newline='\n') as file:

            #creating a csv writer
            csv_write = csv.writer(file)

            #specify which data is to be appeneded and append it
            patient_data_append = [self.name, self.id]
            csv_write.writerow(patient_data_append)

            print('Patient data succesfully appended')

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
Staff('Brando Tye', 'Physiotherapist', 1004).remove_staff()