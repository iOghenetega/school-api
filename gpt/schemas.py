from marshmallow import Schema, fields, validate


class EnrollmentSchema(Schema):
    course_id = fields.Int(required=True)
    student_id = fields.Int(required=True)
    grades = fields.Str(validate=validate.Length(max=255))
    grade_points = fields.Float(dump_only=True)




class CourseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=50))
    teacher = fields.Str(required=True, validate=validate.Length(max=50))
    created_at = fields.DateTime(dump_only=True)



class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=50))
    email = fields.Email(required=True, validate=validate.Length(max=120))
    created_at = fields.DateTime(dump_only=True)
    gpa = fields.Float(dump_only=True)
