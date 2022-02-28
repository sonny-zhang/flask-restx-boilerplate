from typing import Any

def ok_message():
    response_object = {"code": 200, "messages": '操作成功'}
    return response_object


def validation_error(code: int, errors: Any):
    response_object = {"code": code, "errors": errors}

    return response_object


def err_resp(code: int, messages: Any, reason: Any, status_code: int):
    err = dict()
    err['code'] = code
    err['messages'] = messages
    err["error_reason"] = reason
    return err, status_code


def err_500_resp(error):
    err = dict()
    err['code'] = 500
    err['messages'] = "程序运行中出现了错误，请联系管理员sonny"
    err["error_reason"] = f"{error}"
    return err, 500
