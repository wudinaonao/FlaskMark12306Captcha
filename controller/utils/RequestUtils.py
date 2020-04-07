from controller.utils import ResponseUtils
from constants import ResponseStatus
from flask import request
from functools import wraps
from exception import RequestDataFormatException


class RequestUtils(object):
    
    @staticmethod
    def checkPostDataIsJson(req: request):
        """check post data is json

        check post data if is json type, otherwise
        return invalid exception.

        Args:
            req: flask request object

        Returns:

        """
        if not req.json:
            raise RequestDataFormatException(
                ResponseStatus.FAILED,
                "data invalid, not json.",
                400
            )
        
    # @staticmethod
    # def checkSession(func, *args, **kwargs):
    #     """check session if is valid.
    #
    #     annotation for check session is valid,
    #     if invalid need reset session
    #
    #     Args:
    #         func: target function
    #
    #     Returns:
    #         True  -> target function result
    #         False -> intercept requests, because session is invalid.
    #
    #     """
    #     @wraps(func)
    #     def inner(*args, **kwargs):
    #         from initialization import passwordSession
    #         # first use
    #         if passwordSession.get("password", None) is None:
    #             return ResponseUtils.responseJson(
    #                 ResponseGeneral(
    #                     ResponseStatus.FAILED,
    #                     "Please set a password for the first use."
    #                 )
    #             )
    #         # verification password
    #         if request.cookies.get("SESSION_ID"):
    #             sessionId = request.cookies.get("SESSION_ID")
    #             # failed verification
    #             if sessionId != HashUtils.sha1(passwordSession["password"]):
    #                 return ResponseUtils.responseJson(
    #                     ResponseGeneral(
    #                         ResponseStatus.FAILED,
    #                         "session id is invalid, please input password for reset session."
    #                     )
    #                 )
    #         else:
    #             # session invalid
    #             return ResponseUtils.responseJson(
    #                 ResponseGeneral(
    #                     ResponseStatus.FAILED,
    #                     "session id is invalid, please input password for reset session."
    #                 )
    #             )
    #
    #         return func(*args, **kwargs)
    #
    #     return inner
    
    @staticmethod
    def deleteNoneAttributes(obj: any) -> any:
        """delete attribute is none from instance
        
        Args:
            obj: instance

        Returns: instance

        """
        if obj is None:
            return obj
        attributeNames = obj.__dict__.keys()
        for attributeName in list(attributeNames):
            attribute = getattr(obj, attributeName)
            if attribute is None:
                delattr(obj, attributeName)
        return obj
