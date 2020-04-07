from typing import Tuple
from typing import Any
from PIL import Image

class ResultCutCaptcha(object):
    
    def __init__(self, label: bytes, images: Tuple[bytes, bytes, bytes, bytes, bytes, bytes, bytes, bytes]):
        self.label = label
        self.images = images
        
    @property
    def getLabel(self):
        return self.label
    
    @property
    def getImages(self):
        return self.images
    
    