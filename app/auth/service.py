from datetime import datetime
from flask import current_app
from flask_jwt_extended import create_access_token

from app import db
from app.utils import ok_message, err_resp, err_500_resp
from app.models.user import User
from app.models.schemas import UserSchema
from libs import resp

user_schema = UserSchema()


class AuthService:
    @staticmethod
    def login(data):
        # Assign vars
        email = data["email"]
        password = data["password"]

        try:
            # Fetch user data
            if not (user := User.query.filter_by(email=email).first()):
                return resp.fail(resp.DataNotFound.set_msg(msg='输入的邮箱与任何帐户不匹配'))
            # 密码错误
            elif user and not user.verify_password(password):
                return resp.fail(resp.InvalidRequest.set_msg(msg='密码错误'))

            user_info = user_schema.dump(user)
            access_token = create_access_token(identity=user.id)

            data = {
                'Authorization': access_token,
                'userItem': user_info
            }
            return resp.ok(data=data)

        except Exception as error:
            current_app.logger.error(error)
            return resp.fail(resp.ServerError.set_msg(error))

    @staticmethod
    def register(data):
        # Assign vars

        ## dto里是必填参数
        email = data["email"]
        username = data["username"]
        password = data["password"]

        ## dtoi里是选填参数
        data_name = data.get("name")

        # Check if the email is taken
        if User.query.filter_by(email=email).first() is not None:
            # return err_resp(code=403, messages="邮箱已经被使用", reason="email_taken", status_code=403)
            return resp.fail(resp.InvalidRequest.set_msg(f'邮箱{email}已经被使用'))

        # Check if the username is taken
        if User.query.filter_by(username=username).first() is not None:
            # return err_resp(code=403, messages="用户名称已经被使用", reason="username_taken", status_code=403)
            return resp.fail(resp.InvalidRequest.set_msg(f'用户名{username}已经被使用'))
        try:
            new_user = User(
                email=email,
                username=username,
                name=data_name,
                password=password,
            )

            db.session.add(new_user)
            db.session.flush()

            # Load the new user's info
            user_info = user_schema.dump(new_user)

            # Commit changes to DB
            db.session.commit()

            # Create an access token
            access_token = create_access_token(identity=new_user.id)

            data = {
                'Authorization': access_token,
                'userItem': user_info
            }
            return resp.ok(data=data)

        except Exception as error:
            current_app.logger.error(error)
            return resp.fail(resp.ServerError.set_msg(error))
