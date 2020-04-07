import json
import inspect
from exception import RequestDataFormatException
from constants import ResponseStatus


class BaseEntity(object):
    """base entity
    
    the class implement object convert to json string and
    check attributes is none method.
    
    """
    def __str__(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, ensure_ascii=False, indent=4, sort_keys=True)

    def checkAttributesIsNone(self, on: bool = True):
        """check attributes is none
        
        Returns:

        """
        if not on:
            return
        for attributeName in list(self.__dict__.keys()):
            value = getattr(self, attributeName)
            if value is None:
                raise RequestDataFormatException(
                    status=ResponseStatus.FAILED,
                    message="Attribute {} not found.".format(str(attributeName)),
                    statusCode=400
                )

