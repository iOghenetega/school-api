from db import db
from datetime import datetime


class EnrollmentModel(db.Model):
    _tablename_ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'courses.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'students.id'), nullable=False)
    grades = db.Column(db.String(255))
    grade_points = db.Column(db.Float)

    def calculate_grade_points(self):
        # Helper function to convert the grades string to a numerical value
        # We assume that the grades are in the format "A, B+, C-, F, etc."
        grade_map = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                     'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0,
                     'F': 0.0}
        grade_tokens = self.grades.split(',')
        grade_values = [grade_map[token.strip()] for token in grade_tokens]
        grade_points = sum(grade_values) / len(grade_values)
        self.grade_points = grade_points

