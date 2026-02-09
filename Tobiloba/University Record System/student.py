
students_database = {}

courses_list = {
    "Math", "Physics", "Computer Science", "Biology", 
    "Chemistry", "Statistics", "English", "Economics", 
    "History", "Philosophy", "Sociology", "APsychology", 
    "Political Science", "Geography", "Psychology", 
    "Art", "Music", "Engineering", "Law", "Medicine", 
    "Business"
}

# demo_student =

#     students_database[username] = {
#     "unique_id": "STU11111",
#     "name": "John Paul",
#     "age": 20,
#     "courses": ["Mathematics", "Physics", "Computer Science"],
#     "address": {
#         "city": "Lagos",
#         "zip_code": "12345",
#     }


# # demo_student2 = {
# #     "unique_id": "STU22222",
# #     "name": "Jane Smith",
# #     "age": 19,
# #     "courses": ["Biology", "Chemistry", "Geography"],
# #     "address": {
# #         "city": "Lagos",
# #         "zip_code": "12890",
# #     }
# # }

# # student_record.append(demo_student)
# # student_record.append(demo_student2) 

def create_student(username, name, age, courses, city, zip_code):
    students_database[username] = {
        "name": name,
        "age": age,
        "courses": set(courses),
        "address": {
            "city": city,
            "zip_code": zip_code,
        }
    }
    
def display_Student(username):
    if username in students_database:
        print(students_database[username])
    else:
        print("Student not found.")

def display_student_courses(username):
    if username in students_database:
        print(students_database[username]["courses"])
    else:
        print("Student not found.")

def display_zip_code(username):
    if username in students_database:
        print(students_database[username]["address"]["zip_code"])
    else:
        print("Student not found.")

def display_city(username):
    if username in students_database:
        print(students_database[username]["address"]["city"])
    else:
        print("Student not found.")

def add_course(username, course):
    if username in students_database:
        if course in courses_list:
            if course not in students_database[username]["courses"]:
                students_database[username]["courses"].append(course)
                print(f"{course} added to {username}'s courses.")
            else:
                print(f"{course} is already in {username}'s courses.")
        else:
            print("Course not found in the available courses list.")
    else:
        print("Student not found.")

def remove_course(username, course):
    if username in students_database:
        if course in students_database[username]["courses"]:
            students_database[username]["courses"].remove(course)
            print(f"{course} removed from {username}'s courses.")
        else:
            print(f"{course} is not in {username}'s courses.")
    else:
        print("Student not found.")

def update_course(username, old_course, new_course):
    if username in students_database:
        if old_course in students_database[username]["courses"]:
            if new_course in courses_list:
                students_database[username]["courses"].remove(old_course)
                students_database[username]["courses"].append(new_course)
                print(f"{old_course} updated to {new_course} in {username}'s courses.")
            else:
                print("New course not found in the available courses list.")
        else:
            print(f"{old_course} is not in {username}'s courses.")
    else:
        print("Student not found.")

def update_student(username, name=None, age=None, city=None, zip_code=None):
    if username in students_database:
        if name:
            students_database[username]["name"] = name
        if age:
            students_database[username]["age"] = age
        if city:
            students_database[username]["address"]["city"] = city
        if zip_code:
            students_database[username]["address"]["zip_code"] = zip_code
        print(f"{username}'s information updated.")
    else:
        print("Student not found.")

def total_students():
    print(f"Total number of students: {len(students_database)}")




