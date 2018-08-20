import re

def phone_number(string):
    expression = "[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]"
    match = re.search(expression, string)
    if match is None:
        return False
    else:
        return True