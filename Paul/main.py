from student_manager import*

def menu():
    print("""
===========================================
----WELCOME TO BRIGHT FUTURE UNIVERSITY----
===========================================    
1. Create Student
2. View Student Record
3. View Student Courses
4. Add Course
5. Remove Course
6. Update Student Info
7. Total Students
8. Exit
""")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        display_student_record(input("Username: "))
    elif choice == "3":
        display_student_courses(input("Username: "))
    elif choice == "4":
        add_course(input("Username: "), input("Course: "))
    elif choice == "5":
        remove_course(input("Username: "), input("Course: "))
    elif choice == "6":
        update_student_info(
            input("Username: "),
            name=input("New name: "),
            age=int(input("New age: ")),
            city=input("New city: "),
            zip_code=input("New zip code: ")
        )
    elif choice == "7":
        total_students()
    elif choice == "8":
        break
    else:
        print("Invalid option.")
