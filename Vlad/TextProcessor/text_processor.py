from Vlad.TextProcessor.text_sorter import TextSorter
from Vlad.TextProcessor.text_learner import TextLearner
from Vlad.TextProcessor.module_router import ModuleRouter
from Vlad.configurer import config


class TextProcessor:
    def __init__(self, events):
        self.sorter = TextSorter()
        self.learner = TextLearner()
        self.router = ModuleRouter(events)
        self.c = config

    def process(self, raw_text):
        try:
            explicit = self.c.config.getboolean("SYSTEM", "greet_engine")
            sub_words, key_words = self.sorter.sort(raw_text, explicit=explicit)
            module_info = self.learner.learn(key_words)
            result_speech_text = self.router.inject(module_info, raw_text, sub_words, key_words)
        except Exception as e:
            print(e)
            return None
        return result_speech_text
