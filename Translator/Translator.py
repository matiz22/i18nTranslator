import deepl
import os
from dotenv import load_dotenv


class Translator:
    def __init__(self):
        load_dotenv()
        self.translator = deepl.Translator(os.environ.get('api_key'))

    def translate(self, text, lang_code):
        return self.translator.translate_text(text, target_lang=lang_code).text
