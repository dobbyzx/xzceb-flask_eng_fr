'''French/English Translator Module'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION_LT='2018-05-01'
authenticator = IAMAuthenticator(apikey)


language_translator = LanguageTranslatorV3(authenticator=authenticator, version=VERSION_LT)
language_translator.set_service_url(url)

def englishtofrench(englishtext):
    '''Translates English text to French text'''
    translation_response = language_translator.translate(text=str(englishtext), model_id='en-fr')
    translation = translation_response.get_result()
    frenchtext = translation['translations'][0]['translation']
    return frenchtext

def frenchtoenglish(frenchtext):
    '''Translate French text to English text'''
    translation_response = language_translator.translate(text=str(frenchtext), model_id='fr-en')
    translation = translation_response.get_result()
    englishtext = translation['translations'][0]['translation']
    return englishtext
