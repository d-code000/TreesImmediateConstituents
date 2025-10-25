from nltk.parse import ChartParser

from pos.pos_tagger_interface import PosTaggerInterface
from sentence_parser import SentenceParser


def process_sentences(text: str, pos_tagger: PosTaggerInterface, grammar_class):
    """
    Обрабатывает несколько предложений

    :param text: Текст с предложениями
    :param pos_tagger: Теггер частей речи
    :param grammar_class: Класс грамматики (MemberGrammar или другой)
    """
    # Токенизация всех предложений
    parser = SentenceParser(text)
    sentences = list(parser.get_tokenize_sentence())

    # Обрабатываем каждое предложение отдельно
    for i, tokens in enumerate(sentences, 1):
        print(f"\n{'=' * 60}")
        print(f"Предложение {i}: {' '.join(tokens)}")
        print('=' * 60)

        # Создаём грамматику для конкретного предложения
        grammar = grammar_class(pos_tagger, tokens)

        cfg = grammar.to_cfg()
        chart_parser = ChartParser(cfg)

        trees = list(chart_parser.parse(tokens))

        if trees:
            for j, tree in enumerate(trees, 1):
                print(f"\nВариант разбора {j}:")
                tree.pretty_print()
                # Если нужен UI через Tkinter
                # tree.draw()
        else:
            print("Не удалось разобрать предложение")