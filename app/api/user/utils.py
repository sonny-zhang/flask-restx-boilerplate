from flask_restx import marshal
from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length

from app.models.user import User


def load_data(user_db_obj):
    """ Load user's data

    Parameters:
    - User db object
    """
    from app.models.schemas import user_schema
    data = marshal(user_db_obj, user_schema)

    return data


class UserListSchema(Schema):
    """ /auth/login [POST]

    Parameters:
    - Email
    - Password (Str)
    """
    id = fields.Email(description=User.id.info)
    name = fields.Email(description=User.name.info)
    username = fields.Email(description=User.username.info)
    email = fields.Email(description=User.email.info)

