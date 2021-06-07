import re


def email_parse(email):
    re_email = re.compile(r'(?P<username>\w+)@(?P<domain>[A-Za-z]+\.[A-Za-z]+)')
    if re_email.match(email) != None:
        return re_email.match(email).groupdict()
    else:
        raise ValueError(f'wrong email {email}')
