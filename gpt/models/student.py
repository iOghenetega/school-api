from db import db
from datetime import datetime
from models import enrollment, EnrollmentModel



class StudentModel(db.Model):
    _tablename_ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @property
    def gpa(self):
        # Calculate the student's GPA based on their grades in each course
        # We assume that each enrollment has a grade_points field
        enrollments = enrollment.query.filter_by(student_id=self.id).all()
        if len(enrollments) == 0:
            return None
        total_points = sum(
            [enrollment.grade_points for enrollment in enrollments])
        gpa = total_points
        return gpa / len(enrollments)
