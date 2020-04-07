import json
import requests
from exception import GetCaptchaException


class GetCaptcha(object):

    @classmethod
    def getCaptchaFrom12306(cls) -> str:
        '''
        获取12306验证码
        :return: base64 string
        '''
        url = "https://kyfw.12306.cn/passport/captcha/captcha-image64"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
        }
        req = requests.get(url=url, headers=headers)
        json_data = json.loads(req.content)
        if json_data['result_message'] == "系统维护时间":
            raise GetCaptchaException("system maintenance, get captcha failed.")
        return json_data['image']