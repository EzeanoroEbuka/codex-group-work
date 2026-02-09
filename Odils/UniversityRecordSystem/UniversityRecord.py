class UniversityRecord:
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

    def display_student_record(self, username):


