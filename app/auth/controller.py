from flask import request, current_app
from flask_restx import Resource

from libs import resp

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
        responses={
            200: ("请求成功", auth_success),
            400: "请求失败",
            403: resp.PermissionDenied.msg,
            500: resp.ServerError.msg,
        },
    )
    @api.expect(auth_login, validate=True)
    def post(self):
        """ 密码登录 """
        # Grab the json data
        login_data = request.get_json()

        # Validate data
        if (errors := login_schema.validate(login_data)):
            current_app.logger.info(errors)
            return resp.fail(resp.InvalidParams.set_msg(msg=errors))

        return AuthService.login(login_data)


@api.route("/register")
class AuthRegister(Resource):
    """ User register endpoint
    用户注册后得到用户的信息和token
    """

    auth_register = AuthDto.auth_register

    @api.doc(
        responses={
            200: ("请求成功", auth_success),
            400: "请求失败",
        },
    )
    @api.expect(auth_register, validate=True)
    def post(self):
        """ 注册用户 """
        # Grab the json data
        register_data = request.get_json()

        # Validate data
        if (errors := register_schema.validate(register_data)):
            current_app.logger.info(errors)
            return resp.fail(resp.InvalidParams.set_msg(msg=errors))

        return AuthService.register(register_data)
