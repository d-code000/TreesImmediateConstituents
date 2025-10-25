import pytest
from pos.morphy_pos_tagger import MorphyPosTaggerInterface
from pos.manual_pos_tagger import ManualPosTaggerInterface

@pytest.fixture(params=[
    MorphyPosTaggerInterface(),
    ManualPosTaggerInterface({
        "кот": "NOUN",
        "бежит": "VERB",
        "быстро": "ADVB",
        "красивый": "ADJF",
        "%t&ro*s": None
    })
])
def pos_tagger(request):
    return request.param

def test_tag_noun(pos_tagger):
    assert pos_tagger.tag("кот") == "NOUN"

def test_tag_verb(pos_tagger):
    assert pos_tagger.tag("бежит") == "VERB"

def test_tag_adverb(pos_tagger):
    assert pos_tagger.tag("быстро") == "ADVB"

def test_tag_adjective(pos_tagger):
    assert pos_tagger.tag("красивый") in ["ADJF", "ADJ"]

def test_tag_unknown_word(pos_tagger):
    assert pos_tagger.tag("%t&ro*s") is None