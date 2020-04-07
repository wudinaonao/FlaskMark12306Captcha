from flask import request, make_response

class ResponseUtils(object):
    

    @staticmethod
    def responseJson(obj: object, headers: dict=None) -> any:
        """convert obj to response object
        
        the method encapsulation the object to flask response
        object and set content type is json.
        you still can custom headers.
        the method need input obj rewrite __str__ method,
        __str__ method return a json string
        
        Examples:
            
            {
                "status": "...",
                ...
            }
        
        Args:
            obj: any object

        Returns: flask response object

        """
        response = make_response(str(obj))
        response.headers["Content-Type"] = "application/json"
        if headers:
            for k, v in headers.items():
                response.headers[str(k)] = v
        return response