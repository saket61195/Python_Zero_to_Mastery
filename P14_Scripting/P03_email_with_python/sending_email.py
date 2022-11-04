import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Saket Prabhakar'
email['to'] = 'aspire404@protonmail.com'
email['subject'] = 'This is testing'

email.set_content('i am learning Python and testing again')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('prabhakar61195@gmail.com', 'hywlwkvlhjdmndkp')
    smtp.send_message(email)
    print('all good boss!')