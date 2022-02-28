from flask_restx import Namespace, fields

from app.models.user import User


class AuthDto:
    api = Namespace("auth", description="认证和获取token")

    user_obj = api.model(
        "用户对象",
        {
            "email": fields.String(description=User.email.info),
            "name": fields.String(description=User.name.info),
            "username": fields.String(description=User.username.info),
            "role_id": fields.Integer(description=User.role_id.info),
            "create_time": fields.DateTime(description=User.create_time.info, format='%Y-%m-%d %H:%M:%S'),
            "update_time": fields.DateTime(description=User.update_time.info, format='%Y-%m-%d %H:%M:%S'),
            "Authorization": fields.String,
        },
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
            "userName": fields.String(required=True, description=User.username.info),
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
            "data": fields.Nested(user_obj)
        },
    )
