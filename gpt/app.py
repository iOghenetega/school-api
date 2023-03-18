from flask import Flask
from flask.views import MethodView
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_smorest import Api, Blueprint
from db import db
from config.config import config
# from .resources import course


app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "SM API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db.init_app(app)
jwt = JWTManager(app)
api = Blueprint('api', 'api', url_prefix='/api')
api = Api(app)


# api.register_blueprint(EnrollmentSchema)
# api.register_blueprint(CourseSchema)
# api.register_blueprint(StudentSchema)


if __name__ == 'main':
    app.run(debug=True)
