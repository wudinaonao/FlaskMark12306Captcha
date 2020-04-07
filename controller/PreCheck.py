from PIL import Image
from exception import CaptchaValidException
from io import BytesIO
import base64
from constants import ResponseStatus


class PreCheck(object):
    
    @staticmethod
    def checkImageIsValid(imageBase64: str):
        try:
            Image.open(BytesIO(base64.b64decode(imageBase64))).convert("RGB")
        except IOError:
            raise CaptchaValidException(
                status=ResponseStatus.FAILED,
                message="captcha is invalid, broken data."
            )
