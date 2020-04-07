import Config
import numpy as np
from PIL import Image
from io import BytesIO
from controller.utils import ConvertFormat


class PreprocessingCaptcha(object):
    
    @classmethod
    def decode(cls, y: list) -> str:
        """decode np array predict result to string"""
        y = np.array(y)
        y = np.argmax(y, axis=2)[:, 0]
        return "".join([Config.LABEL_LIST[x] for x in y])
    
    @classmethod
    def loadData(cls, imageByte: bytes, height: int, width: int, channel: int):
        """load data from image byte to np array"""
        x = np.zeros((1, height, width, channel), dtype=np.float32)
        # read to image object
        image = Image.open(BytesIO(imageByte)).convert("RGB")
        # convert format
        image = ConvertFormat.convertImageFormat(image)
        # resize image
        image = image.resize((width, height), Image.ANTIALIAS)
        # convert channel
        imageArray = ConvertFormat.convertImageToArrayByChannel(image, channel)
        # normalization
        x[0] = imageArray / 255.0
        return x
    
if __name__ == '__main__':
    
    pass