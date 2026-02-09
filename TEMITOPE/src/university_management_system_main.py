from university_management_system_function import *


def main_menu():
    choice = -1

    while choice != 0:
        print("""
        1. Create student record
        2. Display student record
        3. Display student courses
        4. Display student zip_code
        5. Display student city
        6. Add course
        7. Remove course
        8. Update student information
        9. Overall number of students
        0. Exit
        """)

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                username = input("Enter your username: ")
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                courses = input("Enter your courses: ")
                city = input("Enter your city: ")
                zip_code = int(input("Enter your zip_code: "))
                create_student_record(username, name, age, courses, city, zip_code)
                print("Student record created successfully")

            case 2:
                username = input("Enter your username: ")
                print(display_student_record(username))

            case 3:
                username = input("Enter your username: ")
                print(display_student_courses(username))

            case 4:
                username = input("Enter your username: ")
                print(display_student_zip_code(username))

            case 5:
                username = input("Enter your username: ")
                print(display_student_city(username))

            case 6:
                username = input("Enter your username: ")
                course = input("Enter course to be added: ")
                print(add_course(username, course))

            case 7:
                username = input("Enter your username: ")
                course = input("Enter course to be removed: ")
                print(remove_course(username, course))

            case 8:
                username = input("Enter your username: ")
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                city = input("Enter your city: ")
                zip_code = int(input("Enter your zip_code: "))
                print(update_student_record(username, name, age, city, zip_code))

            case 9:
                print("Overall number of students is:", overall_number_of_students())

            case 0:
                print("Exiting....")
                break

            case _:
                print("Invalid input")

main_menu()