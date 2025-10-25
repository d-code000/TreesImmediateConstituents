from entrypoints import text, dictionary
from grammar.member_grammar import MemberAbstractGrammar
from pos.manual_pos_tagger import ManualPosTagger
from process import process_sentences

if __name__ == "__main__":
    pos_tagger = ManualPosTagger(dictionary)
    process_sentences(text, pos_tagger, MemberAbstractGrammar)