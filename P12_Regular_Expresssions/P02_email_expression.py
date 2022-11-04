import re

email_pattern = re.compile(
    r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email_id = 'psf@python.org'
check_email = email_pattern.fullmatch(email_id)
print(check_email)
email_id1 = 'psf@python'
check_email1 = email_pattern.fullmatch(email_id1)
print(check_email1)
