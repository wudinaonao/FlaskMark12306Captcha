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

mark = Blueprint("mark", __name__, url_prefix="/{}/api/{}/mark".format(Config.APP_NAME, Config.APP_VERSION))


@mark.route("", methods=["POST"])
def markCaptcha():
    """mark captcha"""
    RequestUtils.checkPostDataIsJson(request)
    from Initialization import scheduler
    requetsMark = RequestMark(request.json)
    # PreCheck.checkImageIsValid(requetsMark.originCaptcha)
    resultMarked = scheduler.markCaptcha(requetsMark)
    return ResponseUtils.responseJson(ResponseGeneral(
        status=ResponseStatus.SUCCESS,
        message="mark successfully",
        result=json.loads(str(resultMarked))
    ))


@mark.route("lite", methods=["POST"])
def markCaptchaLite():
    """mark captcha lite result"""
    RequestUtils.checkPostDataIsJson(request)
    from Initialization import scheduler
    requetsMark = RequestMark(request.json)
    # PreCheck.checkImageIsValid(requetsMark.originCaptcha)
    resultMarked = scheduler.markCaptcha(requetsMark)
    return ResponseUtils.responseJson(ResponseGeneral(
        status=ResponseStatus.SUCCESS,
        message="mark successfully",
        result=resultMarked.results
    ))