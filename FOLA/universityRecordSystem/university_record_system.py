university_record = {}

def university_courses():
    courses = ("Math", "Physics", "Computer Science", "Biology", "Chemistry",
                "Statistics", "English", "Economics", "History", "Philosophy",
                "Sociology", "Political Science", "Geography", "Psychology", "Art",
                "Music", "Engineering", "Law", "Medicine", "Business")
    return courses


def create_student_record(username, age, city, zip_code):
    student_record = {
        "name": username,
        "age": age,
        "courses": set(),
        "address": {
            "city": city,
            "zip_code": zip_code
        }
    }
    return student_record

def add_student_to_university_record(username,student_record):
    university_record[username] = student_record

def display_university_courses():
    print('-------------- COURSES ---------------')
    subject_count = 1
    for course in university_courses():
        print(course, end=', ')
        if subject_count % 5 == 0:
            print()
        subject_count += 1
    print()

def display_university_record(student_username):
    print(university_record.get(student_username))

def display_student_offered_courses(student_username):
    print(university_record[student_username].get("courses"))

def display_student_zip_code(student_username):
    print(university_record[student_username]['address'].get("zip_code"))

def display_student_city(student_username):
    print(university_record[student_username]['address'].get("city"))

def add_new_course(student_username, course):
    if course in university_courses() and course not in university_record[student_username]['courses']:
        university_record[student_username]['courses'].update([course])

def remove_course(student_username, course):
    university_record[student_username]['courses'].discard(course)

def update_name_age_city_zip_code(student_username, new_name, age, city, zip_code):
    university_record[student_username]['name'] = new_name
    university_record[student_username]['age'] = age
    university_record[student_username]['address']['city'] = city
    university_record[student_username]['address']['zip_code'] = zip_code

def display_overall_number_of_students():
    return len(university_record)
