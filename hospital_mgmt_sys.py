#Creating a hospital management system
#First goal: track who is coming in and out of hospital (manage appointment)
#Second goal: manage doctors and nurses
#Thrid goal: manage patient
import sqlite3

#Creating connection to sql database
conn = sqlite3.connect('staff_detail.db')
cursor = conn.cursor()

#WRITE CHAGNES HERE
conn.commit()
conn.close()
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

    def __init__(self, fname, lname, department):
        self.fname = fname
        self.lname = lname
        self.department = department

    def add_patient (self, fname, lname, department):
        pass

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