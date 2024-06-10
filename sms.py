
from twilio.rest import Client
def sendsms():
    SID='id here'
    token='token here'
    ct=Client(SID,token)
    ms="Alert: Unknown Person Detected. Some movement has been identified in the camera. For further details, refer to the email."
    ct.messages.create(body=ms,from_='provided number',to='+reciver')
    print("sms sent successfully")
    



def sms_to_neighbour():
    def send_sms(recipient_number):
        account_sid = 'acc id here'
        auth_token = 'acc token place here'
        client = Client(account_sid, auth_token)

        message_body = "Alert: Please checkout my home its an emergency -Your neighbour Dinesh "
        from_number = '+from number'

        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=recipient_number
        )

        print(f"Message sent successfully to {recipient_number}")

    # List of recipient phone numbers
    recipient_numbers = [ '+reciver','+reciver']

    # Iterate over the recipient phone numbers and send SMS to each recipient
    for recipient_number in recipient_numbers:
        send_sms(recipient_number)

