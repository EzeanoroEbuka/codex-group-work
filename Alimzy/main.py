

all_students = {}

DEPARTMENT_COURSES = ("Math", "Physics", "Computer Science", "Biology", "Chemistry",
"Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art",
"Music", "Engineering", "Law", "Medicine", "Business")




def create_student(name,age,courses,address_city, address_zip):
    student = {
        "name": name,
        "age": age,
        "courses": [courses],
        "address": {"city": address_city, "zip": address_zip}

    }

    return student


def get_a_student_record(username):
    if username  in all_students:
        return all_students[username]

def get_courses_of_a_student(username):
    if username in all_students:
        return all_students[username]["courses"]

def get_zip_address_of_a_student(username):
    if username in all_students:
        return all_students[username]["address"]["zip"]

def get_city_address_of_a_student(username):
    if username in all_students:
        return all_students[username]["address"]["city"]



def add_course(username, course):
    if username not in all_students:
        return "There is no student with this username"
    if course in all_students[username]["courses"]:
        return "course already registered"

    if course not in DEPARTMENT_COURSES:
        return "course not offered by the department"

    all_students[username]["courses"].append(course)



def remove_or_update_course(username, old_course, latest_course):
    if username in all_students:
        choice = input(int("press 1 to update and 2 to remove"))
        if choice == 1:
            all_students[username]["courses"].remove(old_course)
        if choice == 2:
            if old_course not in all_students[username]["courses"]:
                return "course cannot be found in the student data"
            if latest_course not in DEPARTMENT_COURSES:
                return "Course not offered by the department"

            all_students[username]["courses"].remove(old_course)


def update_student_data(username,key, new_value):
    if username in all_students:
        if key == "age":
            all_students[username]["age"] = new_value
        if key == "name":
            all_students[username]["name"] = new_value
        if key == "city":
            all_students[username]["address"]["city"] = new_value
        if key == "zip":
            all_students[username]["address"]["zip"] = new_value


def get_overall_number_of_student():
    return len(all_students)





while(True):
    menu = """
        "Welcome to Bright Future University"
        press any key to
        
        1. Register a student
        2. Check a student record
        3. update student data
        4. get total number of student
        5. Exit
        
    
    """
    print(menu)

    menu_option = int(input("Enter your choice"))


    match menu_option:
        case 1:

            username = input("Enter username")
            name = input("Enter name")
            age = input("Enter age")
            courses = input("Enter courses")
            address_city = input("Enter city of address")
            address_zip = input("Enter zip of address")
            student = create_student( name, age, courses, address_city, address_zip)
            all_students[username] = student
            print(all_students)

        case 2:
            check_student_record_menu = """
            1. check a student record
            2. check the courses of a particular student
            3. check zip code of a particular student
            4. check city of a particular student       
            """
            print(check_student_record_menu)

            student_record_choice = int(input("Enter your choice: "))
            match student_record_choice:
                case 1:
                    username = input("Enter student username: ")
                    print(get_a_student_record(username))

                case 2:
                    username = input("Enter student username: ")
                    print(get_courses_of_a_student(username))

                case 3:
                    username = input("Enter student username: ")
                    print(get_zip_address_of_a_student(username))

                case 4:
                    username = input("Enter student username: ")
                    print(get_city_address_of_a_student(username))

        case 3:
            update_student_data = """
            1. Add course for student
            2. Remove or update course for student
            3. Update student data
            
            """
            print(update_student_data)
            update_student_data_choice = int(input("Enter your choice: "))

            match update_student_data_choice:
                case 1:
                    username = input("Enter student username: ")
                    course = input("Enter course name: ")
                    add_course(username, course)
                case 2:
                    username = input("Enter student username: ")
                    old_course = input("Enter course name: ")
                    latest_course = input("Enter new course name: ")
                    remove_or_update_course(username, old_course, latest_course)
                case 3:
                    username = input("Enter student username: ")
                    key = input("Enter your key: ")
                    new_value = input("Enter new value")
                    update_student_data(username, key, new_value)

        case 4:
            print(get_overall_number_of_student())

        case 5:
            break







