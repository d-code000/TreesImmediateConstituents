from grammar.abstract_grammar import AbstractGrammar


class MemberGrammar(AbstractGrammar):
    def get_structural_rules(self) -> str:
        """
        Возвращает структурные правила по членам предложения
        """
        return """
        S -> SubjectGroup PredicateGroup

        SubjectGroup -> Subject 
        SubjectGroup -> Attribute Subject 
        SubjectGroup -> Subject Attribute

        PredicateGroup -> Predicate 
        PredicateGroup -> Manner Predicate 
        PredicateGroup -> Predicate Object 
        PredicateGroup -> Predicate Circumstance 
        PredicateGroup -> Manner Predicate Object 
        PredicateGroup -> Predicate Object Circumstance

        Subject -> N | PRON
        Predicate -> V
        Object -> N | ADJ N | PRON
        Attribute -> ADJ
        Manner -> ADV
        Circumstance -> PrepPhrase | ADV

        PrepPhrase -> PREP N | PREP ADJ N
        """