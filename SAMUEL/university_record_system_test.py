import unittest
import SAMUEL.student_and_university_services as student_module


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
        student_module.update_student_name("id1", "Sam")
        self.assertEqual(
            student_module.get_student_by_id("id1")["student_info"]["Name"],
            "Sam"
        )

    def test_update_student_age_changes_age(self):
        student_module.update_student_age("id1", 21)
        self.assertEqual(
            student_module.get_student_by_id("id1")["student_info"]["Age"],
            21
        )

    def test_update_student_city_changes_city(self):
        student_module.update_student_city("id1", "Ibadan")
        self.assertEqual(
            student_module.get_student_by_id("id1")["student_info"]["Address"]["City"],
            "Ibadan"
        )

    def test_update_student_zip_code_changes_zip_code(self):
        student_module.update_student_zip_code("id1", "111111")
        self.assertEqual(
            student_module.get_student_by_id("id1")["student_info"]["Address"]["Zip_code"],
            "111111"
        )

    def test_add_course_successfully(self):
        result = student_module.add_student_courses("id1", "Math")
        self.assertEqual(result, "course added successfully")
        self.assertIn("Math", student_module.get_student_courses("id1"))

    def test_add_existing_course_returns_error(self):
        student_module.add_student_courses("id1", "Math")
        result = student_module.add_student_courses("id1", "Math")
        self.assertEqual(result, "course already exists")

    def test_add_unavailable_course_returns_error(self):
        result = student_module.add_student_courses("id1", "Dancing")
        self.assertEqual(result, "course not available for student department")

    def test_update_course_successfully(self):
        student_module.add_student_courses("id1", "Math")
        result = student_module.update_student_course("id1", "Math", "Physics")
        self.assertEqual(result, "course updated successfully")
        self.assertIn("Physics", student_module.get_student_courses("id1"))

    def test_update_non_existing_course_returns_error(self):
        result = student_module.update_student_course("id1", "Chemistry", "Physics")
        self.assertEqual(result, "old course not found")

    def test_delete_course_successfully(self):
        student_module.add_student_courses("id1", "Math")
        result = student_module.delete_student_course("id1", "Math")
        self.assertEqual(result, "course removed successfully")
        self.assertNotIn("Math", student_module.get_student_courses("id1"))

    def test_delete_non_existing_course_returns_error(self):
        result = student_module.delete_student_course("id1", "Biology")
        self.assertEqual(result, "course not found")


    def test_check_student_has_course_returns_true(self):
        student_module.add_student_courses("id1", "Math")
        self.assertTrue(student_module.check_student_has_course("id1", "Math"))

    def test_check_student_has_course_returns_false(self):
        self.assertFalse(student_module.check_student_has_course("id1", "Physics"))


if __name__ == "__main__":
    unittest.main()
