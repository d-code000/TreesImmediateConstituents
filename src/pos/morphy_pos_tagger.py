import pymorphy3

from pos.pos_tagger_interface import PosTaggerInterface


class MorphyPosTagger(PosTaggerInterface):
    def __init__(self):
        self.morph = pymorphy3.MorphAnalyzer(lang='ru')

    def tag(self, word: str) -> str | None:
        analysis = self.morph.parse(word)[0]
        return analysis.tag.POS