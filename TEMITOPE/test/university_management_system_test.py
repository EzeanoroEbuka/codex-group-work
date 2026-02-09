import unittest
from university_management_system_function import *


class TestUniversityManagementSystem(unittest.TestCase):

    def setUp(self):
        students.clear()

    def test_that_student_record_is_empty(self):
        self.assertEqual(overall_number_of_students(), 0)

    def test_that_create_student_record_creates_record(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        self.assertEqual(overall_number_of_students(), 1)

    def test_that_display_student_record_displays_record(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        record = display_student_record("Darkwolf")
        self.assertEqual(type(record), dict)

    def test_that_display_student_courses_display_courses(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        self.assertSetEqual(display_student_courses("Darkwolf"), {"Math", "Physics"})

    def test_that_add_course_adds_a_new_course(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        self.assertEqual(add_course("Darkwolf", "English"), "Course added successfully")

    def test_that_add_course_does_not_add_an_existing_course(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        self.assertEqual(add_course("Darkwolf", "Math"), "Course already exists")

    def test_that_add_course_does_not_add_invalid_course(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        self.assertEqual(add_course("Darkwolf", "Literature"), "Course not found")

    def test_that_remove_course_removes_a_course(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        self.assertEqual(remove_course("Darkwolf", "Math"), "Course removed successfully")

    def test_that_update_student_record_updates_record(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        result = update_student_record(
            "Darkwolf", "Ifeoluwa Adekoje", 20, "Abuja", "02101"
        )

        self.assertEqual(result, "Student updated successfully")

    def test_overall_number_of_students(self):
        self.assertEqual(overall_number_of_students(), 0)

        create_student_record(
            username = "Darkwolf",
            name = "Ifeoluwa Adekoje",
            age = 20,
            courses = ["Math", "Physics"],
            city = "Lagos",
            zip_code = "12345"
        )

        create_student_record(
            username="Smartwolf",
            name="Ayooluwa Adekoje",
            age=20,
            courses=["English", "Economics"],
            city="Abuja",
            zip_code="54321"
        )

        self.assertEqual(overall_number_of_students(), 2)