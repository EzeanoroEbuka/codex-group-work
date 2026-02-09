from SAMUEL.university_record_input_handler import *


def menu():
    menu = """
=============================
UNIVERSITY MANAGEMENT SYSTEM  
-----------------------------
1.  Add Student
2.  Add Student Course
3.  Update Students info
4.  View Students Info
5.  View all Available Student Record
0.  Exit
---------------------------
    """
    return menu

def update_submenu():
    menu = """
===========================
    UPDATE SUBMENU
---------------------------
1.  Update Student Name
2.  Update Student Zip Code
3.  Update Student City
4.  Update Student Age
5.  Update Student Course
6.  Back
----------------------------
    """
    return menu

def get_submenu():
    menu = """
=============================
    VIEW STUDENT INFO
-----------------------------
1. Get Student City
2. Get Student Course
3. Get Student Zip Code
4. Get Numbers Of Students
5. Get Individual Student Records
6. Back
---------------------------------
    """
    return menu


def display_menu():
    option = 1
    while option != 0:
        print(menu())
        option = input("Enter your choice: ")
        match option:
            case 1: create_student()
            case 2: add_course()
            case 3:
                sub_option = 1
                while sub_option != 9:
                    print(update_submenu())
                    sub_option = input("Enter your choice: ")
                    match sub_option:
                        case 1: update_student_name()
                        case 2: update_student_zip_code()
                        case 3: update_student_city()
                        case 4: update_student_age()
                        case 5: update_course()
                        case 6: break
                        case _: print("Invalid input")
            case 4:
                sub_option = 1
                while sub_option != 5:
                    print(get_submenu())
                    sub_option = input("Enter your choice: ")
                    match sub_option:
                        case 1: get_student_city()
                        case 2: get_student_courses()
                        case 3: get_student_zip_code()
                        case 4: get_number_of_students()
                        case 5: get_student_info()
                        case 6: break
                        case _: print("Invalid input")
            case 5: display_students_records()
            case 0: break
            case _: print("Invalid input")
    print("Exiting....")


display_menu()
