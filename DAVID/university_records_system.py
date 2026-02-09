
course_list = {"Math", "Physics", "Computer Science", "Biology", "Chemistry","Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art","Music", "Engineering", "Law", "Medicine", "Business"}

# student_record = []
student_details = {}
def creating_students(name, age,city,zip_code,username,courses ):

    student_details [username]={
        "name":name,
        "age":age,
        "courses":courses,
        "student_address": {"city": city, "address": zip_code,}
    }

    # student ={
    #     username: student_details
    # }
    # student_record.append(student)
    #




def display_student_records(username):
        student = student_details.get(username)
        if student is None:
            return "Student not found"
        return student


def display_student_courses(username):
    courses = student_details[username].get("courses")
    if courses is None:
        return "Course not found"
    return student_details[username]["courses"]


def display_student_zipcode(username):
    if username in student_details:
        return student_details[username]["student_address"]["zip_code"]
    return "Student Zip-code not found"


def display_student_city(username):
    if username in student_details:
        return student_details[username]["student_address"]["city"]
    return "Student not found"



def display_the_number_of_all_students():
    return len(student_details)






