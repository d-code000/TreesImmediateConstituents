from abc import ABC, abstractmethod


class PosTaggerInterface(ABC):
    @abstractmethod
    def tag(self, word: str) -> str | None:
        """
        :param word: слово
        :return: часть речи (None, если определить невозможно)
        """
        pass