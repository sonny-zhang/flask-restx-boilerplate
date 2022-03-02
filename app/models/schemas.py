# Model Schemas
from flask_restx import fields, Model

from app.models.user import User

pagination_schema = Model(
    'pagination_schema',
    {
        'current_page': fields.Integer(description='当期页码数'),
        'pages': fields.Integer(description='总页码数'),
        'page_size': fields.Integer(description='每页显示的条数'),
        'total_size': fields.Integer(description='总条数'),
    }

)

user_schema = Model(
    'user_schema',
    {
        "id": fields.String(description=User.id.info),
        "email": fields.String(description=User.email.info),
        "name": fields.String(description=User.name.info),
        "username": fields.String(description=User.username.info),
        "roleId": fields.Integer(description=User.role_id.info, attribute=User.role_id.name),
        "createTime": fields.DateTime(description=User.create_time.info, attribute=User.create_time.name,
                                      example='2022-03-01 15:32:01'),
        "updateTime": fields.DateTime(description=User.update_time.info, attribute=User.update_time.name,
                                      example='2022-03-01 15:33:02'),
    }
)
