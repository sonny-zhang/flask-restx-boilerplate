from flask_restx import Namespace, fields

from app.models.user import User


class UserDto:
    api = Namespace("user", description="User related operations.")

    user = api.model(
        "User object",
        {
            "email": fields.String(description=User.email.info),
            "name": fields.String(description=User.name.info),
            "username": fields.String(description=User.username.info),
            "role_id": fields.Integer(description=User.role_id.info),
            "create_time": fields.DateTime(description=User.create_time.info),
            "update_time": fields.DateTime(description=User.update_time.info),
        },
    )

    data_resp = api.model(
        "User Data Response",
        {
            "code": fields.Integer,
            "message": fields.String,
            "data": fields.Nested(user),
        },
    )
