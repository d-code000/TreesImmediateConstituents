from abc import ABC, abstractmethod


class POSTagger(ABC):
    @abstractmethod
    def tag(self, tokens: list[str]) -> list[tuple[str, str | None]]:
        """
        Принимает список токенов и возвращает список кортежей (токен, часть речи)
        """
        pass