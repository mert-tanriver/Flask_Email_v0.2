import smtplib
from email.message import EmailMessage
import os

def mail_sender(subject,to,content):
    gmailaddress = "developingserver001@gmail.com"
    gmailpassword = "Develop001"

    contacts = ['unstoppablehero99@gmail.com']

    mailto = to.split(',')
    print("Mail sent to : ", mailto)
    

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "developingserver001@gmail.com"
    msg["To"] = mailto
    msg.set_content(content)
    

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
        """ +str(content)+ """
        </body>
    </html>
    """,subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com' , 465) as smtp:
        smtp.login(gmailaddress , gmailpassword)
        
        smtp.send_message(msg)

        print("Mail Has Sent!")
        smtp.quit()

   