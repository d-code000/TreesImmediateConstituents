from grammar.member_grammar import MemberGrammar
from pos.manual_pos_tagger import ManualPosTagger
from process import process_sentences

if __name__ == "__main__":
    text = """
    Большая собака быстро бежит.
    Мальчик читает интересную книгу.
    Кот спит на диване.
    Красивая птица поёт в саду.
    Умный студент решает сложную задачу.
    Маленький ребёнок играет с игрушкой.
    """

    dictionary = {
        # Существительные
        'собака': 'NOUN',
        'мальчик': 'NOUN',
        'книгу': 'NOUN',
        'кот': 'NOUN',
        'диване': 'NOUN',
        'птица': 'NOUN',
        'саду': 'NOUN',
        'студент': 'NOUN',
        'задачу': 'NOUN',
        'ребёнок': 'NOUN',
        'игрушкой': 'NOUN',

        # Прилагательные
        'большая': 'ADJF',
        'интересную': 'ADJF',
        'красивая': 'ADJF',
        'умный': 'ADJF',
        'сложную': 'ADJF',
        'маленький': 'ADJF',

        # Глаголы
        'бежит': 'VERB',
        'читает': 'VERB',
        'спит': 'VERB',
        'поёт': 'VERB',
        'решает': 'VERB',
        'играет': 'VERB',

        # Наречия
        'быстро': 'ADVB',

        # Предлоги
        'на': 'PREP',
        'в': 'PREP',
        'с': 'PREP',
    }

    pos_tagger = ManualPosTagger(dictionary)
    process_sentences(text, pos_tagger, MemberGrammar)