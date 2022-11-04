import re
#\d which means we have to put a digit number in the length of 8 password
password_patter = re.compile(r"([a-zA-Z0-9@#$%]{8,}\d$)")
password = '123456789'
check_password = password_patter.fullmatch(password)
print(check_password)
password1 = '@5757589598#$%'
check_password1 = password_patter.fullmatch(password1)
print(check_password1)
password2 = '@5757589598#$%4'
check_password2 = password_patter.fullmatch(password2)
print(check_password2)
