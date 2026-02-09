from student import *

while True:

    print("Welcome to the University Record System!"
        
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
            username = input("Enter student username: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            courses = input("Enter student courses (comma-separated): ").split(",")
            city = input("Enter student city: ")
            zip_code = input("Enter student zip code: ")
            create_student(username, name, age, courses, city, zip_code)
        case "2":
            username = input("Enter student username: ")
            display_Student(username)
        case "3":
            username = input("Enter student username: ")
            old_course = input("Enter course to update: ")
            new_course = input("Enter new course name: ")
            update_course(username, old_course, new_course)
        case "4":
            username = input("Enter student username: ")
            course = input("Enter course to remove: ")
            remove_course(username, course)
        case "5":
            total_students()
        case "6":
            print("Exiting the system. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")  