import requests
from .exceptions_manager import *

class WolframalphaSpeech:
    def __init__(self, API_TOKEN="DEMO"):
        self.requests = requests
        self.url = "http://api.wolframalpha.com/v2/spoken"
        self.API_TOKEN = API_TOKEN
        self.params = {
            "appid": self.API_TOKEN,
        }

    def search(self, query, units=None, timeout=5):
        self.params['i'] = query
        self.params['units'] = units
        self.params['timeout'] = timeout
        r = self.requests.get(self.url, params=self.params)
        text = self.check_for_exceptions(r)
        return text

    def check_for_exceptions(self, request):
        status_code = request.status_code
        text = request.text
        if status_code == 501:
            raise ConfidenceError("In wolframalpha index Query error: The query isn't properly formatted.")
        if status_code == 400:
            raise InternalErro()"Something is wrong with the server, try again.")
        if not text:
            raise ConfidenceError("In wolframalpha index Query error: The query isn't properly formatted.")
        if not request.ok:
            if text is "Error 2: Appid missing":
                raise MissingTokenError("In wolframalpha API error: API TOKEN is missing!")
            else:
                raise InvalidTokenError("In wolframalpha API error: Invalid API TOKEN provided.")
        return text
