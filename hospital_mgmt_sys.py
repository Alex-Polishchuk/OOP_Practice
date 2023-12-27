import pandas as pd
from datetime import datetime
import calendar
import csv

class Staff():
    
    #creating a staff class
    def __init__(self, name, role, department):
        self.name = name
        self.role = role
        self.department = department

    def add_staff(self):
        #function which adds staff to file containing staff data

        #opening file containing staff data
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
                iterr_ID = (row[0])
            
                if staff_ID_input == iterr_ID:
                #checking if the input has found match in the list

                    match_ID = True
                    print("Match Found")
                    
                    df = pd.read_csv('staff.csv', index_col='ID')
                    df = df.drop(int(iterr_ID))
                    df.to_csv('staff.csv', index=True)
                    break
            else:
                print("No match found in records")


class Patient():

    #initialising patient class
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

    def remove_patient(self):
        
         #function to remove particular staff member based on id
        patient_ID_input = str(input("Please input the patient ID number you wish to remove: "))
        match_ID = False
            
        with open('patient.csv', mode='r') as file:
            
            reader_obj = csv.reader(file)

            for row in reader_obj:
                iterr_ID = (row[0])
            
                if patient_ID_input == iterr_ID:
                #checking if the input has found match in the list

                    match_ID = True
                    print("Match Found")
                    
                    df = pd.read_csv('patient.csv', index_col='ID')
                    df = df.drop(int(iterr_ID))
                    df.to_csv('patient.csv', index=True)
                    break
            else:
                print("No match found in records")
class Appointment():

    def __init__(self, time_start, time_finish, date, staff_ID, patient_ID):
        self.time_start = time_start
        self.time_finish = time_finish
        self.date = date
        self.staff_ID = staff_ID
        self.patient_ID = patient_ID

    def book_appt(self):
        pass


    def delete_appt(self):
        pass

    def free_time(self):
        pass

    def schedule_gen (self, start_date, end_date):
        #this will generate a csv file which will be available for filling in a schedule.
        #Inputs are start date & end date. The opening and closing of doctors office will remain constant
        #Open at 9AM and closes at 6PM
        
        #check that start date and end date are in the correct format

        start_date_syntax = False
        end_date_syntax = False

        while start_date_syntax == False and end_date_syntax == False:
            #format required is DD/MM/YYYY
            
            def date_syntax_checker (string_checks):

                #1. check if string is correct length
                #2. check if string is correct format
                    #a.check the dashes are in the correct place
                    #b.
                #3. check if start date is before end date

                #this checks that the string is the correct length
                if len(string_checks) == 10:
                    print("String is correct length")
                else:
                    print("String is not the correct length")
                    return False   
                

                #break the string down into it's constituent dates & checks that it matches the format


                split_string = string_checks.split("/")
                if len(split_string[0]) == 2 and len(split_string[1]) == 2 and len(split_string[2]) == 4:
                    print("The date provided matches the required format")
                else:
                    print("The date does not match the required format")
                    return False
                

                
                
