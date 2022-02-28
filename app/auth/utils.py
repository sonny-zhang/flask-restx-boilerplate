# Validations with Marshmallow
from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length

from app.models.user import User


class LoginSchema(Schema):
    """ /auth/login [POST]

    Parameters:
    - Email
    - Password (Str)
    """
    email = fields.Email(required=True, validate=[Length(max=64)], description=User.email.info)
    password = fields.Str(validate=[Length(min=6, max=128)], description='密码')


class RegisterSchema(Schema):
    """ /auth/register [POST]

    Parameters:
    - Email
    - Username (Str)
    - Name (Str)
    - Password (Str)
    """
    email = fields.Email(required=True, validate=[Length(max=64)], description=User.email.info)
    username = fields.Str(
        required=True,
        validate=[
            Length(min=4, max=15),
            Regexp(
                r"^([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)$",
                error="无效的用户名",
            ),
        ],
        description=User.username.info
    )
    name = fields.Str(
        validate=[
            Regexp(
                r"^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$", error="无效的姓名",
            )
        ],
        description=User.name.info
    )
    password = fields.Str(validate=[Length(min=6, max=128)], description='密码')
