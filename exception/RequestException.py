from exception import BaseException


class RequestDataFormatException(BaseException):
    pass

class CaptchaValidException(BaseException):
    pass

class GetCaptchaException(BaseException):
    pass
