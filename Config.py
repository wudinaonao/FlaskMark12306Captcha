import os
from controller.charset import LABEL


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# general configuration
APP_NAME = "Mark12306Captcha"
APP_VERSION = "v1.0"

# model and mark configuration
MODEL_PATH = {
    "label": os.path.join(CURRENT_DIR, "controller", "models", "Label_12306_SmallCNN4.model"),
    "image": os.path.join(CURRENT_DIR, "controller", "models", "Image_12306_SmallCNN4.model")
}

LABEL_LIST = LABEL

MARK_CONFIG = {
    # captcha size
    "label": {
        "height": 30,
        "width": 63,
        "channel": 1
    },
    "image": {
        "height": 67,
        "width": 67,
        "channel": 3
    }
}

# draw marked result
DRAW_CONFIG = {
    # RGB
    "color": (255, 0, 0),
    "lineSize": 5
}