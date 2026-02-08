import unittest

from SAMUEL.student import *


class TestStudentManagement(unittest.TestCase):

    def setUp(self):

        university_record = []
        demo_student = {
            "Unique_user_ID": "id",
            "student_info": {
                "Name": "Samuel",
                "Age": "20",
                "Courses": {"Mathematic", "English", "Yoruba"},
                "Department": "COMPUTER SCIENCE",
                "Address": {
                    "City": "Lagos",
                    "Zip_code": "202022",
                },
            }
        }
        university_record.append(demo_student)

    def test_create_student(self):
        student_info = create_student("Alice", 22, "id2", "Abuja", "100001")
        university_record.append(student_info)
        student = get_student_by_id("id2")
        self.assertIsNotNone(student)
        self.assertEqual(student["student_info"]["Name"], "Alice")
        self.assertEqual(student["student_info"]["Age"], 22)
        self.assertEqual(student["student_info"]["Address"]["City"], "Abuja")

    def test_get_student_by_id_and_name(self):
        student = get_student_by_id("id")
        self.assertEqual(student["student_info"]["Name"], "Samuel")


    def test_update_student_info(self):
        update_student_name("id", "Sam")
        update_student_age("id", 21)
        update_student_city("id", "Ibadan")
        update_student_zip_code("id", "101010")
        student = get_student_by_id("id")
        self.assertEqual(student["student_info"]["Name"], "Sam")
        self.assertEqual(student["student_info"]["Age"], 21)
        self.assertEqual(student["student_info"]["Address"]["City"], "Ibadan")
        self.assertEqual(student["student_info"]["Address"]["Zip_code"], "101010")

    def test_courses_management(self):
        result = add_student_courses("id", "Math")
        self.assertEqual(result, "course added successfully")
        self.assertIn("Math", get_student_courses("id"))

        result = add_student_courses("id", "Math")
        self.assertEqual(result, "course already exists")

        result = add_student_courses("id", "Dance")
        self.assertEqual(result, "course not available for student department")

        result = update_student_course("id", "Yoruba", "Physics")
        self.assertEqual(result, "course updated successfully")
        self.assertIn("Physics", get_student_courses("id"))
        self.assertNotIn("Yoruba", get_student_courses("id"))


        result = delete_student_course("id", "Physics")
        self.assertEqual(result, "course removed successfully")
        self.assertNotIn("Physics", get_student_courses("id"))


        result = delete_student_course("id", "Dance")
        self.assertEqual(result, "course not found")

    def test_check_student_has_course(self):
        self.assertTrue(check_student_has_course("id", "English"))
        self.assertFalse(check_student_has_course("id", "Math"))

    def test_course_available(self):
        self.assertTrue(course_available("Math"))
        self.assertEqual(course_available("Dance"), "Course is not available in department")


if __name__ == "__main__":
    unittest.main()
