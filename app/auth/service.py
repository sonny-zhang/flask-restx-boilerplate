from datetime import datetime
from flask import current_app
from flask_jwt_extended import create_access_token

from app import db
from app.utils import ok_message, err_resp, err_500_resp
from app.models.user import User
from app.models.schemas import UserSchema

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
                return err_resp(
                    code=404,
                    messages="您输入的电子邮件与任何帐户不匹配。",
                    reason="email_404",
                    status_code=404,
                )

            elif user and user.verify_password(password):
                user_info = user_schema.dump(user)

                access_token = create_access_token(identity=user.id)

                resp = ok_message()
                resp['data']['access_token'] = access_token
                resp['data']['user'] = user_info

                return resp, 200

            return err_resp(
                code=401,
                messages="登录失败，可能是密码错误。",
                reason="password_invalid",
                status_code=401
            )

        except Exception as error:
            current_app.logger.error(error)
            return err_500_resp(error)

    @staticmethod
    def register(data):
        # Assign vars

        ## Required values
        email = data["email"]
        username = data["username"]
        password = data["password"]

        ## Optional
        data_name = data.get("name")

        # Check if the email is taken
        if User.query.filter_by(email=email).first() is not None:
            return err_resp(code=403, messages="邮箱已经被使用", reason="email_taken", status_code=403)

        # Check if the username is taken
        if User.query.filter_by(username=username).first() is not None:
            return err_resp(code=403, messages="用户名称已经被使用", reason="username_taken", status_code=403)

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

            resp = ok_message()
            resp['data']["access_token"] = access_token
            resp['data']["user"] = user_info

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return err_500_resp(error)
