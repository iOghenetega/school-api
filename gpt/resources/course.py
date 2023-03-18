from flask.views import MethodView
from flask_smorest import Blueprint,abort #
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import db
from schemas import CourseSchema
from sqlalchemy.exc import SQLAlchemyError
from models import course


EnrollmentBlueprint =  Blueprint("enrollment", __name__, description="Operations on enrollment")

@EnrollmentBlueprint.route('/courses')
class CoursesView(MethodView):
    @EnrollmentBlueprint.response(CourseSchema(many=True))
    @jwt_required()
    def get(self):
        """Get all courses"""
        courses = course.query.all()
        return courses

    @EnrollmentBlueprint.arguments(CourseSchema)
    @EnrollmentBlueprint.response(CourseSchema)
    @jwt_required()
    def post(self, course):
        """Create a new course"""
        db.session.add(course)
        db.session.commit()
        return course


@EnrollmentBlueprint.route('/courses/int:id')
class CourseView(MethodView):
    @EnrollmentBlueprint.response(CourseSchema)
    @jwt_required()
    def get(self, id):
        """Get a course by ID"""
        course = course.query.get_or_404(id)
        return course

    @EnrollmentBlueprint.arguments(CourseSchema)
    @EnrollmentBlueprint.response(CourseSchema)
    @jwt_required()
    def put(self, course, id):
        """Update a course by ID"""
        old_course = course.query.get_or_404(id)
        old_course.name = course.name
        old_course.teacher = course.teacher
        db.session.commit()
        return old_course

    @EnrollmentBlueprint.response(CourseSchema)
    @jwt_required()
    def delete(self, id):
        """Delete a course by ID"""
        course = course.query.get_or_404(id)
        db.session.delete(course)
        db.session.commit()
        return course