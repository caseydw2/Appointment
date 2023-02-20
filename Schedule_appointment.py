import pickle
import os
from appointment_gui import yes_no

def save_appointment(appointment_dict):
    dir_path = os.getcwd()
    firstname,lastname,date,time = appointment_dict["fn"],appointment_dict['ln'],appointment_dict['file date'],appointment_dict['time']
    time = time.replace(":","").replace(" ","")
    filename = f"{date}_{time}_{firstname} {lastname}.pickle"
    filepath = f"{dir_path}\\Appointments\\{filename}"
    with open(filepath, "wb") as handle:
        pickle.dump(appointment_dict, handle, protocol = pickle.HIGHEST_PROTOCOL)


def load_appointment(filepath:str):
    with open(filepath,'rb') as handle:
        appt_dict = pickle.load(handle)
    return appt_dict
        
def find_appointment() -> str:
    dir_path = os.getcwd()
    path = f"{dir_path}\\Appointments"
    dir_list = os.listdir(path)
    for file in dir_list:
        if file.endswith(".pickle"):
            text = f"{file}\nIs this the appointment you were looking for?"
            response = yes_no(text)
            x = file
            if response == "Yes":
                return f"{path}/{x}"
    else:
        raise Exception("Appointment not Found")
    

def delete_appointment(path:str):
    os.remove(path)
