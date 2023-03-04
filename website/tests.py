import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PASSWORD_SENDER = 'Anepaspirater123@'
EMAIL_SENDER = 'contact@dgital.org'

def send_email(customer_name, company_name, phone_number, email, interest, message):
    # Create a message object
    message = MIMEMultipart()
    message['From'] = EMAIL_SENDER
    message['To'] = "leonel.zone@yahoo.fr"
    message['Subject'] = 'New Email from Potential Customer'

    # Add message body
    body = f'Dear Zone Yemeli,\n\nI hope this email finds you well. I wanted to reach out to let you know that we have received a new email from a potential customer who is interested in our products/services. As the CEO of our company, I believe you would be interested in hearing about this exciting development!\n\nThe email was sent by {customer_name}, who expressed interest in learning more about what we do and how we can help their business grow. They seem like a great fit for our company and I believe there is a lot of potential for us to work together.\n\nI have already replied to the email and provided some initial information about our products/services. However, I think it would be a great idea for you to personally follow up with {customer_name} to introduce yourself and discuss how we can assist them.\n\nI have included the email below for your reference. Let me know if you have any questions or if you would like me to set up a call for you and {customer_name} to discuss further.\n\nThank you for your time and consideration.\n\nBest regards,\nDigtal Developer\'s Team'
    message.attach(MIMEText(body, 'plain'))

    # Include the previous email in the message body
    previous_email = f"""Email from {company_name},\nPhone:{phone_number},\nEmail:{email},\nInterest:{interest}"""
    message.attach(MIMEText(previous_email, 'plain'))

    # Set up SMTP connection
    smtp_server = 'smtp.ionos.de'
    smtp_port = 587
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(EMAIL_SENDER, PASSWORD_SENDER)

    # Send email
    smtp_connection.sendmail(EMAIL_SENDER, "leonel.zone@yahoo.fr", message.as_string())

    # Close SMTP connection
    smtp_connection.quit()

    print('Email sent successfully!')

send_email(customer_name='John Doe', company_name='Acme Inc.', phone_number='555-1234', email='bilimdepaullilian@gmail.com', interest='Product Inquiry', message='Hi, I am interested in learning more about your products. Can you please send me some information?')