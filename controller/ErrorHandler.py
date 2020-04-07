"""
Register error handler in flask framework

"""
from flask import jsonify, Blueprint
from exception import RequestDataFormatException
from exception import CaptchaValidException
from exception import GetCaptchaException


errorHandler = Blueprint("errorHandler", __name__)


@errorHandler.app_errorhandler(RequestDataFormatException)
def handleRequestDataFormatException(error):
    response = jsonify(error.toDict())
    response.statusCode = error.statusCode
    return response

@errorHandler.app_errorhandler(CaptchaValidException)
def handleCaptchaValidException(error):
    response = jsonify(error.toDict())
    response.statusCode = error.statusCode
    return response

@errorHandler.app_errorhandler(GetCaptchaException)
def handleGetCaptchaException(error):
    response = jsonify(error.toDict())
    response.statusCode = error.statusCode
    return response

