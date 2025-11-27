import requests

class Translator:
    def translate(self, word):
        url = "https://api.mymemory.translated.net/get"
        params = {"q": word, "langpair": "en|es"}
        try:
            response = requests.get(url, params=params)
            data = response.json()
            translation = data["responseData"]["translatedText"]
            return word, translation
        except Exception:
            return word, "Failed"