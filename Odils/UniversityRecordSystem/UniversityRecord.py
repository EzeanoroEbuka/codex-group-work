
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
