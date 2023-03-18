from flask.views import MethodView
from flask_smorest import Blueprint,abort #
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import db
from schemas import StudentSchema, CourseSchema, EnrollmentSchema
from sqlalchemy.exc import SQLAlchemyError
from models import enrollment, EnrollmentModel


EnrollmentBlueprint =  Blueprint("enrollment", __name__, description="Operations on enrollment")

@EnrollmentBlueprint.route('/enrollments')
class EnrollmentsView(MethodView):
    @EnrollmentBlueprint.response(EnrollmentSchema(many=True))
    @jwt_required()
    def get(self):
        """Get all enrollments"""
        enrollments = enrollment.query.all()
        return enrollments


    @EnrollmentBlueprint.arguments(EnrollmentSchema)
    @EnrollmentBlueprint.response(EnrollmentSchema)
    @jwt_required()
    def post(self, enrollment):
        """Create a new enrollment"""
        db.session.add(enrollment)
        db.session.commit()
        return enrollment


@EnrollmentBlueprint.route('/enrollments/int:id')
class EnrollmentView(MethodView):
    @EnrollmentBlueprint.response(EnrollmentSchema)
    @jwt_required()
    def get(self, id):
        """Get an enrollment by ID"""
        enrollment = enrollment.query.get_or_404(id)
        return enrollment


    @EnrollmentBlueprint.arguments(EnrollmentSchema)
    @EnrollmentBlueprint.response(EnrollmentSchema)
    @jwt_required()
    def put(self, enrollment, id):
        """Update an enrollment by ID"""
        old_enrollment = enrollment.query.get_or_404(id)
        old_enrollment.course_id = enrollment.course_id
        old_enrollment.student_id = enrollment.student_id
        old_enrollment.grades = enrollment.grades
        old_enrollment.calculate_grade_points()
        db.session.commit()
        return old_enrollment


    @EnrollmentBlueprint.response(EnrollmentSchema)
    @jwt_required()
    def delete(self, id):
        """Delete an enrollment by ID"""
        enrollment = enrollment.query.get_or_404(id)
        db.session.delete(enrollment)
        db.session.commit()
        return enrollment
