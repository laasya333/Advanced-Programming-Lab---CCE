#tkinter + sqlite + regex + error hadling
#student database for application in student council
#make a form with tkinter. use text bar, checkbox,radio and store into database
import tkinter as tk
from tkinter import font
import sqlite3
import re

patternemail="[a-z]+.[a-z]+@learner\.manipal\.edu"
patternphno="\d{10}"

class InvalidEmail(Exception):
    pass

class InvalidPhoneNumber(Exception):
    pass

def validate_email(email):
    if not re.match(patternemail, email):
        raise InvalidEmail("Invalid email entered.")

def validate_phno(phno):
    if not re.match(patternphno, phno):
        raise InvalidPhoneNumber("Invalid phone number entered.")

def submit():
    name=entryname.get()
    regno=entryregno.get()
    learnerid=entrylid.get()
    contact=entryphno.get()
    try:
        validate_email(learnerid)
        validate_phno(contact)
        
        entryname.delete(0, tk.END)
        entryregno.delete(0, tk.END)
        entrylid.delete(0, tk.END)
        entryphno.delete(0, tk.END)
        conn=sqlite3.connect("student_info.db")
        cursor=conn.cursor()
        cursor.execute('''
            insert into student(name, regno, email, phno)
            values(?,?,?,?)
            ''',(name, regno, learnerid, contact))
        labell=tk.Label(root, text="loaded to database.")
        labell.grid(row=6, column=0)
        conn.commit()
        cursor.close()
    except InvalidEmail as ie:
        labeler1=tk.Label(root, text=f"{ie}")
        labeler1.grid(row=3, column=2, pady=10)
    except InvalidPhoneNumber as ip:
        labeler2=tk.Label(root, text=f"{ip}")
        labeler2.grid(row=4, column=2, pady=10)
    
root=tk.Tk()#app window
root.geometry("800x600")
root.configure(bg='beige')
root.title("Application form")#window title

font1=font.Font(family="Times New Roman", size=26)#if we want diff font or size

label2=tk.Label(root, text="Enter student details", font=font1)
label2.grid(column=1)

labelname=tk.Label(root, text="Enter name: ")#name label
labelname.grid(row=1, column=0, pady=10)
entryname=tk.Entry(root)
entryname.grid(row=1, column=1)

labelregno=tk.Label(root, text="Enter registration number: ")#registration number label
labelregno.grid(row=2, column=0, pady=10)
entryregno=tk.Entry(root)
entryregno.grid(row=2, column=1)

labellid=tk.Label(root, text="Enter learner id: ")#learner id label
labellid.grid(row=3, column=0, pady=10)
entrylid=tk.Entry(root)
entrylid.grid(row=3, column=1)

labelphno=tk.Label(root, text="Enter contact: ")#contact number label
labelphno.grid(row=4, column=0, pady=10)
entryphno=tk.Entry(root)
entryphno.grid(row=4, column=1)

but=tk.Button(root, text="submit", command=submit)
but.grid(row=5, column=0, pady=10)

root.main
