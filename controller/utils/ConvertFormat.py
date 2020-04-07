from PIL import Image
import os
import Config
import shutil
import numpy as np
from io import BytesIO


class ConvertFormat(object):
    
    @classmethod
    def convertImageToArrayByChannel(cls, image, channel: int):
        '''
        input image (PIL) object convert to array by channel
        :param image: image obj
        :return:      numpy array obj
        '''
        if channel == 3:
            return np.array(image.convert("RGB"))
        if channel == 1:
            imageArray = np.array(image.convert("L"))
            imageArray = np.expand_dims(imageArray, axis=2)
            return imageArray
        return np.array(image.convert("RGB"))

    @classmethod
    def convertImageFormat(cls, image, format="PNG"):
        '''
        input image obj, convert to png format
        :param image: image obj
        :return:      image obj
        '''
        if image is None:
            raise TypeError("image object is none.")
        with BytesIO() as imageIO:
            image.save(imageIO, format=format)
            imageByte = imageIO.getvalue()
        return Image.open(BytesIO(imageByte))