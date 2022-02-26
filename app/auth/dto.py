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
            "create_time": fields.DateTime(description=User.create_time.info),
            "update_time": fields.DateTime(description=User.update_time.info),
            "access_token": fields.String,
        },
    )

    auth_login = api.model(
        "登录请求参数",
        {
            "email": fields.String(required=True),
            "password": fields.String(required=True),
        },
    )

    auth_register = api.model(
        "注册请求参数",
        {
            "email": fields.String(required=True, description=User.email.info),
            "username": fields.String(required=True, description=User.username.info),
            # Name is optional
            "name": fields.String(description=User.name.info),
            "password": fields.String(required=True, description='密码'),
        },
    )

    auth_success = api.model(
        "成功认证返回数据",
        {
            "code": fields.Integer(example=200, description='状态码'),
            "message": fields.String,
            "data": fields.Nested(user_obj)
        },
    )
