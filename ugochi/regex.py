
COURSES = (
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
)

name = ""
age = ""
username = ""
city = ""
zip_code = ""
courses = " "

def creatingstudent():
    username = input("Enter unique username: ")
    name = input("Enter Full Name: ")
    age = int(input("Enter Age: "))
    city = input("Enter City: ")
    zip_code = input("Enter Zip Code: ")
    print(f"Available Courses: {COURSES}")
    courses = (input("input courses you want to offer"))
   



def full_record(username):
    pupil = students.get(username)
    if pupil:
        print(f"{students[username],[name],[age],[city],[zip_code],[courses]")

def student_courses(username):
    student = students.get(username)
    if student:
        print(f"Courses for {username}: {students['courses']}")

def zip_code(username):
    student = students.get(username)
    if student:
        print(f"Zip Code: {students['address']['zip']}")

def city(username):
    student = students.get(username)
    if student:
        print(f"City: {students['address']['city']}")



 
students = {}
  
students[username] = {
    "name": name,
    "age": age,
    "courses": courses,
    "address": {"city": city, "zip": zip_code}
    }
print(f"Record created for {username}")


creatingstudent()
user = input("Enter username to view: ")
full_record(user)
city(user)

