
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

def display_all_student_records():
    for key, value in student_details:
        print(key,":",value)


def display_student_records(username):
    return student_details.get(username)

def display_student_courses(username):
    return student_details[username]["courses"]

def display_student_zipcode(username):
    return student_details[username]["zip_code"]







