# Model Schemas
from app import ma

from .user import User


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("email", "name", "username", "role_id", "create_time", "update_time")
        ordered = True
        datetimeformat = '%Y-%m-%d %H:%M:%S'
