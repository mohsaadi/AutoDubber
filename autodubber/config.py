import os
from dotenv import load_dotenv

load_dotenv()

SPEECH_KEY = os.getenv('speech_key')
SERVICE_REGION = os.getenv('service_region')

languages = {
    'en': 'en-US',
    'ar': 'ar-SA',
    'es': 'es-ES',
    'fr': 'fr-FR',
    'it': 'it-IT',
    'de': 'de-DE',
    'ru': 'ru-RU'
}

voices = {
    'en': 'en-US-JennyNeural',
    'ar': 'ar-SA-HamedNeural',
    'es': 'es-ES-AlvaroNeural',
    'fr': 'fr-FR-CharlineNeural',
    'it': 'it-IT-BenignoNeural',
    'de': 'de-DE-BerndNeural',
    'ru': 'ru-RU-DariyaNeural'

}