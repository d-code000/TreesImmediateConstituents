from grammar.abstract_grammar import AbstractGrammar


class FrameGrammar(AbstractGrammar):
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
                S -> Event 
                S -> Agent Event 
                S -> Event Patient 
                S -> Agent Event Patient 
                S -> Manner Event 
                S -> Agent Manner Event 
                S -> Event Patient Location 
                S -> Agent Event Patient Location 
                S -> Manner Agent Event Patient
                S -> Agent Event Location 
                S -> Agent Event Instrument

                Event -> V | ADV V
                Agent -> NP
                Patient -> NP
                Location -> PP
                Manner -> ADV | PP
                Instrument -> PP

                NP -> N | PRON | ADJ N | ADJ ADJ N | N N
                PP -> PREP N | PREP ADJ N | PREP NP
                """