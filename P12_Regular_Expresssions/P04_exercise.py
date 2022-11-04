# email 
# passowrd contain 8 digit with special charcter(@#$%)
# password end with a number
import re

email_pattern = re.compile(
    r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email_id = 'psf@python.org'


password_patter = re.compile(r"([a-zA-Z0-9@#$%]{8,}\d$)")
password = '123456789$'
check_password = password_patter.fullmatch(password)

check_email = email_pattern.fullmatch(email_id)
if check_email and check_password:
    print("Both email and password are correct.")
else:
    print("Try again.")