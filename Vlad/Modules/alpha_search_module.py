from Vlad.Modules.base_module import BaseModule
from Vlad.local_libs.wolframalpha_speech.index import WolframalphaSpeech
from Vlad.local_libs.wolframalpha_speech.exceptions_manager import *


class AlphaSearchModule(BaseModule):
    def __init__(self, *args):
        super(AlphaSearchModule, self).__init__(*args)
        self.app_id = self.get_configuration('wolframalpha_search_engine_key')
        if self.app_id:
            self.client = WolframalphaSpeech(self.app_id)
        else:
            return False

    def do_a_search(self):
        status = False
        phrase = ""
        raw_text_array = self.raw_text.split()
        end_index = len(raw_text_array)
        for i in range(0, end_index):
            if status:
                phrase += " " + raw_text_array[i]
            elif raw_text_array[i] == "search":
                status = True
        if status is False:
            return "Can you repeat?"
        phrase = phrase.strip()
        try:
            text = self.client.search(phrase)
        except ConfidenceError:
            return "Forgive me, I was unable to fetch what you have asked for."
        except InternalError:
            return "wolframalpha server error, try again."
        except MissingTokenError:
            return "In modules AlphaSearchModule Api Error: configur the API"
            print("API TOKEN for wolframalpha search engine is missing")
        except InvalidTokenError:
            return "In modules AlphaSearchModule Api Error: configur the API"
            print("API TOKEN for wolframalpha search engine is missing")
        return text
