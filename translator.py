import requests
from countries import country_codes


class Translator:

    
    def __init__(self):
        language_names, language_codes = list(country_codes.keys()), list(country_codes.values())
    
    def translate(self, input_text, language_from, language_to):

        response = requests.get(f"https://api.mymemory.translated.net/get?q={input_text}&langpair={language_from}|{language_to}")
        translation = response.json()['responseData']['translatedText']
        
        return translation
        

