from entrypoints import text
from grammar.frame_grammar import FrameGrammar
from pos.morphy_pos_tagger import MorphyPosTagger

from process import process_sentences

if __name__ == "__main__":
    pos_tagger = MorphyPosTagger()
    process_sentences(text, pos_tagger, FrameGrammar)
