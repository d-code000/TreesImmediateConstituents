import pymorphy3

from pos_tagger import PosTagger


class MorphyPosTagger(PosTagger):
    def __init__(self):
        self.morph = pymorphy3.MorphAnalyzer(lang='ru')

    def tag(self, word: str) -> str | None:
        analysis = self.morph.parse(word)[0]
        return analysis.tag.POS