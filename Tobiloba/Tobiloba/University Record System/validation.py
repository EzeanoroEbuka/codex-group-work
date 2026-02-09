# validation

import re

user_namepattern = re.compile(r'^[a-zA-Z0-9_]{3,12}$')
namepattern = re.compile(r'^[a-zA-Z0-9_]{3,20}$')
age_pattern = re.compile(r'^(1[6-9]|[2-9][0-9]|40)$')
course_pattern = re.compile(r'^[a-zA-Z\s]{3,15}$')
city_pattern = re.compile(r'^[a-zA-Z\s]{3,20}$')
zip_code_pattern = re.compile(r'^[0-9]{5}$')


def validate_input(pattern, userInput):
    if pattern.match(userInput):
        return True
    else:
        return False




