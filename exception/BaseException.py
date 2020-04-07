from enum import Enum


class BaseException(Exception):
    
    STATUS_CODE = 200
    
    def __init__(self, status: Enum, message: str, statusCode=None, payload=None):
        super().__init__()
        self.status = status
        self.message = message
        if statusCode is not None:
            self.statusCode = statusCode
        else:
            self.statusCode = self.STATUS_CODE
        self.payload = payload
    
    def toDict(self):
        rv = dict(self.payload or ())
        rv["statusCode"] = int(self.statusCode)
        rv["status"] = self.status.value
        rv["message"] = self.message
        return rv
    
    def __str__(self):
        return self.message
