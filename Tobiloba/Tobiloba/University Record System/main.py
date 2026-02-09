from student import *
from validation import *

while True:

    print("Welcome to the University Management System!"
        
        "Please select an option:")
    print("1. Add a student")
    print("2. View student details")
    print("3. Update student courses")
    print("4. Remove a course from a student")
    print("5. Total number of students")
    print("6. Exit")

    
    choice = input("Enter your choice (1-6): ")
    
    match choice:
        case "1":
            username = input("Enter student username(3–20 letters, numbers, _): ")
            while True:
                if not validate_input(user_namepattern, username):
                    print("Invalid username format.")
                    continue
                else:
                    break
            while True:
                name = input("Enter student name (letters only): ")
                if not validate_input(namepattern, name):
                    print("Invalid name format.")
                    continue
                else:
                    break
            while True:
                age = int(input("Enter student age(16-40): "))
                if not validate_input(age_pattern, str(age)):
                    print("Invalid age format.")
                    continue
                else:
                    break
            while True:
                courses = input("Enter student courses (comma-separated 3- 15 characters): ").split(",")
                if not validate_input(course_pattern, ", ".join(courses)):
                    print("Invalid course format.")
                    continue
                else:
                    break
            while True:
                city = input("Enter student city(3-20 letters only): ")
                if not validate_input(city_pattern, city):
                    print("Invalid city format.")
                    continue
                else:
                    break
            while True:
                zip_code = input("Enter student zip code(5 digits): ")
                if not validate_input(zip_code_pattern, zip_code):
                    print("Invalid zip code format.")
                    continue
                else:
                    break
            create_student(username, name, age, courses, city, zip_code)
        case "2":
            while True:
                username = input("Enter student username(3–20 letters, numbers, _): ")
                if not validate_input(user_namepattern, username):
                    print("Invalid username format.")
                    continue
                else:
                    break
            display_Student(username)
        case "3":
            while True:
                username = input("Enter student username(3–20 letters, numbers, _): ")
                if not validate_input(user_namepattern, username):
                    print("Invalid username format.")
                    continue
                else:
                    break
            while True:
                old_course = input("Enter course to update(3- 15 characters): ")
                if not validate_input(course_pattern, old_course):
                    print("Invalid course format.")
                    continue
                else:
                    break
            while True:
                new_course = input("Enter new course name(3- 15 characters): ")
                if not validate_input(course_pattern, new_course):
                    print("Invalid course format.")
                    continue
                else:
                    break
            update_course(username, old_course, new_course)
        case "4":
            while True:
                username = input("Enter student username(3–20 letters, numbers, _): ")
                if not validate_input(user_namepattern, username):
                    print("Invalid username format.")
                    continue
                else:
                    break
            while True:
                course = input("Enter course to remove(3- 15 characters): ")
                if not validate_input(course_pattern, course):
                    print("Invalid course format.")
                    continue
                else:
                    break
            remove_course(username, course)
        case "5":
            total_students()
        case "6":
            print("Exiting the system. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")  