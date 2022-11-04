from urllib import response
import requests
import hashlib


def request_api_data(query_char):

    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error feching: {res.status_code}check the api and try again')
    return res

def pwned_api_check(password):
    # sha1password = hashlib.sha1(password.encode('utf-8'))
    #hexdigest convert hash object into hexadecimal string
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1password)
    first5_char , tail = sha1password[:5], sha1password[5:]
    print(first5_char,tail)
    response = request_api_data(first5_char)
    print(response)
    return sha1password

pwned_api_check('123')
