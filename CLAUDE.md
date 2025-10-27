# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a computational linguistics project for parsing Russian sentences using immediate constituent analysis. It builds parse trees from tokenized Russian text using Context-Free Grammars (CFG) and NLTK's ChartParser.

## Core Architecture

### Three-Layer Design Pattern

1. **POS Tagging Layer** (`src/pos/`)
   - `PosTaggerInterface`: Abstract base for all taggers
   - `ManualPosTagger`: Uses a predefined dictionary for POS tagging
   - `MorphyPosTagger`: Uses pymorphy3 for automatic morphological analysis
   - All taggers implement `.tag(word: str) -> str | None` returning tags like 'NOUN', 'VERB', 'ADJF', 'ADVB', 'PREP', etc.

2. **Grammar Layer** (`src/grammar/`)
   - `AbstractGrammar`: Base class that handles word-to-POS mapping and lexical rule generation
   - `FrameGrammar`: Defines sentence structure using situational frames (Agent, Event, Patient, Location, Manner, Instrument)
   - `MemberGrammar`: Defines structure using traditional sentence members (Subject, Predicate, Object, Attribute, Circumstance)
   - Grammar classes generate CFG rules dynamically based on input tokens

3. **Processing Layer** (`src/`)
   - `SentenceParser`: Tokenizes Russian text into sentences and removes punctuation
   - `process.py`: Orchestrates parsing by combining POS tagger + grammar + ChartParser for each sentence

### Key Architectural Pattern

Grammar classes are **instantiated per-sentence** with specific tokens, not globally:
```python
grammar = GrammarClass(pos_tagger, tokens)  # Creates sentence-specific grammar
cfg = grammar.to_cfg()
chart_parser = ChartParser(cfg)
trees = list(chart_parser.parse(tokens))
```

This allows lexical rules to be dynamically generated only for words present in each sentence.

## Running the Code

### Entry Points

There are four main entry points in `src/entrypoints/`:
- `main_frame_grammar_manual.py`: Frame grammar with manual dictionary
- `main_frame_grammar_morphy.py`: Frame grammar with pymorphy3
- `main_member_grammar_manual.py`: Member grammar with manual dictionary
- `main_member_grammar_morphy.py`: Member grammar with pymorphy3

Run any entry point from the project root:
```bash
cd C:\Users\Disha\PycharmProjects\ComputationalLinguistics\TreesImmediateConstituents
python -m src.entrypoints.main_frame_grammar_manual
```

### Testing

Run tests with pytest:
```bash
pytest tests/unit/test_sentence_parser.py
pytest tests/unit/test_pos_tagger.py
```

Run all tests:
```bash
pytest tests/
```

## Key Implementation Details

### Grammar Rule Generation

- `AbstractGrammar._build_word_pos_map()`: Maps each token to its POS tag
- `AbstractGrammar._map_pos_to_grammar_symbol()`: Converts Russian POS tags (NOUN, VERB, ADJF, etc.) to grammar symbols (N, V, ADJ, etc.)
- `AbstractGrammar._generate_lexical_rules()`: Creates rules like `N -> 'собака' | 'кот' | ...` from the word-POS map
- Subclasses implement `get_structural_rules()` to define syntactic structure

### FrameGrammar vs MemberGrammar

- **FrameGrammar**: Models sentences as semantic frames with roles (Agent performs Event on Patient)
  - Has special preposition handling: `PREP_LOC` for location, `PREP_INSTR` for instrument
  - More flexible word order support

- **MemberGrammar**: Traditional grammatical structure (SubjectGroup + PredicateGroup)
  - Stricter word order expectations
  - Simpler preposition handling via `PrepPhrase`

### Sentence Processing Flow

1. `SentenceParser` tokenizes text into sentences using NLTK
2. For each sentence, tokens are lowercased and punctuation removed
3. Grammar instance created with POS tagger and tokens
4. Grammar generates CFG combining structural + lexical rules
5. ChartParser parses tokens, yielding parse trees
6. Trees can be printed via `.pretty_print()` or visualized with `.draw()`

## Dependencies

- `nltk`: Tokenization and chart parsing
- `pymorphy3`: Russian morphological analysis (for morphy-based taggers)
- `pytest`: Testing framework

The code uses modern Python 3.13 with type hints (`list[str]`, `str | None`, etc.).
