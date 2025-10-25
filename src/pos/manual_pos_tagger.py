from pos.pos_tagger_interface import PosTaggerInterface


class ManualPosTagger(PosTaggerInterface):
    def __init__(self, dictionary: dict[str, str]):
        """
        :param dictionary: Заранее определенный словарь
        """
        self.dictionary = dictionary

    def tag(self, word: str) -> str | None:
        return self.dictionary.get(word.lower())