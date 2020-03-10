import urllib3
import urllib.parse
import json

class translate(object):
	def __init__(self, auth, text, lang):
		instance = urllib3.PoolManager()
		translatePath = {"q": text}
		translateEncode = urllib.parse.urlencode(translatePath)
		translateRequest = instance.request("POST", f"https://translation.googleapis.com/language/translate/v2/?{translateEncode}&target={lang}&key={auth}")
		self.translateInfo = translateRequest.data

	def languages(self, lang=None):
		with open("googleapi/types/languages.json", "r") as read_language:
			languageType = read_language.read()
			if lang:
				langCleaned = json.loads(languageType)
				langDumped = json.dumps(langCleaned)
				all_lang = json.loads(langDumped)["languages"]

				return all_lang[lang]
			return languageType

	def translateParsed(self, title=False, formatting=False):
		translateCleaned = json.loads(self.translateInfo)
		translateDumped = json.dumps(translateCleaned)

		translateData = json.loads(translateDumped)["data"]
		translateDataDumped = json.dumps(translateData)

		translations = json.loads(translateDataDumped)["translations"][0]
		translationsDumped = json.dumps(translations)
		translatedText = json.loads(translationsDumped)["translatedText"]
		
		sourceLanguage = json.loads(translationsDumped)["detectedSourceLanguage"]
		
		parsed = {"translated": translatedText, "src_lang": sourceLanguage}
		parsedTitle = {"translations": {"translated": translatedText, "src_lang": sourceLanguage}}
		if formatting is False and title is False:
			return parsed
		
		if title is True and formatting is True:
			return json.dumps(parsedTitle, indent=4)
		elif title is False and formatting is True:
			return json.dumps(parsed, indent=4)