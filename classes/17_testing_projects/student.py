
class Student:
    ''' A Student is a person currently enrolled in this awesome course. '''

    def __init__(self, name, sid):
        ''' return a Student object, with a name, id, and fresh grades '''
        self.name = name
        self.student_id = sid
        self.hw_grades = [0.0] * 10
        self.test_grades = [0.0, 0.0]

    def set_hw_grade(self, grade, week):
        ''' Set the grade for a specific homework '''
        self.hw_grades[week] = grade

    def set_test_grade(self, grade, exam):
        ''' Set the grade for a specific test '''
        self.test_grades[exam] = grade

    def calculate_grade(self):
        ''' Return the current grade of the student.
            Tests and homeworks are each worth 50%.
        '''
        average_hw_grade = sum(self.hw_grades) / len(self.hw_grades)
        average_test_grade = sum(self.test_grades) / len(self.test_grades)
        final_grade = (average_hw_grade + average_test_grade) / 2.0

        return final_grade

    @staticmethod
    def letter_grade(percent_grade):
        ''' return a letter grade from a percentage grade '''
        if percent_grade >= 90.0:
            return 'A'
        elif percent_grade >= 80.0:
            return 'B'
        elif percent_grade >= 70.0:
            return 'C'
        elif percent_grade >= 60.0:
            return 'D'
        else:
            return 'F'
