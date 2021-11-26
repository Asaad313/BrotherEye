from Vlad.TextManager.text_recognizer import TextRecognizer
from Vlad.TextManager.speaker import Speaker
from Vlad.configurer import config


class TextManager:
    def __init__(self):
        self.text_recognizer = TextRecognizer()
        self.speaker = Speaker()
        self.c = config

    def get_speech_from_text(self, text):
        option = self.c.config['TTS']['tts_engine'].lower()
        if option == "google":
            try:
                self.text_recognizer.recognize_from_google(text)
            except:
                print("Error with Google speech recoginition, try again.")
            return self
        else:
            raise Exception("Critical error!")

    def save_speech_result(self):
        try:
            return self.text_recognizer.save_speech_from_google()
        except:
            print("Critical Error.")

    def speak_result(self, speech_result_filename):
        option = self.c.config['TTS']['tts_player'].lower()
        if option == "os":
            self.speaker.speak_from_os(speech_result_filename)
        elif option == "mixer":
            self.speaker.speak_from_pygame(speech_result_filename)
        else:
            raise Exception("In text manager Text_manager TTS error: Reconfigure TTS engine settings.")

    def speak(self, text):
        filename = self.get_speech_from_text(text).save_speech_result()
        self.speak_result(filename)
