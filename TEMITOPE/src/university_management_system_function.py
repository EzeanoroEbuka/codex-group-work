COURSES = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
}

students = {}

def create_student_record(username, name, age, courses, city, zip_code):
    students[username] = {
        "name": name,
        "age": age,
        "courses": set(courses),
        "address": {
            "city": city,
            "zip_code": zip_code
        }
    }

def display_student_record(username):
    return students.get(username, "Student not found")

def display_student_courses(username):
    if username in students:
        return students[username]["courses"]
    else:
        return "Student not found"

def display_student_zip_code(username):
    if username in students:
        return students[username]["address"]["zip_code"]
    else:
        return "Student not found"

def display_student_city(username):
    if username in students:
        return students[username]["address"]["city"]
    else:
        return "Student not found"

def add_course(username, course):
    if username not in students:
        return "Student not found"
    if course not in COURSES:
        return "Course not found"
    if course in students[username]["courses"]:
        return "Course already exists"
    students[username]["courses"].add(course)
    return "Course added successfully"

def remove_course(username, course):
    if username not in students:
        return "Student not found"
    students[username]["courses"].discard(course)
    return "Course removed successfully"

def update_student_record(username, name, age, city, zip_code):
    if username not in students:
        return "Student not found"
    else:
        students[username]["name"] = name
        students[username]["age"] = age
        students[username]["address"]["city"] = city
        students[username]["address"]["zip_code"] = zip_code
        return "Student updated successfully"

def overall_number_of_students():
    return len(students)