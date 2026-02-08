import re

def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]{2,30}", name))

def validate_student_id(student_id):
    return bool(re.fullmatch(r"[A-Za-z0-9]{2,10}", student_id))

def validate_city(city):
    return bool(re.fullmatch(r"[A-Za-z ]{2,30}", city))

def validate_zip_code(zip_code):
    return bool(re.fullmatch(r"\d{5,6}", zip_code))
