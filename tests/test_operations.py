import json
from paraphrase_generator.operations import (
    lines_to_text,
    text_to_lines,
    get_paraphrase,
    swap_word,
    add_word,
    perform_operation,
    swap_rhymes,
    swap_synonyms,
    swap_homophones,
    swap_homonyms,
    add_adjectives,
)

with open('constants/test_data.json', 'r') as file:
    test_data = json.load(file)


def pick1st(a):
    return a[0]


def test_lines_to_text():
    lines = test_data['lines']
    text = test_data['text']
    assert text == lines_to_text(lines)


def test_text_to_lines():
    lines = test_data['lines']
    text = test_data['text']
    assert lines == text_to_lines(text)


def test_get_paraphrase(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    word = 'forgetful'
    paraphrase = get_paraphrase(word, 'rhymes')
    assert paraphrase == 'fretful'


def test_swap_word(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    sentance = test_data['lines'][0]
    keywords = test_data['keywords']
    result = swap_word(sentance, keywords)
    assert result == test_data['swap_result'][0]


def test_add_word(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    sentance = test_data['lines'][0]
    keywords = test_data['keywords']
    result = add_word(sentance, keywords)
    assert result == test_data['add_result'][0]


def test_perform_operation(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    text_lines = test_data['lines']
    keywords = test_data['keywords'].keys()
    result = perform_operation(
        text_lines,
        keywords,
        'rhymes',
        swap_word
        )
    assert result == test_data['text_result']


def test_swap_rhymes(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    input_text = test_data['text']
    keywords = test_data['keywords'].keys()
    result = swap_rhymes(input_text, keywords)
    assert result == test_data['rhymes']


def test_swap_synonyms(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    input_text = test_data['text']
    keywords = test_data['keywords'].keys()
    result = swap_synonyms(input_text, keywords)
    assert result == test_data['synonyms']


def test_swap_homophones_not_found(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    input_text = test_data['text']
    keywords = test_data['keywords'].keys()
    result = swap_homophones(input_text, keywords)
    assert result == test_data['homophones']


def test_swap_homonyms_not_found(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    input_text = test_data['text']
    keywords = test_data['keywords'].keys()
    result = swap_homonyms(input_text, keywords)
    assert result == test_data['homonyms']


def test_add_adjectives(monkeypatch):
    monkeypatch.setattr('paraphrase_generator.operations.choice', pick1st)
    input_text = test_data['text']
    keywords = test_data['keywords'].keys()
    result = add_adjectives(input_text, keywords)
    assert result == test_data['adjectives']
