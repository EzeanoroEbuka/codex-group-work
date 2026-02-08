from SAMUEL.student import *

def id_exist(student_id):
    return id_exists(student_id)

def display_students_records():
    for student in university_record:
        student_id = student["Unique_user_ID"]
        print(get_student_info(student_id))

def display_student_subject(student_id):
    if id_exist(student_id):
        print(f"Courses offered by student {student_id.upper()}")
        print("------------------------------")
        if len(get_student_courses(student_id)) > 0:
            for course in get_student_courses(student_id):
                print(course)
    print("------------------------------")
    print("student does not exist")

def display_student_post_code(student_id):
    if id_exist(student_id):
        zip_code = get_student_zip_code(student_id)
        print(f"Post Code of student {student_id.upper()}: {zip_code}")
    print("------------------------------")
    print("student does not exist")

def display_student_city(student_id):
    if id_exist(student_id):
        student = get_student_by_id(student_id)
        city = student.get("student_info")["Address"]["City"]
        print(f"City of student {student_id.upper()}: {city}")
    print("------------------------------")
    print("student does not exist")

def add_students_course(student_id, course):
    if id_exist(student_id):
        add_status = add_student_courses(student_id, course)
        print(add_status)
    print("------------------------------")
    print("student does not exist")

def update_students_course(student_id, old_course, new_course):
    if id_exist(student_id):
        update_status = update_student_course(student_id, old_course, new_course)
        print(update_status)
    print("------------------------------")
    print("student does not exist")

def update_students_age(student_id, age):
    if id_exist(student_id):
        update_status = update_student_age(student_id, age)
        print(update_status)
    print("------------------------------")
    print("student does not exist")



add_students_course("id3","Physics")
#
# display_students_records()