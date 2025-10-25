from grammar.grammar import Grammar


class FrameGrammar(Grammar):
    """
    Грамматика на основе ситуационных фреймов.

    Идея: предложение строится вокруг главного события (обычно глагол),
    к которому привязаны участники с определёнными ролями:
    - Agent (Агент) - кто действует
    - Patient (Пациент) - над кем/чем действие
    - Location (Место) - где происходит
    - Time (Время) - когда происходит
    - Manner (Образ действия) - как происходит
    - Instrument (Инструмент) - чем/с помощью чего
    """

    def get_structural_rules(self) -> str:
        """
        Возвращает структурные правила по фреймам
        """
        return """
        S -> Event | Agent Event | Event Patient | Agent Event Patient | Manner Event | Agent Manner Event | Event Patient Location | Agent Event Patient Location | Manner Agent Event Patient

        Event -> V | ADV V
        Agent -> NP
        Patient -> NP
        Location -> PP
        Manner -> ADV | PP

        NP -> N | PRON | ADJ N | ADJ ADJ N | N N
        PP -> PREP N | PREP ADJ N | PREP NP
        """