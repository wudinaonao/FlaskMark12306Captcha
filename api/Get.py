from flask import jsonify, Blueprint, request
import Config
from controller.utils import RequestUtils
from controller.utils import ResponseUtils
from controller import PreCheck
from entities import RequestMark
from entities import ResponseGeneral
from constants import ResponseStatus
from controller import PreCheck
import json
from controller import GetCaptcha


get = Blueprint("get", __name__, url_prefix="/{}/api/{}/get".format(Config.APP_NAME, Config.APP_VERSION))


@get.route("/captcha", methods=["GET"])
def getCaptchaFrom12306():
    """get captcha from 12306"""
    # RequestUtils.checkPostDataIsJson(request)
    # from Initialization import scheduler
    # requetsMark = RequestMark(request.json)
    # PreCheck.checkImageIsValid(requetsMark.originCaptcha)
    # resultMarked = scheduler.markCaptcha(requetsMark)
    
    return ResponseUtils.responseJson(ResponseGeneral(
        status=ResponseStatus.SUCCESS,
        message="mark successfully",
        result=GetCaptcha.getCaptchaFrom12306()
    ))