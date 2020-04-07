import json


class ResultMarked(object):
    
    def __init__(self, originCaptcha: str, ids: list, results: list, markedCaptcha: str):
        self._originCaptcha = originCaptcha
        self._ids = ids
        self._results = results
        self._markedCatpcha = markedCaptcha
    
    @property
    def originCaptcha(self):
        return self._originCaptcha
    
    @property
    def ids(self):
        return self._ids
    
    @property
    def results(self):
        return self._results
    
    @property
    def markedResult(self):
        return self._markedCatpcha
    
    def __str__(self):
        return json.dumps(
            {
                "originCaptcha": self._originCaptcha,
                "ids": self._ids,
                "results": self._results,
                "markedCaptcha": self._markedCatpcha
            }
        )
