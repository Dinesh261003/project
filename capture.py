#sending the alert msg

import sms
import mail

def captureall(image_path):
    sms.sendsms()
    
    mail.mail_to_user(image_path)
    sms.sms_to_neighbour()

