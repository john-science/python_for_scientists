import unittest

from gradebook.student import Student


class TestStudent(unittest.TestCase):
    def test_no_grades(self):
        """Test that the constructor works, and that calculate_grade works when there are no grades."""
        charles = Student("Charlie Brown", 12345)
        self.assertEqual(charles.calculate_grade(), 0.0)

    def test_perfect_grades(self):
        """Test that this works for students with perfect grades."""
        emmy = Student("Emmy Noether", 14152)

        # set all of the grades to perfect
        emmy.set_test_grade(100.0, 0)
        emmy.set_test_grade(100.0, 1)
        for i in range(10):
            emmy.set_hw_grade(100.0, i)

        self.assertEqual(emmy.calculate_grade(), 100.0)

    def test_better_than_perfect_grades(self):
        """Test that this works for students with extra credit."""
        emmy = Student("Emmy Noether", 14152)

        # set all of the grades to perfect
        emmy.set_test_grade(100.0, 0)
        emmy.set_test_grade(110.0, 1)
        for i in range(10):
            emmy.set_hw_grade(100.0, i)

        final_grade = emmy.calculate_grade()
        self.assertEqual(final_grade, 102.5)
        self.assertEqual(Student.letter_grade(final_grade), "A")
