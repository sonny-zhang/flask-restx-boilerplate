from typing import Union
from flask_restx._http import HTTPStatus as http_status


# from . import status as http_status


class Resp(object):
    def __init__(self, code: int, msg: str, status_code: int):
        self.code = code
        self.msg = msg
        self.status_code = status_code

    def set_msg(self, msg):
        self.msg = self.msg + ': ' + str(msg)
        return self


InvalidRequest: Resp = Resp(1000, "无效的请求", http_status.BAD_REQUEST)
InvalidParams: Resp = Resp(1002, "无效的参数", http_status.BAD_REQUEST)
BusinessError: Resp = Resp(1003, "业务错误", http_status.BAD_REQUEST)
DataNotFound: Resp = Resp(1004, "查询失败", http_status.BAD_REQUEST)
DataStoreFail: Resp = Resp(1005, "新增失败", http_status.BAD_REQUEST)
DataUpdateFail: Resp = Resp(1006, "更新失败", http_status.BAD_REQUEST)
DataDestroyFail: Resp = Resp(1007, "删除失败", http_status.BAD_REQUEST)
PermissionDenied: Resp = Resp(1008, "权限拒绝", http_status.FORBIDDEN)
ServerError: Resp = Resp(5000, "服务器繁忙", http_status.INTERNAL_SERVER_ERROR)


def ok(*, data: Union[list, dict, str] = None, pagination: dict = None, msg: str = "success"):
    status_code = http_status.OK
    obj = {
            'code': 200,
            'msg': msg,
            'data': data,
            'pagination': pagination
        }

    return obj, status_code


def fail(resp: Resp):
    status_code = resp.status_code
    obj = {
            'code': resp.code,
            'msg': resp.msg,
        }
    return obj, status_code
