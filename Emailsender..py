from email.message import EmailMessage
import ssl
import smtplib
import logging

logging.basicConfig (level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


email_sender = "hesham.tarek147@gmail.com"
email_password = # Password
email_receiver= "hesham.tarek794@gmail.com"

email_subject = " Congratulations"

body= """

Hello Hesham Hanafy, Congratulations for Registering your Thesis, I wish you All The Best!.

"""

em=EmailMessage()
em['From'] = email_sender
em['to'] = email_receiver
em['subject'] = email_subject
em.set_content(body)

context =ssl.create_default_context() #  this is crucial for creating a secure, encrypted connection when sending emails.


try:

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
        logging.info("Email Send Successfully to {}".format(email_sender))
              

except Exception as e:

        logging.error(f" Email Failed to send Because:{e}")
