class University Management:
    def __int__(self, name, age, courses, city, zip_code):
        self.set_name(name)
        self.set_age(age)
        self.set_courses(courses)
        self.set_city(city)
        self.set_zip_code(zip_code)

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

