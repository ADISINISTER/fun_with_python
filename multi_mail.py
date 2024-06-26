import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'sujeetkyt102@gmail.com'
EMAIL_PASSWORD = 'toydthmjvfvpamki'


# List of recipient emails
recipients = ['sujeetk102@gmail.com', 'adisin3503@gmail.com', 'adisin2604@gmail.com']

def send_email(subject, body, recipient):
    message = MIMEMultipart()
    message['From'] = EMAIL_USERNAME
    message['To'] = recipient
    message['Subject'] = subject

    # Attach the email body
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()

        # Log in to the email account
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)

        # Send the email
        server.sendmail(EMAIL_USERNAME, recipient, message.as_string())

        # Close the connection
        server.quit()

        print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {str(e)}")

# Loop through recipients and send the email
for recipient in recipients:
    subject = 'Hello from Python!, mail sent for goodwill'
    body = f'Dear {recipient.split("@")[0]},\n\nThis is a test email sent using Python.\n\nBest regards,\nYour Name'
    send_email(subject, body, recipient)
