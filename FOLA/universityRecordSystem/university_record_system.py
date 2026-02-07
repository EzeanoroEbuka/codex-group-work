from os import name

university_record = {}

def create_student_record(username, age, city, zip_code):
    student_record = {
        "name": username,
        "age": age,
        "courses": ("Math", "Physics", "Computer Science", "Biology", "Chemistry",
                    "Statistics", "English", "Economics", "History", "Philosophy",
                    "Sociology", "Political Science", "Geography", "Psychology", "Art",
                    "Music", "Engineering", "Law", "Medicine", "Business"),
        "address": {
            "city": city,
            "zip_code": zip_code
        }
    }
    return student_record

name = 'Fola'
university_record[name] = create_student_record(name,21,'lagos',2134)
university_record['Lola'] = create_student_record('Lola',17,'abuja',2774)
print(university_record)
