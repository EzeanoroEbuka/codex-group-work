
university_record = []
available_courses = {"Math", "Physics", "Computer Science", "Biology", "Chemistry",
                    "Statistics", "English", "Economics", "History", "Philosophy",
                    "Sociology", "Political Science", "Geography", "Psychology", "Art",
                    "Music", "Engineering", "Law", "Medicine", "Business"}


demo_student1 = {
            "Unique_user_ID": "id1",   # FIXED ID
            "student_info": {
                "Name": "Samuel",
                "Age": 20,
                "Courses": set(),
                "Department": "COMPUTER SCIENCE",
                "Address": {
                    "City": "Lagos",
                    "Zip_code": "202022",
                },
            }
        }

demo_student = {
            "Unique_user_ID": "id2",   # FIXED ID
            "student_info": {
                "Name": "Samuel",
                "Age": 20,
                "Courses": {"Music", "Engineering", "Law", "Medicine", "Business"},
                "Department": "COMPUTER SCIENCE",
                "Address": {
                    "City": "Lagos",
                    "Zip_code": "202022",
                },
            }
        }

university_record.append(demo_student)
university_record.append(demo_student1)
def create_student(student_name, student_age, student_id, city, zip_code):
    if id_exists(student_id): return "Id already exists"
    student = {
        "Unique_user_ID": student_id,
        "student_info": {
            "Name": student_name,
            "Age": student_age,
            "Courses": set(),
            "Department": "COMPUTER SCIENCE",
            "Address": {
                "City": city,
                "Zip_code": zip_code,
            },
        }
    }
    university_record.append(student)
    return "student created successfully"

def id_exists(student_id):
    for students in university_record:
        return students["Unique_user_ID"] == student_id
    return False


def course_available(course):
    if course in available_courses:
        return True
    return "Course is not available in department"


def get_student_by_id(student_id):
    for student in university_record:
        if student.get("Unique_user_ID")== student_id:
            return student
    return None


def get_student_by_name(student_name):
    for student in university_record:
        if student["student_info"]["Student_Name"] == student_name:
            return student
    return None

def get_student_zip_code(student_id):
    return get_student_by_id(student_id)["student_info"]["Address"].get("Zip_code")

def get_student_courses(student_id):
    return get_student_by_id(student_id)["student_info"].get("Courses")

def update_student_name(student_id, student_new_name):
    get_student_by_id(student_id)["student_info"]["Name"] = student_new_name

def update_student_age(student_id, student_new_age):
    get_student_by_id(student_id)["student_info"]["Age"] = student_new_age

def update_student_city(student_id, student_new_city):
    get_student_by_id(student_id)["student_info"]["Address"]["City"] = student_new_city

def update_student_zip_code(student_id, student_new_zip_code):
    get_student_by_id(student_id)["student_info"]["Address"]["Zip_code"] = student_new_zip_code

def add_student_courses(student_id, student_new_course):
    if check_student_has_course(student_id, student_new_course):
        return "course already exists"
    elif course_available(student_new_course) == True:
        student_courses = get_student_by_id(student_id)["student_info"].get("Courses")
        student_courses.add(student_new_course)
        return "course added successfully"
    return "course not available for student department"

def update_student_course(student_id, old_course, student_new_course):
    if check_student_has_course(student_id, old_course) and course_available(student_new_course):
        student_courses = get_student_by_id(student_id)["student_info"].get("Courses")
        student_courses.remove(old_course)
        student_courses.add(student_new_course)
        return "course updated successfully"
    return "old course not found"

def delete_student_course(student_id, course):
    if check_student_has_course(student_id, course):
        student_courses = get_student_by_id(student_id)["student_info"].get("Courses")
        student_courses.remove(course)
        return "course removed successfully"
    return "course not found"

def check_student_has_course(student_id, course):
    student_courses = get_student_by_id(student_id)["student_info"].get("Courses")
    return course in student_courses


def get_student_info(student_id):
    student_info = get_student_by_id(student_id)
    return f"""
Student ID:  {student_id:>2}   
NAME:  {student_info["student_info"]["Name"]:>12}
AGE:  {student_info["student_info"]['Age']:>9}
COURSES:  \t{student_info["student_info"]['Courses']}
DEPARTMENT:  {student_info["student_info"]['Department']:>7}
CITY: {student_info["student_info"]['Address']['City']:>12}
ZIP_CODE: {student_info["student_info"]['Address']['Zip_code']:>9}
"""

