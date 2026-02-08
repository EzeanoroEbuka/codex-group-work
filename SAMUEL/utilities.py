import re

from SAMUEL import student
from SAMUEL.student import university_record






def is_valid_name(name: str) -> bool:
    pattern = r"^[A-Za-z]+([ '-][A-Za-z]+)*$"
    if re.match(pattern, name):
        return True
    return False

#
# print(is_valid_name("samuel"))