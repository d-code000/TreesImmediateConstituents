from grammar.abstract_grammar import AbstractGrammar


class MemberGrammar(AbstractGrammar):
    def get_structural_rules(self) -> str:
        """
        Возвращает структурные правила по членам предложения
        """
        return """
        S -> SubjectGroup PredicateGroup

        SubjectGroup -> Subject | Attribute Subject | Subject Attribute
        PredicateGroup -> Predicate | Manner Predicate | Predicate Object | Predicate Circumstance | Manner Predicate Object | Predicate Object Circumstance

        Subject -> N | PRON
        Predicate -> V
        Object -> N | ADJ N | PRON
        Attribute -> ADJ
        Manner -> ADV
        Circumstance -> PrepPhrase | ADV

        PrepPhrase -> PREP N | PREP ADJ N
        """