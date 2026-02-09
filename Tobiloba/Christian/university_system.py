
OFFICIAL_COURSES = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
}
students= {}

def create_student(student_id,name,age,courses,city,zip_code):
    students[student_id] = {
        "name": name,
        "age": age,
        "courses": courses,
        address: {
            "city": city,
            "zip_code": zip_code
        }
    }
def get_student(student_id):
    return students.get(student_id, "Student not found")

def display_courses(student_id):
    student = get_student(student_id)
    if student != "Student not found":
        return student["courses"]
    return student

def update_courses(student_id, new_courses):
    student = get_student(student_id)
    if student != "Student not found":
        valid_courses = [course for course in new_courses if course in OFFICIAL_COURSES]
        student["courses"] = valid_courses
        return f"Courses updated for {student['name']}"
    return student

def display_city(student_id):
    student = get_student(student_id)
    if student != "Student not found":
        return student["address"]["city"]
    return student

def display_zip_code(student_id):
    student = get_student(student_id)
    if student != "Student not found":
        return student["address"]["zip_code"]
    return student

def remove_course(student_id, course):
    student = get_student(student_id)
    if student != "Student not found":
        if course in student["courses"]:
            student["courses"].remove(course)
            return f"{course} removed from {student['name']}'s courses"
        return f"{course} not found in {student['name']}'s courses"
    return student

def update_course(student_id, old_course, new_course):
    student = get_student(student_id)
    if student != "Student not found":
        if old_course in student["courses"]:
            if new_course in OFFICIAL_COURSES:
                index = student["courses"].index(old_course)
                student["courses"][index] = new_course
                return f"{old_course} updated to {new_course} for {student['name']}"
            return f"{new_course} is not an official course"
        return f"{old_course} not found in {student['name']}'s courses"
    return student

def update_student_info(student_id, name=None, age=None, city=None, zip_code=None):
    student = get_student(student_id)
    if student != "Student not found":
        if name:
            student["name"] = name
        if age:
            student["age"] = age
        if city:
            student["address"]["city"] = city
        if zip_code:
            student["address"]["zip_code"] = zip_code
        return f"Student information updated for {student['name']}"
    return student

def total_students():
    return len(students)