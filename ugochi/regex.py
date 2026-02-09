
john_address = {
    "city": "New York",
    "zip_code": "10001"
}


john_paul = {
    "name": "John Paul",
    "age": 22,
    "courses": {"Math", "Physics", "Computer Science"},
    "address": john_address
}


sarah_address = {
    "city": "Boston",
    "zip_code": "02108"
}

sarah_lee = {
    "name": "Sarah Lee",
    "age": 20,
    "courses": {"History", "Math", "Art"},
    "address": sarah_address
}

student_database = [john_paul, sarah_lee]


print("Successfully added", len(student_database), "students to the system.")


available_courses = (
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
)






