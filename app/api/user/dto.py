from flask_restx import Namespace, fields, reqparse

from app.models.user import User
from app.models.schemas import pagination_schema, user_schema


class UserDto:
    api = Namespace("user", description="用户相关操作")
    api.models[user_schema.name] = user_schema
    api.models[pagination_schema.name] = pagination_schema

    # user_obj = api.model(
    #     "user_object",
    #     {
    #         "email": fields.String(description=User.email.info),
    #         "name": fields.String(description=User.name.info),
    #         "username": fields.String(description=User.username.info),
    #         "roleId": fields.Integer(description=User.role_id.info),
    #         "createTime": fields.DateTime(description=User.create_time.info, format='%Y-%m-%d %H:%M:%S'),
    #         "updateTime": fields.DateTime(description=User.update_time.info, format='%Y-%m-%d %H:%M:%S'),
    #     },
    # )

    search_parse = reqparse.RequestParser(bundle_errors=True)
    search_parse.add_argument('id', type=int)
    search_parse.add_argument('name')
    search_parse.add_argument('username')
    search_parse.add_argument('email')

    data_resp = api.model(
        "Response",
        {
            "code": fields.Integer(example=200),
            "message": fields.String(example='success'),
            "data": fields.Nested(user_schema),
            "pagination": fields.Nested(pagination_schema)
        },
    )
