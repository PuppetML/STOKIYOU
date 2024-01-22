from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize

from googletrans import Translator
import re
import nltk

class Interpreter:

    def __init__(self):

        self.phrase = None
        self.phrase_pt = None
        self.phrase_en = None
        self.base_text = None

    def text_prepare(self, base_text):

        regex_links = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        regex_mentions = r'\b\w+@\w+\b'

        # Remove links
        text_without_link = re.sub(regex_links, '', base_text)

        # Remove @
        text = re.sub(regex_mentions, '', text_without_link)

        return text        

    def translate_phrase(self, phrase_pt):

        text = self.text_prepare(phrase_pt)

        translator = Translator()

        phrase = translator.translate(text).text

        return phrase

    def interpret_context(self, phrase_en):

        phrase = self.translate_phrase(phrase_en)
        
        sid = SentimentIntensityAnalyzer()
        polarity = sid.polarity_scores(phrase)

        if polarity['compound'] <= -0.05:

            tokenize = sent_tokenize(phrase)
            token = word_tokenize(phrase)

            return True