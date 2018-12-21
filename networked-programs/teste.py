# Import smtplib for the actual sending function
import smtplib
import email
# Import the email modules we'll need
#from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
with open("test.txt") as fp:
    # Create a text/plain message
    msg = email.message.EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()