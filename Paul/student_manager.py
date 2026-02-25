from department_courses import DEPARTMENT_COURSES
from students_information import students

def create_student():
    username = input("Enter unique username: ")

    if username in students:
        print("Username already exists.")
        return

    name = input("Enter name: ")
    age = int(input("Enter age: "))

    courses_input = input("Enter courses (comma separated): ")

    courses = set()

    course_list = courses_input.split(",")

    for course in course_list:
        clean_course = course.strip()

        if clean_course in DEPARTMENT_COURSES:
            courses.add(clean_course)

    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")

    students[username] = {
        "name": name,
        "age": age,
        "courses": courses,
        "address": {
            "city": city,
            "zip_code": zip_code
        }
    }

    print("Student created successfully.")


def display_student_record(username):
    student = students.get(username)
    if not student:
        print("Student not found.")
        return

    print(f"\nName: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Courses: {', '.join(student['courses'])}")
    print(f"City: {student['address']['city']}")
    print(f"Zip Code: {student['address']['zip_code']}")


def display_student_courses(username):
    student = students.get(username)
    if student:
        print(", ".join(student["courses"]))
    else:
        print("Student not found.")


def display_city(username):
    student = students.get(username)
    if student:
        print(student["address"]["city"])
    else:
        print("Student not found.")


def display_zip_code(username):
    student = students.get(username)
    if student:
        print(student["address"]["zip_code"])
    else:
        print("Student not found.")


def add_course(username, course):
    student = students.get(username)

    if not student:
        print("Student not found.")
        return

    if course not in DEPARTMENT_COURSES:
        print("Course not offered.")
        return

    student["courses"].add(course)
    print("Course added.")


def remove_course(username, course):
    student = students.get(username)
    if student and course in student["courses"]:
        student["courses"].remove(course)
        print("Course removed.")
    else:
        print("Course not found.")


def update_student_info(username, name=None, age=None, city=None, zip_code=None):
    student = students.get(username)

    if not student:
        print("Student not found.")
        return

    if name:
        student["name"] = name
    if age:
        student["age"] = age
    if city:
        student["address"]["city"] = city
    if zip_code:
        student["address"]["zip_code"] = zip_code

    print("Student updated.")


def total_students():
    print(len(students))

