from constants import ResponseStatus
from enum import Enum
import json


class ResponseGeneral(object):
    
    def __init__(self, status: Enum, message: str, **kwargs):
        self.status = status.value
        self.message = message
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def __str__(self):
        jsonObj = dict()
        args = self.__dict__.keys()
        for arg in args:
            jsonObj.setdefault(arg, getattr(self, arg))
        return json.dumps(jsonObj)


if __name__ == '__main__':
    print(ResponseGeneral(
        ResponseStatus.SUCCESS,
        "request success.",
        count=[{"task": "naonao"}]
    ))