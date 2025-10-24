import pymorphy2

from pos_tagger import POSTagger


class MorphyPOSTagger(POSTagger):
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()

    def tag(self, word: str) -> str | None:
        analysis = self.morph.parse(word)[0]
        return analysis.tag.POS