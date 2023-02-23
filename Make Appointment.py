from email_appointment import email_appt_conf,email_appt_request
from appointment_gui import appointment_info,conf_or_req



if __name__ == "__main__":
    x = conf_or_req()
    if x == "Request":
        email_appt_request(appointment_info())
    elif x == "Confirm":
        email_appt_conf()
    else:
        raise Exception("Nothing Happened")
