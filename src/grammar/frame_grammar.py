from grammar.abstract_grammar import AbstractGrammar


class FrameGrammar(AbstractGrammar):
    """
    Грамматика на основе ситуационных фреймов с лексическими ограничениями.
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
        Location -> PREP_LOC NP
        Manner -> ADV
        Instrument -> PREP_INSTR NP

        NP -> N | PRON | ADJ N | ADJ ADJ N | N N
        """

    def get_lexical_rules(self) -> str:
        """
        Добавляет специфичные правила для предлогов
        """
        base_rules = super().get_lexical_rules()

        preposition_rules = """
        PREP_LOC -> 'на' | 'в' | 'у' | 'под' | 'над' | 'около' | 'возле' | 'за' | 'перед'
        PREP_INSTR -> 'с' | 'при' | 'посредством' | 'через' | 'благодаря'
        """

        return base_rules + preposition_rules