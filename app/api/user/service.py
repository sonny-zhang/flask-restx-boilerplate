from flask import current_app

from app.models.user import User
from libs import resp


class UserService:
    @staticmethod
    def get_user_data(username):
        """ Get user data by username """
        if not (user := User.query.filter_by(username=username).first()):
            return resp.fail(resp.InvalidRequest.set_msg('没有找到用户'))

        from .utils import load_data

        try:
            user_data = load_data(user)
            return resp.ok(data=user_data)

        except Exception as error:
            current_app.logger.error(error)
            return resp.fail(resp.ServerError)


class UserListService:
    @staticmethod
    def get_user_list_data(parameters):
        uId = parameters.get('id', None)
        email = parameters.get('email', None)
        name = parameters.get('name', None)
        username = parameters.get('username', None)

        data = User.query.filter_by(id=uId, email=email, name=name, username=username).Order_by(User.id).all()
        return resp.ok(data=data)
