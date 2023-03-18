from flask.views import MethodView
from flask_smorest import Blueprint,abort #
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import db
from schemas import StudentSchema, CourseSchema, EnrollmentSchema
from sqlalchemy.exc import SQLAlchemyError
from models import student



StudentBlueprint =  Blueprint("student", __name__, description="Operations on students")

@StudentBlueprint.route('/students')
class StudentsView(MethodView):
    @StudentBlueprint.response(StudentSchema(many=True))
    @jwt_required()
    def get(self):
        """Get all students"""
        students = student.query.all()
        return students

    @StudentBlueprint.arguments(StudentSchema)
    @StudentBlueprint.response(StudentSchema)
    @jwt_required()
    def post(self, student):
        """Create a new student"""
        db.session.add(student)
        db.session.commit()
        return student


@StudentBlueprint.route('/students/int:id')
class StudentView(MethodView):
    @StudentBlueprint.response(StudentSchema)
    @jwt_required()
    def get(self, id):
        """Get a student by ID"""
        student = student.query.get_or_404(id)
        return student

    @StudentBlueprint.arguments(StudentSchema)
    @StudentBlueprint.response(StudentSchema)
    @jwt_required()
    def put(self, student, id):
        """Update a student by ID"""
        old_student = student.query.get_or_404(id)
        old_student.nStudentBlueprintme = student.name
        old_student.eStudentBlueprintail = student.email
        db.session.commit()
        return old_student

    @StudentBlueprint.response(StudentSchema)
    @jwt_required()
    def delete(self, id):
        """Delete a student by ID"""
        student = student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return student


@StudentBlueprint.route('/courses/int:id/students')
class CourseStudentsView(MethodView):
    @StudentBlueprint.response(StudentSchema(many=True))
    @jwt_required()
    def get(self, id):
        """Get all students registered in a course"""
        course = course.query.get_or_404(id)
        students = [enrollment.student for enrollment in course.enrollments]
        return students


@StudentBlueprint.route('/students/<int:id>/enrollments')
class StudentEnrollmentsView(MethodView):
    @StudentBlueprint.response(EnrollmentSchema(many=True))
    @jwt_required()
    def get(self, id):
        """Get all enrollments for a student"""
        student = student.query.get_or_404(id)
        enrollments = student.enrollments
        return enrollments


@StudentBlueprint.route('/students/int:id/gpa')
class StudentGPAView(MethodView):
    @StudentBlueprint.response()
    @jwt_required()
    def get(self, id):
        """Get the GPA for a student"""
        student = student.query.get_or_404(id)
        gpa = student.calculate_gpa()
        return {'gpa': gpa}

