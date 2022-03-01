from flask_restx import Namespace, fields

from app.models.user import User
from app.models.schemas import user_schema


class AuthDto:
    api = Namespace("auth", description="认证和获取token")
    api.models[user_schema.name] = user_schema

    user_obj = api.model(
        "用户对象",
        {
            'Authorization': fields.String,
            'userItem': fields.Nested(user_schema)
        }
    )

    auth_login = api.model(
        "login_parameters",
        {
            "email": fields.String(required=True, description=User.email.info),
            "password": fields.String(required=True, description='密码'),
        },
    )

    auth_register = api.model(
        "registration_parameters",
        {
            "email": fields.String(required=True, description=User.email.info),
            "username": fields.String(required=True, description=User.username.info),
            # Name is optional
            "name": fields.String(description=User.name.info),
            "password": fields.String(required=True, description='密码'),
        },
    )

    auth_success = api.model(
        "Response",
        {
            "code": fields.Integer(example=200),
            "message": fields.String(example='success'),
            "data": fields.Nested(user_obj),
        },
    )
