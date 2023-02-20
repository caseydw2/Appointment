import PySimpleGUI as sg
import datetime as dt

time = ['9:00AM', '9:30AM', '10:00AM', '10:30AM', '11:00AM', '11:30AM', '12:00PM', '12:30PM', '1:00PM', '1:30PM', '2:00 PM', '2:30 PM', '3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM', 
        '6:00PM', '6:30PM', '7:00PM', '7:30PM', '8:00PM', '8:30PM', '9:00PM']

days_of_week = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

def confirmation(events:dict)->str:
    split = events['Date'].split("-")
    day = int(split[2].split(" ")[0])
    date = dt.date(int(split[0]),int(split[1]),day)
    
    american_date = date.strftime("%m/%d")
    file_date = date.strftime("%m-%d")
    day_of_the_week = days_of_week[date.weekday()].capitalize()


    layout = [[sg.Text("You inputed:")],
              [sg.Text(f"Name: {events['fn']} {events['ln']}")],
              [sg.Text(f"S Number: {events['sid']}")],
              [sg.Text(f"Course: {events['course']}")],
              [sg.Text(f"Date: {day_of_the_week},{american_date} @ {events['time']}")],
              [sg.Text(f"For {events['length']}")],
              [sg.Text("Is this correct?")],
              [sg.Button("Yes"),sg.Button("No")]]
    
    events["pretty date"] = f"{day_of_the_week} ({american_date})"
    events["file date"] = f"{day_of_the_week}_{file_date}"
    window = sg.Window("Confirmation",layout=layout)
    x = window.read()[0]
    window.close()
    return x

def appointment_info()-> dict:
    correct = "No"
    while correct != "Yes":
    

        layout =[[sg.Text("Fill in the information below.")],
                [sg.Text("First Name"),sg.InputText(k="fn")],
                [sg.Text("Last Name"),sg.InputText(k="ln")],
                [sg.Text("S Number"),sg.InputText(k="sid")],
                [sg.Text("Course"),sg.InputText(k="course")],
                [sg.CalendarButton("Date")],
                [sg.Text("Time of Appointment"),sg.Combo(time,k="time")],
                [sg.Text("Length of Session"), sg.Combo(["30 Minutes","1 Hour"],k="length")],
                [sg.Submit(),sg.Cancel()]]
        window = sg.Window("Make Appointment", layout)
        x = window.read()[1]
        window.close()
        correct = confirmation(x)
        
    return x

def yes_no(text:str) -> str:
    layout = [[sg.Text(text)],
              [sg.Button("Yes"),sg.Button("No")]]
    window = sg.Window("Yes or No",layout)
    x = window.read()[0]
    window.close()
    return x

def email_review(mail):
    layout = [[sg.Text("Please review the information below")],
              [sg.Text(f"To: {mail.To}")],
              [sg.Text(f'CC: {mail.CC}')],
              [sg.Text(f"BCC: {mail.BCC}")],
              [sg.Text(f"Subject: {mail.Subject}")],
              [sg.Text(f'Body: {mail.Body}')],
              [sg.Text("Want to send it?")],
              [sg.Button("Send"),sg.Cancel()]]

    window = sg.Window("Email Review",layout)
    x = window.read()[0]
    window.close()
    return x


