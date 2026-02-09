import university_mangement_system
students = university_mangement_system
user_input = 10
while user_input != 0:
    menu = """"
        WELCOME TO BRIGHT FUTURE UNIVERSITY
        1. Register New Student
        2. Display Student Record
        3. Display Student Courses
        4. Display Student Address
        5. Add New Student Course
        6. Remove Student Course
        7. Update Student Records
        8. Show Overall Number Of Students Registered
        0. Exit
           """
    print(menu)
    user_input = int(input("Please enter your choice: "))
    match user_input:
        case 1:
            students.student_data()
        case 2:
            students.display_student_record()
        case 3:
            students.display_student_courses()
        case 4:
            print("1. Display Student Zipcode")
            print("2. Display Student Address")
            selection = int(input("Please enter your choice: "))
            match selection:
                case 1:
                    students.display_student_zipcode()
                case 2:
                    students.display_student_address()
        case 5:
            students.add_new_course()
        case 6:
            students.remove_student_course()
        case 7:
            students.update_various_fields()
        case 8:
            students.display_number_of_students()
        case 0:
            break




