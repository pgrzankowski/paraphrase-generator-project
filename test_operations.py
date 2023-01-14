from operations import (
    swap_rhymes,
    swap_synonyms,
    add_adjectives,
    lines_to_text,
    text_to_lines,
    swap_words,
    swap_text,
    add_words,
    add_text
)


test_var = {
    'lines': [
        'This is the first line!\n',
        'That is the, second one@\n',
        'and it is a third. Perfect\n'
    ],
    'text': 'This is the first line!\nThat is the, second one@\nand it is a third. Perfect\n'
}


def pick_1st(some_list):
    return some_list[0]


def test_lines_to_text():
    lines = test_var['lines']
    text = lines_to_text(lines)
    assert text == test_var['text']


def test_text_to_lines():
    text = test_var['text']
    lines = text_to_lines(text)
    assert lines == test_var['lines']


def test_swap_words(monkeypatch):
    monkeypatch.setattr('operations.choice', pick_1st)
    line = test_var['lines'][0]
    assert swap_words(line, 'rhymes') == 'Miss riz a burst design!\n'


def test_add_words(monkeypatch):
    monkeypatch.setattr('operations.choice', pick_1st)
    line = test_var['lines'][0]
    assert add_words(line, 'adjectives') == 'Try thisispart thetwenty firstline!\n'


def test_swap_text(monkeypatch):
    pass


def test_add_text(monkeypatch):
    pass


def test_swap_rhymes():
    pass


def test_swap_synonyms():
    pass

def test_add_adjectives():
    pass
