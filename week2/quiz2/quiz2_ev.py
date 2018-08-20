import re

def phone_number(string):
    expression = "[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]"
    match = re.search(expression, string)
    if match is None:
        return False
    else:
        return True

print(phone_number("212-893 is my number"))




'''
* * Takes one argument, a string

* * Returns a True or False value (or a value equivalent to True or False)

* * Does not print or input

* * Returns True if the string contains a phone number of the form 555-5555
#### Test Strings:

##### should match (return a True value):

* "Jenny, don't change your number 867-5309"
and
* "555-4321? That sounds fake."

##### should not match (return a False value):

* My number is 12-8930
or
* 212-893 is my number.

#### Submissions:

* Upload your code to github and send me a link. It can either be in an existing repository or a new one.
'''