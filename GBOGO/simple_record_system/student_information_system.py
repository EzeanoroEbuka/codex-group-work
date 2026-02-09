from typing import Any

department=[]
fixed_courses=("Math", "Physics", "Computer Science", "Biology", "Chemistry",
"Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art",
"Music", "Engineering", "Law", "Medicine", "Business")

def collect_student_information(username:str,name:str,age:int,student_courses:set[str],address:dict)-> list[Any]:
    department.append({
        "id":username,
        "record" :{
        "username":username,
        "name":name,
        "age":age,
        "courses":student_courses,
        "address":address
    }
    })
    return department

def register_courses(name:str,course_wanted:set[str])-> Any | None:
    if course_wanted in fixed_courses:
        for student in department:
            if student["record"]["name"] == name:
                student["record"]["courses"].add(course_wanted)
                return student["record"]["courses"]
    return None

def display_student_records()-> dict | None:
    for student in department:
        return student
    return None

def display_course_for_student(student_id:str)->set[str] | None:
    for student in department:
        if student["id"] == student_id:
            return student["record"]["courses"]
    return None

def display_zipcode_from_students_address(student_id:str)->str | None:
    for student in department:
        if student["id"] == student_id:
            return student["record"]["address"]["zip"]
    return None

def display_city_from_students_address(student_id:str)->str | None:
    for student in department:
        if student["id"] == student_id:
            return student["record"]["address"]["city"]
    return None

def add_new_course(student_id:str,course)->set[str] | None:
    for student in department:
        if student["id"] == student_id:
            if course not in student["record"]["courses"] and course in fixed_courses:
                student["record"]["courses"].append(course)
                return student["record"]["courses"]
    return None

def remove_or_update_student_course(student_id:str,operation:str,course)-> None:
    for student in department:
        if student["id"] == student_id:
            if course in student["record"]["courses"]:
                if operation == "remove":
                    student["record"]["courses"].remove(course)
                elif operation == "update":
                    student["record"]["courses"].remove(course)
                    student["record"]["courses"].add(course)

# def update_age_field(student_id:str,operation:str)->None:
#     for student in department: