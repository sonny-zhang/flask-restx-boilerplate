from flask_restx import Namespace, fields

from app.models.user import User
from app.utils import pagination_dict


class UserDto:
    api = Namespace("user", description="用户相关操作")

    user_obj = api.model(
        "user_object",
        {
            "email": fields.String(description=User.email.info),
            "name": fields.String(description=User.name.info),
            "username": fields.String(description=User.username.info),
            "role_id": fields.Integer(description=User.role_id.info),
            "create_time": fields.DateTime(description=User.create_time.info, format='%Y-%m-%d %H:%M:%S'),
            "update_time": fields.DateTime(description=User.update_time.info, format='%Y-%m-%d %H:%M:%S'),
        },
    )

    pagination_obj = api.model(
        "pagination_obj",
        pagination_dict
    )

    data_resp = api.model(
        "Response",
        {
            "code": fields.Integer(example=200),
            "message": fields.String(example='success'),
            "data": fields.Nested(user_obj),
            "pagination": fields
        },
    )


