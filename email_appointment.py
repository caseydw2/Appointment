import win32com.client as win32
import datetime as dt
from appointment_gui import yes_no, email_review, pick_time
import PySimpleGUI as pg
from Schedule_appointment import save_appointment,find_appointment,load_appointment,delete_appointment

def greetings(name:str) -> str:
    hour = dt.datetime.now().hour
    if hour < 12:
        return f"Good morning, {name}!"
    elif hour >= 12 and hour <= 17:
        return f"Good afternoon, {name}!"
    elif hour > 17:
        return f"Good evening, {name}!"
    else:
        return f"Hello, {name}!"

def email_appt_request(appt_dict:dict):
    name = f'{appt_dict["fn"]} {appt_dict["ln"]}'
    appointments = ""
    for appointment in appt_dict['appointments']:
        appointments += appointment.capitalize() +'\n'
    if len(appt_dict["appointments"]) > 1:
        at_listed_time = " one of the following times?"
        which_time = " let me know which time, and"
    else: 
        which_time = ""
        at_listed_time = " the following time?"

    text = f"""{greetings("Loye")}
We have an appointment request from {name} (ID#:{appt_dict['sid']}) for {appt_dict["course"].upper()} tutoring. Would you be able to meet with the student at{at_listed_time}\n
{appointments}
If so,{which_time} I will send out a confirmation email. If not, I will ask the student for a different time.\n
{appt_dict["comments"]}
Thank you very much!
Casey"""
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    if yes_no("Is this a Test?") == "Yes":
        mail.To = "casey.wheaton-werle@mcckc.edu"
        mail.Bcc = ""
        mail.CC = ""
    else:
        mail.BCC = "casey.wheaton-werle@mcckc.edu"
        mail.To = "Loye.Henrikson@mcckc.edu"
        mail.CC = ""
    mail.Subject = f"Appointment Request: {appt_dict['ln']}, {appt_dict['course']}"
    mail.Body = text
    
    if email_review(mail) == "Send":
        save_appointment(appt_dict)
        mail.Send()

    else:
        pg.Popup('Email not Sent')



def email_appt_conf():
    path = find_appointment()
    appt_dict = load_appointment(path)
    date = pick_time(appt_dict['appointments'])
    name = appt_dict['fn']
    text = f"""{greetings(name)}
Your appointment with Loye for {appt_dict['course']} tutoring for {date} has been confirmed.\n
At the time of the appointment, please use the Zoom link below to join the tutoring session.\n
https://mcckc.zoom.us/j/99568429730?pwd=VC94MFZVRkpNbjlzdjhUQWF6SFFCQT09\n
If you have any questions or concerns, please let me know.\n
Thank you!
Casey"""

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    if yes_no("Is this a Test?") == "Yes":
        mail.To = "casey.wheaton-werle@mcckc.edu"
        mail.Bcc = ""
        mail.CC = ""
    else:
        mail.BCC = "casey.wheaton-werle@mcckc.edu"
        mail.CC = "Loye.Henrikson@mcckc.edu"
        mail.To = f"{appt_dict['sid']}@student.mcckc.edu"
    mail.Subject = f"Appointment Confirmed: {date}"
    mail.Body = text

    if email_review(mail) == "Send":
        mail.Send()
        delete_appointment(path)
    else:
        pg.Popup('Email not Sent')

