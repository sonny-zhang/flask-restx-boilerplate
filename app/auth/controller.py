from flask import request
from flask_restx import Resource

from app.utils import validation_error

# Auth modules
from .service import AuthService
from .dto import AuthDto
from .utils import LoginSchema, RegisterSchema

api = AuthDto.api
auth_success = AuthDto.auth_success

login_schema = LoginSchema()
register_schema = RegisterSchema()


@api.route("/login")
class AuthLogin(Resource):
    """ User login endpoint
    用户登录后得到用户的信息和token
    """

    auth_login = AuthDto.auth_login

    @api.doc(
        "认证登录",
        responses={
            200: ("登录成功", auth_success),
            400: "请求参数，验证失败",
            403: "密码不正确或凭据不完整",
            404: "根据邮箱没有找到用户",
        },
    )
    @api.expect(auth_login, validate=True)
    def post(self):
        """ 密码登录 """
        # Grab the json data
        login_data = request.get_json()

        # Validate data
        if (errors := login_schema.validate(login_data)) :
            return validation_error(400, errors), 400

        return AuthService.login(login_data)


@api.route("/register")
class AuthRegister(Resource):
    """ User register endpoint
    用户注册后得到用户的信息和token
    """

    auth_register = AuthDto.auth_register

    @api.doc(
        "Auth registration",
        responses={
            200: ("用户注册成功", auth_success),
            400: "数据验证失败",
        },
    )
    @api.expect(auth_register, validate=True)
    def post(self):
        """ 注册用户 """
        # Grab the json data
        register_data = request.get_json()

        # Validate data
        if (errors := register_schema.validate(register_data)) :
            return validation_error(400, errors), 400

        return AuthService.register(register_data)
