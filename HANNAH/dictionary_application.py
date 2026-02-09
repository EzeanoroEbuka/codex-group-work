students = {}
allowed_courses = {'Math', 'Physics', 'Computer Science', 'Biology', 'Chemistry',
                   'Statistics', 'English', 'Economics',"History", "Philosophy",
                   "Sociology", "Political Science", "Geography", "Psychology",
                   "Art","Music", "Engineering", "Law", "Medicine", "Business"}
def student_record():
    user_name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    zip_code = int(input("Please enter your zip code: "))
    city = input("Please enter your city: ")

course =  []
course_record = int(input("Please enter the amount of course you want to enter: "))
for number in range(course_record):
    courses = input("Please enter the course: ")
    course.add(courses)
student_record()
