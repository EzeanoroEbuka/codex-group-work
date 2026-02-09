import unittest

from FOLA.universityRecordSystem import university_record_system


class MyTestCase(unittest.TestCase):
    def test_toCreateStudentRecord(self):
        university_record_system.create_student_record('Fola',21,'lagos',2134)

if __name__ == '__main__':
    unittest.main()
