"""
This module provides functions to translate English text to French and French text to English.
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Load the environment variables from the .env file
load_dotenv()

# Get the API key and URL from the environment variables.
apikey = os.getenv('apikey')
url = os.getenv('url')

# Create an IAM Authenticator with the API key
authenticator = IAMAuthenticator(apikey)

# Create an instance of the IBM Watson Language Translator service
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set the service URL for the instance
language_translator.set_service_url(url)



def english_to_french(english_text):
    """
    Translates English text to French using IBM Watson Language Translator.
    
    Args:
        english_text (str): The text in English to be translated.
        
    Returns:
        str: The translated text in French.
    """

    # Translate the English text to French
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'  # English to French
    ).get_result()

    # Extract the French text from the translations
    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using IBM Watson Language Translator.
    
    Args:
        french_text (str): The text in French to be translated.
        
    Returns:
        str: The translated text in English.
    """

    # Translate the French text to English
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'  # French to English
    ).get_result()

    # Extract the English text from the translations
    english_text = translation['translations'][0]['translation']

    return english_text

print(english_to_french('Hello'))
print(french_to_english('Bonjour'))
