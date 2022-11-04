

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Saket Prabhakar'
email['to'] = 'prabhakar.saket39@gmail.com'
email['subject'] = 'You Won 100000 dollars!'

# email.set_content('i am learning Python and testing again')
email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('prabhakar61195@gmail.com', 'hywlwkvlhjdmndkp')
    smtp.send_message(email)
    print('all good boss!')