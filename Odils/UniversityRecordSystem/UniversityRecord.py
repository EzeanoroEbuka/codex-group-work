
class UniversityRecord:
    def create_student_profile(self, name, age, courses, address, zipcode, city):
        student_profile = {
            "name" : name,
            "age" : age,
            "courses" : courses,
            "address" : {
                "city" : city,
                "zipcode" : zipcode,
            }
        }

        return student_profile


    def department_courses(self):
        COURSES = (
            "Math", "Physics", "Computer Science", "Biology", "Chemistry",
        "Statistics", "English", "Economics", "History", "Philosophy",
        "Sociology", "Political Science", "Geography", "Psychology", "Art",
        "Music", "Engineering", "Law", "Medicine", "Business"
        )

        return COURSES



