
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def mail_to_user(image_path):
#def mail_to_user(recipient_email):
    sender_email="example@gmail.com"
    sender_passwd="ur password"
    recipient_email="example@gmail.com"
    

    msg=MIMEMultipart()
    msg['From']=sender_email
    msg['To']=recipient_email
    msg["Subject"]="Alert message"

    body="Some unauthorized person movement have been identified in door camera. the person detail have been attached with the mail"
    msg.attach(MIMEText(body,'plain'))
    

    
    with open(image_path,'rb') as f:
        image_data = f.read()
        attachment=MIMEApplication(image_data)
        attachment.add_header('content-Disposition','attachment',filename=image_path)
        msg.attach(attachment)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.starttls
        smtp.login(sender_email,sender_passwd)
        smtp.send_message(msg)

    print("mail sent successful")


