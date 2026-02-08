import re

from SAMUEL.university_record_helper import *

def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]{2,30}", name))

def validate_student_id(student_id):
    return bool(re.fullmatch(r"[A-Za-z0-9]{3,10}", student_id))

def validate_city(city):
    return bool(re.fullmatch(r"[A-Za-z ]{2,30}", city))

def validate_zip_code(zip_code):
    return bool(re.fullmatch(r"\d{5,6}", zip_code))


def create_student():
    student_name = input("Enter student name: ").capitalize()
    while not validate_name(student_name):
        student_name = input("Name must be all alphabet: ").capitalize()

    student_id = input("Enter student id: ").strip()
    while not validate_student_id(student_id):
        student_id = input("Id is a mixture of alphabet and digits and must be more than two character: ").strip()

    while id_exists(student_id):
        student_id = input("Id already exist choose another: ").strip()

    student_age = input("Enter student age: ").strip()
    while not student_age.isdigit() and 0 < int(student_age) < 50:
        student_age = input("Enter valid age: ").strip()

    student_city = input("Enter student city: ").strip().upper()
    while not validate_city(student_city):
        student_city = input("city must be all alpha: ").strip().upper()

    student_zip_code = input("Enter student zip code: ").strip()
    while not validate_zip_code(student_zip_code):
        student_zip_code = input("zip code must be between 5 and 6 digits only: ")
    create_students(student_name,student_age,student_id,student_city,student_zip_code)



def update_student_name():
    student_id = input("Enter student id: ").strip()
    while not validate_student_id(student_id):
        student_id = input("Id is a mixture of alphabet and digits and must be more than two character: ").strip()

    while not id_exists(student_id):
        student_id = input("Id do not exist, enter valid id: ").strip()

    student_name = input("Enter student name: ").capitalize()
    while not validate_name(student_name):
        student_name = input("Name must be all alphabet: ").capitalize()
    update_students_name(student_id,student_name)


def update_student_age():
    student_id = input("Enter student id: ").strip()
    while not validate_student_id(student_id):
        student_id = input("Id is a mixture of alphabet and digits and must be more than two character: ").strip()

    while not id_exists(student_id):
        student_id = input("Id do not exist, enter valid id ").strip()

    student_age = input("Enter student age: ").strip()
    while not student_age.isdigit() and 0 < int(student_age) < 50:
        student_age = input("Enter valid age: ").strip()
    update_students_age(student_id,student_age)


def update_student_city():
    student_id = input("Enter student id: ").strip()
    while not validate_student_id(student_id):
        student_id = input("Id is a mixture of alphabet and digits and must be more than two character: ").strip()

    while not id_exists(student_id):
        student_id = input("Id do not exist, enter valid id: ").strip()

    student_city = input("Enter student city: ").strip().upper()
    while not validate_city(student_city):
        student_city = input("city must be all alpha: ").strip().capitalize()
    update_students_city(student_id,student_city)


def update_student_zip_code():
    student_id = input("Enter student id: ").strip()
    while not validate_student_id(student_id):
        student_id = input("Id is a mixture of alphabet and digits and must be more than two character: ").strip()

    while  not id_exists(student_id):
        student_id = input("Id do not exist, enter valid id: ").strip()

    student_zip_code = input("Enter student zip code: ").strip()
    while not validate_zip_code(student_zip_code):
        student_zip_code = input("zip code must be between 5 and 6 digits only: ")
    update_students_zip_code(student_id,student_zip_code)


def add_course():
    student_id = input("Enter student id: ").strip()
    while not validate_student_id(student_id):
        student_id = input("Id is a mixture of alphabet and digits and must be more than two character: ").strip()

    while not id_exists(student_id):
        student_id = input("Id do not exist, enter valid id:  ").strip()

    course = input("Enter subject name: ").capitalize()
    while not validate_name(course):
        course = input("Must be all alphabet!! Enter again: ").capitalize()
    add_students_course(student_id,course)

def update_course():
    student_id = input("Enter student id: ").strip()
    while not validate_student_id(student_id):
        student_id = input("Id is a mixture of alphabet and digits and must be more than two character: ").strip()

    while not id_exists(student_id):
        student_id = input("Id do not exist, enter valid id:  ").strip()

    old_course = input("Enter former subject name: ").capitalize()
    while not validate_name(old_course):
        course = input("Must be all alphabet!! Enter again: ").capitalize()



    new_course = input("Enter New subject name: ").capitalize()
    while not validate_name(new_course):
        course = input("Must be all alphabet!! Enter again: ").capitalize()
    update_students_course(student_id,old_course,new_course)





update_course()
display_students_records()



































