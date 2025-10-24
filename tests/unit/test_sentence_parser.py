import pytest

from sentence_parser import SentenceParser


@pytest.mark.parametrize("text,expected_tokens", [
    (
            "Большая собака быстро бежит по парку. Маленький кот спит на диване!",
            [
                ['большая', 'собака', 'быстро', 'бежит', 'по', 'парку'],
                ['маленький', 'кот', 'спит', 'на', 'диване']
            ]
    ),
    (
            "Умный мальчик читает интересную книгу?",
            [['умный', 'мальчик', 'читает', 'интересную', 'книгу']]
    ),
    (
            "Привет! Как дела? Всё хорошо.",
            [
                ['привет'],
                ['как', 'дела'],
                ['всё', 'хорошо']
            ]
    ),
    (
            "Солнце светит, птицы поют; природа оживает.",
            [['солнце', 'светит', 'птицы', 'поют', 'природа', 'оживает']]
    ),
    (
            "Стоп!",
            [['стоп']]
    ),
    (
            "",
            []
    ),
])
def test_get_tokenize_sentence(text, expected_tokens):
    parser = SentenceParser(text)
    sentences = list(parser.get_tokenize_sentence())

    assert sentences == expected_tokens