COURSE_LIST = {"Math", "Physics", "Computer Science", "Biology", "Chemistry",
"Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art",
"Music", "Engineering", "Law", "Medicine", "Business"}

all_student_records = {}

def create_student(username, name, age, student_course, city, zip_code):
    all_student_records[username] = {"name": name, "age": age, "courses": [student_course],
        "address": { "city": city, "zip_code": zip_code}
    }
    return all_student_records

def get_student_records(username):
    if username in all_student_records:
        return username, all_student_records[username]
    return None

def get_student_courses(username):
    if username in all_student_records:
        return username, all_student_records[username]["courses"]
    return None




def get_student_zip_codes(username):
    if username in all_student_records:
        return username, all_student_records [username]["address"]["zip_codes"]
    return None

def get_student_city(username):
    if username in all_student_records:
        return username, all_student_records[username]["address"]["city"]
    return None

def add_course_for_student(username, course):
    if course not in COURSE_LIST:
        return "course not found"
    if username in all_student_records:
        all_student_records[username]["courses"].append(course)
        return all_student_records[username]["courses"]
    return None

def update_course_for_student(username, course):
    user_choice = int(input("Enter 1 to update course or 2 to remove course: "))
    if user_choice == 1:
        if course not in COURSE_LIST:
            return"course not found"
        if username not in all_student_records:
            return"username not found"
        all_student_records[username]["courses"].append(course)
        return all_student_records[username]["courses"]
    if user_choice == 2:
        if course not in COURSE_LIST:
            return"course not found"
        if username not in all_student_records:
            return "username not found"
        if course in all_student_records[username]["courses"]:
            all_student_records[username]["courses"].remove(course)
            return all_student_records[username]["courses"]
        return "course not found in student list"
    return None

def update_student_info(username, key, update_value):
    if username in all_student_records:
        if key == "name":
            all_student_records[username]["name"] = update_value
        elif key == "city":
            all_student_records[username]["address"]["city"] = update_value
        elif key == "zip_code":
            all_student_records[username]["address"]["zip_code"] = update_value
        elif key == "age":
            all_student_records[username]["age"] = update_value

def get_all_student_records():
    return all_student_records

