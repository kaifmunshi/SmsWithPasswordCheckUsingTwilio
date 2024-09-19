from twilio.rest import Client

# Twilio credentials
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
registered_mobile_number = '+91XXXXXXXXXX'   # number has been sent to this mobile number we can change it anytime after adding to Twilio 

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def send_sms(message, to_phone_number):
    """
    Function to send SMS to a registered mobile number.
    :param message: The message to send.
    :param to_phone_number: The recipient's phone number.
    """
    try:
        message = client.messages.create(
        messaging_service_sid='MG31fbfe9d318b8b722c8afe29881f4962',
        body=message,
        to=to_phone_number
            )
        print(f"Message sent: SID {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

def check_password_and_send_sms(correct_password, max_attempts=3):
    """
    Check if the user-provided password matches the correct password and track attempts.
    If the password is provided incorrectly 3 times, send an SMS.
    :param password: The user-provided password.
    :param correct_password: The actual correct password.
    :param max_attempts: Maximum number of allowed incorrect attempts.
    """
    attempts = 0

    while attempts < max_attempts:
        user_input = input("Enter the password: ")

        if user_input == correct_password:
            print("Password correct. Access granted.")
            send_sms("The door has been unlocked!", registered_mobile_number)
            print("SMS has been sent to the ADMIN.")


            break
        else:
            attempts += 1
            print(f"Incorrect password. Attempts remaining: {max_attempts - attempts}")

        if attempts == max_attempts:
            send_sms(f"The password has been wrongly provided {max_attempts} times!", registered_mobile_number)
            print("Maximum attempts reached. SMS sent.")
            break


# Set password or we can take password from database
correct_password = "12345"
check_password_and_send_sms(correct_password)
