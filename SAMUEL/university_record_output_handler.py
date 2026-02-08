from SAMUEL.student_and_university_services import *

def id_exist(student_id):
    return id_exists(student_id)

def create_students(student_name, student_age, student_id, city, student_zip_code):
    print(create_student(student_name, student_age, student_id, city, student_zip_code))


def display_students_records():
    for student in university_record:
        student_id = student["Unique_user_ID"]
        print(get_student_info(student_id))

def display_student_courses(student_id):
    if id_exist(student_id):
        print(f"Courses offered by student {student_id.upper()}")
        print("------------------------------")
        if len(get_student_courses(student_id)) > 0:
            for course in get_student_courses(student_id):
                print("------------------------------")
                print(course)
    else:
        print("------------------------------")
        print("student does not exist")

def display_student_post_code(student_id):
    if id_exist(student_id):
        zip_code = get_student_zip_code(student_id)
        print("------------------------------")
        print(f"Post Code of student {student_id.upper()}: {zip_code}")
    else:
        print("------------------------------")
        print("student does not exist")

def display_student_city(student_id):
    if id_exist(student_id):
        student = get_student_by_id(student_id)
        city = student.get("student_info")["Address"]["City"]
        print("------------------------------")
        print(f"City of student {student_id.upper()}: {city}")
    else:
        print("------------------------------")
        print("student does not exist")

def add_students_course(student_id, course):
    if id_exist(student_id):
        add_status = add_student_courses(student_id, course)
        print("------------------------------")
        print(add_status)
    else:
        print("------------------------------")
        print("student does not exist")

def update_students_course(student_id, old_course, new_course):
    if id_exist(student_id):
        update_status = update_student_course(student_id, old_course, new_course)
        print("------------------------------")
        print(update_status)
    else:
        print("------------------------------")
        print("student does not exist")

def update_students_age(student_id, age):
    if id_exist(student_id):
        update_status = update_student_age(student_id, age)
        print("------------------------------")
        print(update_status)
    else:
        print("------------------------------")
        print("student does not exist")


def update_students_name(student_id, name):
    if id_exist(student_id):
        update_status = update_student_name(student_id, name)
        print("------------------------------")
        print(update_status)
    else:
        print("------------------------------")
        print("student does not exist")


def update_students_city(student_id, city):
    if id_exist(student_id):
        update_status = update_student_city(student_id, city)
        print("------------------------------")
        print(update_status)
    else:
        print("------------------------------")
        print("student does not exist")

def update_students_zip_code(student_id, zip_code):
    if id_exist(student_id):
        update_status = update_student_zip_code(student_id, zip_code)
        print("------------------------------")
        print(update_status)
    else:
        print("------------------------------")
        print("student does not exist")

def numbers_of_students():
    print("----------------------------------------")
    print("The numbers of student available: ",len(university_record))

def display_individual_info(student_id):
    if id_exist(student_id):
        info = get_student_info(student_id)
        print("------------------------------")
        print(info)
    else:
        print("------------------------------")
        print("student does not exist")



def display_departmental_courses():
    print(f"{list(available_courses)}")