
course_list = {"Math", "Physics", "Computer Science", "Biology", "Chemistry","Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art","Music", "Engineering", "Law", "Medicine", "Business"}

# student_record = []
student_details = {}

def creating_students(name, age,city,zip_code,username,courses ):

    student_details [username]={
        "name":name,
        "age":age,
        "courses":set(courses),
        "student_address": {"city": city, "zip_code": zip_code,}
    }


def display_student_records(username):
        student = student_details.get(username)
        if student is None:
            return "Student not found"
        return student


def display_student_courses(username):
    student = student_details.get(username)
    if student is None:
        return "Student not found"

    courses = student_details[username].get("courses")
    if courses is None:
        return "Course not found"
    return courses


def display_student_zipcode(username):
    if username in student_details:
        return student_details[username]["student_address"]["zip_code"]
    return "Student  not found"


def display_student_city(username):
    if username in student_details:
        return student_details[username]["student_address"]["city"]
    return "Student not found"



def display_the_number_of_all_students():
    return len(student_details)



def adding_new_course_to_record(username, course):

    if username in student_details:
        if course not in course_list:
            return "Invalid course"
        elif course not in student_details[username]["courses"]:
            student_details[username]["courses"].add(course)
            return f"{course} Successfully added"
        else:
            return "Course already added"
    else:
        return "Student not found"



def update_student_course(username, existing_course, new_course):
    if username in student_details:
        if new_course not in course_list:
            return "Course is not part of the allocated courses"
        elif existing_course in student_details[username]["courses"]:
            student_details[username]["courses"].remove(existing_course)
            student_details[username]["courses"].add(new_course)
            return f"{new_course} Successfully added and {existing_course} removed."

        else:
            return "You are not offering this course"
    else:
        return "Student not found"


def remove_student_course(username, course):
    if username in student_details:
        if course in student_details[username]["courses"]:
            student_details[username]["courses"].remove(course)
            return f"{course} Has been Successfully Removed from the courses you are offering."

        else:
            return "You are not offering this course"
    else:
        return "Student not found"


def update_student_data(username,key, new_value):
    if username in student_details:
        if key == "age":
            student_details[username]["age"] = new_value
        elif key == "name":
            student_details[username]["name"] = new_value
        elif key == "city":
            student_details[username]["student_address"]["city"] = new_value
        elif key == "zip_code":
            student_details[username]["student_address"]["zip_code"] = new_value
        else:
            return f"Enter a valid detail to update"

        return f" {key} Has been updated successfully"
    else:
        return f"Student not found"



