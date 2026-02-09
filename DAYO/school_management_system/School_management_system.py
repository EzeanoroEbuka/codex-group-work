COURSE_LIST = {"Math", "Physics", "Computer Science", "Biology", "Chemistry",
"Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art",
"Music", "Engineering", "Law", "Medicine", "Business"}

all_student_records = {}

def create_student(username, name, age, student_course, city, zip_code):
    all_student_records[username] = {"name": name, "age": age, "courses": student_course,
        "address": { "city": city, "zip_code": zip_code}
    }
    return all_student_records

def get_student_records(username):
    if username in all_student_records:
        return username, all_student_records[username]
    return None

def get_student_courses(username):
    if username in all_student_records:
        return username, all_student_records["courses"]
    return None

def get_student_zip_codes(username):
    if username in all_student_records:
        return username, all_student_records ["address"]["zip_codes"]
    return None

def get_student_city(username):
    if username in all_student_records:
        return username, all_student_records["address"]["city"]
    return None

def add_course_for_student(username, course, student_records):
    if username in all_student_records: