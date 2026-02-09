class UniversityRecord:

    university_records = {}

    def create_student_profile(self,  name, username, age, courses, address, zipcode, city):
        student_record = {
            "name" : name,
            "username" : username,
            "age" : age,
            "courses" : courses,
            "address" : {
                "city" : city,
                "zipcode" : zipcode,
            }
        }


        return student_record


    def department_courses(self):
        COURSES = (
            "Math", "Physics", "Computer Science", "Biology", "Chemistry",
        "Statistics", "English", "Economics", "History", "Philosophy",
        "Sociology", "Political Science", "Geography", "Psychology", "Art",
        "Music", "Engineering", "Law", "Medicine", "Business"
        )

        return COURSES

    def display_student_record(self, username, student_record):
        self.university_records[username] = student_record


    def display_only_the_courses_that_a_student_offer(self, username):
        courses = self.university_records[username].get("courses")

    def display_only_the_zip_code_from_student_address(self, username):
        zip_code = self.university_records[username].get("zipcode")

    def dispay_only_the_city_from_student_address(self, username):
        city = self.university_records[username].get("city")


    def add_new_course_to_student_record(self, username, student_record, new_course):
        for key, value in student_record.keys():
            if value == new_course:
                print("Course already exists")
            else:
                self.university_records[username].append({key: value})







