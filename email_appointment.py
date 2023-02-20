import win32com.client as win32
from appointment_gui import yes_no, email_review
import PySimpleGUI as pg
from Schedule_appointment import save_appointment,find_appointment,load_appointment,delete_appointment

def email_appt_request(appt_dict:dict):
    name = f'{appt_dict["fn"]} {appt_dict["ln"]}'
    text = f"""Hello, Loye.
    We have an appointment request from {name} (ID#:{appt_dict['sid']}) for {appt_dict["course"]} tutoring. Would you be able to meet with the student at the following time?
    {appt_dict["pretty date"]} at {appt_dict['time']}\n
    If so, I will send out a confirmation email. If not, I will ask the student for a different time.\n
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
        mail.To = ""
        mail.CC = ""
    mail.Subject = f"Appointment Request: {appt_dict['pretty date']} @ {appt_dict['time']}"
    mail.Body = text
    
    if email_review(mail) == "Send":
        save_appointment(appt_dict)
        mail.Send()

    else:
        pg.Popup('Email not Sent')



def email_appt_conf():
    path = find_appointment()
    appt_dict = load_appointment(path)
    name = appt_dict['fn']
    text = f"""Hello, {name}. 
    Your appointment with Loye for {appt_dict['course']} at {appt_dict['time']} on {appt_dict['pretty date']} has been confirmed.
    At the time of the appointment, please use the Zoom link below to join the tutoring session.\n
    https://mcckc.zoom.us/j/99568429730?pwd=VC94MFZVRkpNbjlzdjhUQWF6SFFCQT09\n
    If you have any questions or concerns, please let me know.
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
        mail.To = f'{appt_dict["sid"]}@student.mcckc.edu'
    mail.Subject = f"Appointment Confirmed: {appt_dict['pretty date']} @ {appt_dict['time']}"
    mail.Body = text

    if email_review(mail) == "Send":
        mail.Send()
        delete_appointment(path)
    else:
        pg.Popup('Email not Sent')
    
if __name__ == "__main__":  
    pass
