import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


class SentenceParser:
    def __init__(self, text):
        self.text = text
        self._download_nltk_resources()

    @staticmethod
    def _download_nltk_resources():
        """Скачивает необходимые ресурсы NLTK"""
        # Todo: возможно сделать умную загрузку по необходимости
        nltk.download('punkt')
        nltk.download('punkt_tab')

    def get_tokenize_sentence(self):
        """
        Итератор, который возвращает токенизированные предложения без знаков препинания.

        Yields:
            list: Список токенов (слов) одного предложения
        """
        sentences = sent_tokenize(self.text, language='russian')

        for sentence in sentences:
            tokens = word_tokenize(sentence, language='russian')

            # Удаляем только явные знаки препинания, оставляем все буквы и цифры
            tokens = [token.lower() for token in tokens if not re.match(r'^[^\w]+$', token, re.UNICODE)]

            if tokens:
                yield tokens