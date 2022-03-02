from flask import request, current_app
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import UserService, UserListService
from .dto import UserDto
from .utils import UserListSchema
from libs import resp

api = UserDto.api
data_resp = UserDto.data_resp
search_parse = UserDto.search_parse
user_list_schema = UserListSchema()


# TODO 待完成
@api.route('')
class UserList(Resource):
    @api.doc(
        responses={
            200: ("请求成功", data_resp),
            400: "请求失败",
            401: "没有权限",
        },
    )
    @api.expect(search_parse, validate=True)
    @jwt_required()
    def get(self):
        """获取用户列表"""
        args = search_parse.parse_args()
        # Validate data
        if (errors := user_list_schema.validate(args)):
            current_app.logger.info(errors)
            return resp.fail(resp.InvalidParams.set_msg(msg=errors))

        uId = args.get('id', None)
        email = args.get('email', None)
        name = args.get('name', None)
        username = args.get('username', None)

        data = User.query.filter_by(id=uId, email=email, name=name, username=username).Order_by(User.id).all()
        return resp.ok(data=data)

    # def post(self):
    #     """批量创建用户"""
    #     pass


@api.route("/<string:username>")
class User(Resource):
    @api.doc(
        responses={
            200: ("请求成功", data_resp),
            400: "请求失败",
        },
    )
    @jwt_required()
    def get(self, username):
        """ 根据username得到用户数据 """
        return UserService.get_user_data(username)
