
university_record = []
available_courses = {"Math", "Physics", "Computer Science", "Biology", "Chemistry",
                    "Statistics", "English", "Economics", "History", "Philosophy",
                    "Sociology", "Political Science", "Geography", "Psychology", "Art",
                    "Music", "Engineering", "Law", "Medicine", "Business"}

def create_student(student_name, student_age, student_id, city, zip_code):
    student = {
        "Unique_user_ID": "student_id",
        "student_info": {
            "Name": "student_name",
            "Age": "student_age",
            "Courses": set(),
            "Department": "COMPUTER SCIENCE",
            "Address": {
                "City": "city",
                "Zip_code": "zip_code",
            },
        }
    }
    university_record.append(student)

def course_available(course):
    if course in available_courses:
        return True
    return "Course is not available in department"


def get_student_by_id(student_id):
    for student in university_record:
        if student["Unique_user_ID"]== student_id:
            return student
    return None


def get_student_by_name(student_name):
    for student in university_record:
        if student["student_info"]["Student_Name"] == student_name:
            return student
    return None

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



student_info ={
    "Unique_user_ID": "id",
    "student_info" :  {
             "Name": "kay",
             "Age": 20,
             "Courses": set(),
             "Department": "COMPUTER SCIENCE",
             "Address": {
                 "City": "LAGOS STATE",
                 "Zip_code": "55050",
             },
         }
     }


university_record.append(student_info)
#
#
#
update_student_name("id","Ayobami")
update_student_age("id",90)
print(add_student_courses("id","nglish"))
print(add_student_courses("id","English"))

# print(delete_student_course("id","yoruba"))

# print(course_available("Math"))

