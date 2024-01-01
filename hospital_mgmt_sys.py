import pandas as pd
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

    def __init__(self, date, staff_ID, patient_ID, time):

        self.staff_ID = staff_ID
        self.patient_ID = patient_ID
        self.time = time
        self.date = date

    def book_appt(self):

        file_path = "Appointment_scheduler\\" + (self.date) + "_" + str(self.staff_ID) + ".csv"

        #Read a pandas file
        df = pd.read_csv(file_path)
        
        #Locate, within the time column where equal to time provided. Then in patient
        #ID column put in the patient ID
        df.loc[df["Time"]==self.time, "Patient ID"] = self.patient_ID

        #Save CSV filfe
        df.to_csv(file_path, index=False)


    def delete_appt(self):
        
        file_path = "Appointment_scheduler\\" + (self.date) + "_" + str(self.staff_ID) + ".csv"

        #Reading the file as a dataframe
        df = pd.read_csv(file_path)

        #Locate the column where the data shall be removed
        df.loc[df["Time"]==self.time, "Patient ID"] = None

        #Save CSV filfe
        df.to_csv(file_path, index=False)

    def free_time(self):
        pass
            
    def date_syntax_checker (self):

        def func_check(self):
            #this checks that the string is the correct length
            if len(self) == 10:
                print("String is correct length")
            else:
                print("String is not the correct length")
                return False 
                    
            split_string = self.split("/")
            #split the string based on the separator

            if len(split_string[0]) == 2 and len(split_string[1]) == 2 and len(split_string[2]) == 4:
                #check if the dates are correctly structured by checking the breakdown of the string
                print("The date provided matches the required format")
                return True
            else:
                print("The date does not match the required format")
                return False

        start_check = func_check(self.start_date)
        end_check = func_check(self.end_date)

        if start_check and end_check == True:
            #check if the strings returned true or false
            print("The date is in the correct format")
        else:
            print("The dates are not in the correct format")

    def schedule_gen(staff_ID):
        #Inputs are start date & end date. The opening and closing of doctors office will remain constant
        date = "17-10-23"

        #list for time to be input, done in 15 minute increments w/ 1hour break
        time_list = [900, 915, 930, 945, 
                     1000, 1015, 1030, 1045, 
                     1100, 1115, 1130, 1145, 
                     1200, 1215, 1230, 1245, 
                     1400, 1415, 1430, 1445, 
                     1500, 1515, 1530, 1545, 
                     1600, 1615, 1630, 1645, 
                     1700, 1715, 1730, 1745]

        df = pd.DataFrame(time_list)
        df.columns = ['Time']
        df["Patient ID"] = None

        csv_file_path = "Appointment_scheduler\\" + date + "_" + str(staff_ID) + ".csv"

        df.to_csv(csv_file_path, index=False)
#newapt = Appointment("15/10/23", "17/10/2023").date_syntax_checker()
            
#nnewapt = Appointment.schedule_gen(91001)
        
appt_book = Appointment("17-10-23", 91001, 1000, 900).book_appt()
appt_remove = Appointment("17-10-23", 91001, 1000, 900).delete_appt()