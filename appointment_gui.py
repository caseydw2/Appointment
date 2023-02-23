import PySimpleGUI as sg
import datetime as dt

time = ['9:00AM', '9:30AM', '10:00AM', '10:30AM', '11:00AM', '11:30AM', '12:00PM', '12:30PM', '1:00PM', '1:30PM', '2:00 PM', '2:30 PM', '3:00 PM', '3:30 PM', '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM', 
        '6:00PM', '6:30PM', '7:00PM', '7:30PM', '8:00PM', '8:30PM', '9:00PM']

days_of_week = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]


def pick_time(appointments:list) ->str:
    buttons = [sg.Button(appointment) for appointment in appointments]

    layout = [[sg.Text("What appointment time was confirmed?")],
               buttons]

    window = sg.Window("Which Appointment?",layout=layout,icon = "Custom-Icon-Design-Pretty-Office-7-Calendar.ico")
    date = window.read()[0]
    window.close()
    return date

def get_day_of_the_week(date0:dt.datetime) -> str:
    if date0 == dt.date.today():
        day_of_the_week = "today"
    elif date0 == dt.date.today() + dt.timedelta(days=1):
        day_of_the_week = "tomorrow"
    else:
        day_of_the_week = days_of_week[date0.weekday()].capitalize()
    return day_of_the_week


def pretty_date(date:str) -> str:
    
    split = date.split("-")

    day = int(split[2].split(" ")[0])
    date0 = dt.date(year=int(split[0]),month= int(split[1]),day= day)
    
    day_of_the_week = get_day_of_the_week(date0)

    american_date = date0.strftime("%m/%d")
    x = f"{day_of_the_week} ({american_date})"
    return x


def number_of_options()->int:
    layout = [[sg.Text("How many request options?")],
              [sg.Combo([1,2,3],k='z')],
              [sg.Submit()]]
    window = sg.Window('Number of Appointment Options.',layout=layout,icon = "Custom-Icon-Design-Pretty-Office-7-Calendar.ico")
    x = window.read()[1]['z']
    window.close()
    return x

def confirmation(events:dict)->str:
    y = [sg.Text(appointment) for appointment in events["appointments"]]

    layout = [[sg.Text("You inputed:")],
              [sg.Text(f"Name: {events['fn']} {events['ln']}")],
              [sg.Text(f"S Number: {events['sid']}")],
              [sg.Text(f"Course: {events['course']}")],
              [sg.Text("Date(s):")],
              y,
              [sg.Text(f"For {events['length']}")],
              [sg.Text(f'Comments: {events["comments"]}')],
              [sg.Text("Is this correct?")],
              [sg.Button("Yes"),sg.Button("No")]]

    window = sg.Window("Confirmation",layout=layout,icon = "Custom-Icon-Design-Pretty-Office-7-Calendar.ico")
    x = window.read()[0]
    window.close()
    return x

def appointment_info()-> dict:
    icon = "Custom-Icon-Design-Pretty-Office-7-Calendar.ico"
    correct = "No"
    options_num= number_of_options()
    y = [[[sg.CalendarButton(f"Date {i}")],[sg.Combo(time,k=f"time {i}")]] for i in range(options_num)]
    while correct != "Yes":
    

        layout =[[sg.Text("Fill in the information below.")],
                [sg.Text("First Name"),sg.InputText(k="fn")],
                [sg.Text("Last Name"),sg.InputText(k="ln")],
                [sg.Text("S Number"),sg.InputText(k="sid")],
                [sg.Text("Course"),sg.InputText(k="course")]] + y + [[sg.Text("Length of Session"), sg.Combo(["30 Minutes","1 Hour"],k="length")],
                [sg.Text("Comments?")],
                [sg.Multiline("",k="comments")],
                [sg.Submit(),sg.Cancel()]]
        
        window = sg.Window("Make Appointment", layout,icon=icon)
        x = window.read()[1]
        x["comments"] += '\n'
        x["course"] = x['course'].upper()
        window.close()
        appointments = []
        for i in range(options_num):
            appointments.append(f"{pretty_date(x[f'Date {i}'])} at {x[f'time {i}']}")
        x["appointments"] = appointments
        correct = confirmation(x)
    return x

def yes_no(text:str) -> str:
    layout = [[sg.Text(text)],
              [sg.Button("Yes"),sg.Button("No")]]
    window = sg.Window("Yes or No",layout,icon = "Custom-Icon-Design-Pretty-Office-7-Calendar.ico")
    x = window.read()[0]
    window.close()
    return x

def email_review(mail) ->str:
    layout = [[sg.Text("Please review the information below")],
              [sg.Text(f"To: {mail.To}")],
              [sg.Text(f'CC: {mail.CC}')],
              [sg.Text(f"BCC: {mail.BCC}")],
              [sg.Text(f"Subject: {mail.Subject}")],
              [sg.Text(f'Body: {mail.Body}')],
              [sg.Text("Want to send it?")],
              [sg.Button("Send"),sg.Cancel()]]
    window = sg.Window("Email Review",layout,icon = "Custom-Icon-Design-Pretty-Office-7-Calendar.ico")
    x = window.read()[0]
    window.close()
    return x

def conf_or_req():
    layout = [[sg.Text("Would you like to Request or Confirm an Appointment?")],
              [sg.Button("Request"),sg.Button("Confirm"),sg.Cancel()]]
    window = sg.Window("Confirm/Request", layout,icon = "Custom-Icon-Design-Pretty-Office-7-Calendar.ico")
    x = window.read()[0]
    window.close()
    return x

