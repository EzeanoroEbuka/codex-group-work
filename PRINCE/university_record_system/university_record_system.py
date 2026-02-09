student_records = {}
student_address = {}
courses = [
"Math", "Physics", "Computer Science", "Biology", "Chemistry",
"Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art",
"Music", "Engineering", "Law", "Medicine", "Business"]


def student_data():
    name = input("Please enter your name(s): ").title()
    age = input("Please enter your age: ")
    count = 1
    print("COURSES")
    for each_course in courses:
        print("(",count,").", each_course)
        count = count + 1
    course_list = []
    exit_selection = "YES"
    while exit_selection != "NO":
        course = input("Please enter enrolled course: ")
        if course.capitalize() in courses:
            course_list.append(course.capitalize())
            exit_selection = input("Do you want to add another course...Please enter yes or no: ").upper()
        else:
            print({course.capitalize()}, "Not Found")

    city = input("Please enter your city: ").capitalize()
    zipcode = input("Please enter your zipcode: ")
    username = input("Please enter a unique username: ")

    student_records[username] = {"name" : name, "age" : age, "course" : course_list}
    student_address[username] = {"city" : city, "zipcode" : zipcode}


def display_student_record():
    show_student_record = input("Enter Student ID: ")
    if show_student_record in student_records:
        print(student_records.get(show_student_record))
        print(student_address.get(show_student_record))
    else:
        print("Invalid Student ID")


def display_student_courses():
    show_student_courses = input("Enter Student ID: ")
    if show_student_courses in student_records:
        print(student_records[show_student_courses]["course"])
    else:
        print("Invalid Student ID")


def display_student_zipcode():
    show_student_zipcode = input("Enter Student ID: ")
    if show_student_zipcode in student_address:
        print(student_address[show_student_zipcode]["zipcode"])
    else:
        print("Invalid Student ID")


def display_student_address():
    show_student_address = input("Enter Student ID: ")
    if show_student_address in student_address:
        print(student_address[show_student_address]["city"])
    else:
        print("Invalid Student ID")


def add_new_course():
    verify = input("Enter student ID: ")
    if verify in student_records:
        count = 1
        for each_course in courses:
            print("(", count, ").", each_course)
            count = count + 1
        option = "YES"
        while option != "NO":
            add_course = input("Please enter course you want to add: ").capitalize()
            if add_course.capitalize() not in student_records[verify]["course"] and add_course.capitalize() in courses:
                student_records[verify]["course"].append(add_course)
                option = input("Do you want to add another course...Please enter yes or no: ").upper()
            else:
                print(add_course.capitalize(), "Invalid or already exists")
    else:
        print(verify, "Not Found")


def remove_student_course():
    verify = input("Enter student ID: ")
    if verify in student_records:
        print(student_records[verify]["course"])
        option = "YES"
        while option != "NO":
            remove_course = input("Please enter course you want to remove: ").capitalize()
            if remove_course.capitalize() in student_records[verify]["course"] and remove_course.capitalize() in courses:
                student_records[verify]["course"].pop(remove_course)
                option = input("Do you want to remove another course...Please enter yes or no: ").upper()
            else:
                print(remove_course, "Invalid or doesnt exist")
    else:
        print(verify, "Not Found")


def update_various_fields():
    verify = input("Enter student ID: ")
    if verify in student_records:
        print("1. update age")
        print("2. update name")
        print("3. update city")
        print("4. update zipcode")
        print("0. Go back to menu")
        exit_selection = 1
        while exit_selection != 0:
            enter_choice = input("Please enter your choice: ")
            if enter_choice == "1":
                student_records[verify]["age"] = input("Please enter your age: ")
            if enter_choice == "2":
                student_records[verify]["name"] = input("Please enter your name: ").title()
            if enter_choice == "3":
                student_records[verify]["city"] = input("Please enter your city: ").capitalize()
            if enter_choice == "4":
                student_records[verify]["zipcode"] = input("Please enter your zipcode: ")
            else:
                print("Invalid option")
            exit_selection = input("Press 1 to continue or 0 to exit: ")
    else:
        print(verify, "Not Found")


def display_number_of_students():
    number_of_students = len(student_records)
    print(number_of_students)





