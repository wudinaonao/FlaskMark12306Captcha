from entities import BaseEntity


class RequestMark(BaseEntity):
    
    def __init__(self, requestJson: dict):
        self._originCaptcha = requestJson.setdefault("originCaptcha", None)

        self.checkAttributesIsNone()
        
    @property
    def originCaptcha(self) -> str:
        return self._originCaptcha
