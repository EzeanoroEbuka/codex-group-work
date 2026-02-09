class university_management:
    def __int__(self, name,username, age, courses, city, zip_code):
        self.name=name
        self.username=username
        self.age=age
        self.courses=courses
        self.city=city
        self.zipcode=zip_code
        

        def set_username(self,username):
            self.username=username
        def get_username(self):
            return self.username
        def set_name(self,name):
            self.name=name
        def get_age(self):
            return name
        def get_courses(self):
            return courses
        def set_courses(self,courses):
            self.courses=courses
        def get_city(self):
            return city
        def set_city(self,city):
            self.city=city
        def get_zip_code(self,zipcode):
            return zipcode
        def set_zip_code(self,zipcode):
            self.zip_code=zipcode

    available_courses={"Math", "Physics", "Computer Science", "Biology", "Chemistry",
"Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology", "Art",
"Music", "Engineering", "Law", "Medicine", "Business"}

student_file={}
def addding_students(name,username,age,courses,city,zip_code):
    student_file[username]={
        "name":name,
        "age":age,
        "courses":courses,
        "city":city,
        "zip_code":zip_code
    }

def display_student(username):
    if username  not in student_file:
        return "student not found"
    else:
        return {student_file["name"]}

def add_courses(username, course):
    if courses not in student_file:
        {student_file["courses"]}.append(courses)
        return  {student_file["name"]["age"]["courses"]["city"]["zip_code"]}
    else:
        return "course already exists"
def remove_courses(username):
    if courses in student_file:
        {student_file["courses"]}.pop(courses)
        return {student_file["name"]["age"]["courses"]["city"]["zip_code"]}
    else:
        return "course not found"

def available_courses(username,courses):
    if courses not in available_courses:
        return "courses is not found in available courses"
    else:
        return available_courses[courses]

def display_record(name,username,age,courses,city,zip_code):
    if username not in student_file:
        return "student not found"
    else:
        return
def display_zipcode(username,zip_code):
    if zip_code not in student_file:
        return "zipcode not found in system"
    else:
        return {student_file["zip_code"]}

def student_info(username, name=None, age=None, courses=None, city=None, zip_code=None):
    if username not in student_file:
        if name:
            student_file["name"] = name
        if age:
            student_file["age"] = age
        if city:
            student_file["city"] = city
        if zip_code:
            student_file["zip_code"] = zip_code
        {student_file["courses"]}.append(name)
        {student_file["courses"]}.append(age)
        {student_file["courses"]}.append(city)
        {student_file["courses"]}.append(zip_code)
        return "Student information updated for" + {student['name']}



def total_students(name):
        return len(name)







