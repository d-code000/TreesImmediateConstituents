from abc import ABC, abstractmethod
from nltk import CFG

from pos.pos_tagger_interface import PosTaggerInterface


class AbstractGrammar(ABC):
    def __init__(self, pos_tagger: PosTaggerInterface, tokens: list[str]):
        """
        :param pos_tagger: Теггер для определения частей речи
        :param tokens: Токенизированное предложение (список слов)
        """
        self.pos_tagger = pos_tagger
        self.tokens = tokens
        self.word_pos_map = self._build_word_pos_map()

    def _build_word_pos_map(self) -> dict[str, str]:
        """
        Создаёт словарь: слово -> часть речи для текущего предложения
        """
        word_pos_map = {}
        for word in self.tokens:
            pos = self.pos_tagger.tag(word)
            if pos:
                word_pos_map[word] = pos
        return word_pos_map

    def _map_pos_to_grammar_symbol(self, pos: str) -> str:
        """
        Преобразует POS-теги в символы грамматики
        """
        mapping = {
            'NOUN': 'N',
            'VERB': 'V',
            'ADJF': 'ADJ',
            'ADJS': 'ADJ',
            'ADVB': 'ADV',
            'PREP': 'PREP',
            'CONJ': 'CONJ',
            'PRCL': 'PRCL',
            'NPRO': 'PRON',
        }
        return mapping.get(pos, 'WORD')

    @abstractmethod
    def get_structural_rules(self) -> str:
        """
        Возвращает структурные правила грамматики
        """
        pass

    def _generate_lexical_rules(self) -> str:
        """
        Генерирует правила вида: N -> 'собака' | 'кот' | ...
        """
        pos_words = {}
        for word, pos in self.word_pos_map.items():
            grammar_symbol = self._map_pos_to_grammar_symbol(pos)
            if grammar_symbol not in pos_words:
                pos_words[grammar_symbol] = []
            pos_words[grammar_symbol].append(word)

        rules = []
        for pos, words in pos_words.items():
            words_str = " | ".join([f"'{word}'" for word in words])
            rules.append(f"{pos} -> {words_str}")

        return "\n".join(rules)

    def get_rules(self) -> str:
        """
        Возвращает полные правила грамматики
        """
        structural = self.get_structural_rules()
        lexical = self._generate_lexical_rules()
        return structural + "\n" + lexical

    def to_cfg(self) -> CFG:
        """
        Преобразует правила в объект CFG
        """
        return CFG.fromstring(self.get_rules())