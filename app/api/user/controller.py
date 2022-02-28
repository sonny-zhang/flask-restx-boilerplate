from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import UserService
from .dto import UserDto

api = UserDto.api
data_resp = UserDto.data_resp


# TODO 待完成
# @api.route('/')
# class UserList(Resource):
#     @api.doc(
#         responses={
#             200: ("请求成功", data_resp),
#             400: "请求失败",
#         },
#     )
#     def get(self):
#         """获取用户列表"""
#         pass
#
#     def post(self):
#         """批量创建用户"""
#         pass


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
