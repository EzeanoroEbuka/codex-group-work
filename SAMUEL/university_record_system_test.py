import unittest
import SAMUEL.student_handler as student_module
from SAMUEL.student_handler import *


class TestStudentManagement(unittest.TestCase):

    def setUp(self):

        student_module.university_record.clear()

        demo_student = {
            "Unique_user_ID": "id1",   # FIXED ID
            "student_info": {
                "Name": "Samuel",
                "Age": 20,
                "Courses": set(),
                "Department": "COMPUTER SCIENCE",
                "Address": {
                    "City": "Lagos",
                    "Zip_code": "202022",
                },
            }
        }

        student_module.university_record.append(demo_student)


    def test_update_student_name_changes_name(self):
        update_student_name("id1", "Sam")
        self.assertEqual(
            get_student_by_id("id1")["student_info"]["Name"],
            "Sam"
        )

    def test_update_student_age_changes_age(self):
        update_student_age("id1", 21)
        self.assertEqual(
            get_student_by_id("id1")["student_info"]["Age"],
            21
        )

    def test_update_student_city_changes_city(self):
        update_student_city("id1", "Ibadan")
        self.assertEqual(
            get_student_by_id("id1")["student_info"]["Address"]["City"],
            "Ibadan"
        )

    def test_update_student_zip_code_changes_zip_code(self):
        update_student_zip_code("id1", "111111")
        self.assertEqual(
            get_student_by_id("id1")["student_info"]["Address"]["Zip_code"],
            "111111"
        )

    def test_add_course_successfully(self):
        result = add_student_courses("id1", "Math")
        self.assertEqual(result, "course added successfully")
        self.assertIn("Math", get_student_courses("id1"))

    def test_add_existing_course_returns_error(self):
        add_student_courses("id1", "Math")
        result = add_student_courses("id1", "Math")
        self.assertEqual(result, "course already exists")

    def test_add_unavailable_course_returns_error(self):
        result = add_student_courses("id1", "Dancing")
        self.assertEqual(result, "course not available for student department")

    def test_update_course_successfully(self):
        add_student_courses("id1", "Math")
        result = update_student_course("id1", "Math", "Physics")
        self.assertEqual(result, "course updated successfully")
        self.assertIn("Physics", get_student_courses("id1"))

    def test_update_non_existing_course_returns_error(self):
        result = update_student_course("id1", "Chemistry", "Physics")
        self.assertEqual(result, "old course not found")

    def test_delete_course_successfully(self):
        add_student_courses("id1", "Math")
        result = delete_student_course("id1", "Math")
        self.assertEqual(result, "course removed successfully")
        self.assertNotIn("Math", get_student_courses("id1"))

    def test_delete_non_existing_course_returns_error(self):
        result = delete_student_course("id1", "Biology")
        self.assertEqual(result, "course not found")


    def test_check_student_has_course_returns_true(self):
        add_student_courses("id1", "Math")
        self.assertTrue(check_student_has_course("id1", "Math"))

    def test_check_student_has_course_returns_false(self):
        self.assertFalse(check_student_has_course("id1", "Physics"))


if __name__ == "__main__":
    unittest.main()
