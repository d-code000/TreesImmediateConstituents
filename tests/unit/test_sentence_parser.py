from sentence_parser import SentenceParser


def test_get_tokenize_sentence():
    text = """
    Большая собака быстро бежит по парку. 
    Маленький кот спит на диване! 
    Умный мальчик читает интересную книгу?
    """

    parser = SentenceParser(text)
    sentences = list(parser.get_tokenize_sentence())

    # Проверяем количество предложений
    assert len(sentences) == 3

    # Проверяем первое предложение
    assert sentences[0] == ['большая', 'собака', 'быстро', 'бежит', 'по', 'парку']

    # Проверяем второе предложение
    assert sentences[1] == ['маленький', 'кот', 'спит', 'на', 'диване']

    # Проверяем третье предложение
    assert sentences[2] == ['умный', 'мальчик', 'читает', 'интересную', 'книгу']

    # Проверяем, что знаки препинания удалены
    for sentence in sentences:
        for token in sentence:
            assert not any(char in token for char in '.!?,;:')