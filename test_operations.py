from operations import (
    lines_to_text,
    text_to_lines,
    get_paraphrase,
    swap_word,
    perform_operation,
    swap_rhymes
)


test_var = {
    'lines': [
        'This is the forgetful line!\n',
        'That is the, forgetful one@\n',
        'and it is a third. Perfect\n'
    ],
    'text': 'This is the forgetful line!\n' +
            'That is the, forgetful one@\n' +
            'and it is a third. Perfect\n',
    'operation': [
        'This is the fretful line!\n',
        'That is the, fretful one@\n',
        'and it is a third. Perfect\n'
    ]
}


def pick1st(a):
    return a[0]


def test_lines_to_text():
    lines = test_var['lines']
    text = test_var['text']
    assert text == lines_to_text(lines)


def test_text_to_lines():
    lines = test_var['lines']
    text = test_var['text']
    assert lines == text_to_lines(text)


def test_get_paraphrase(monkeypatch):
    monkeypatch.setattr('operations.choice', pick1st)
    word = 'forgetful'
    paraphrase = get_paraphrase(word, 'rhymes')
    assert paraphrase == 'fretful'


def test_swap_word(monkeypatch):
    monkeypatch.setattr('operations.choice', pick1st)
    sentance = test_var['lines'][0]
    keyword = 'forgetful'
    result = swap_word(sentance, keyword, 'rhymes')
    assert result == 'This is the fretful line!\n'


def test_add_word(monkeypatch):
    monkeypatch.setattr('operations.choice', pick1st)
    sentance = test_var['lines'][0]
    keyword = 'forgetful'
    result = swap_word(sentance, keyword, 'adjectives')
    assert result == 'This is the little line!\n'


def test_perform_operation(monkeypatch):
    monkeypatch.setattr('operations.choice', pick1st)
    text_lines = test_var['lines']
    keyword = 'forgetful'
    result = perform_operation(
        text_lines,
        keyword,
        'rhymes',
        swap_word
        )
    assert result == lines_to_text(test_var['operation'])


def test_swap_rhymes(monkeypatch):
    monkeypatch.setattr('operations.choice', pick1st)
    input_text = test_var['text']
    keyword = 'forgetful'
    result = swap_rhymes(input_text, keyword)
    assert result == lines_to_text(test_var['operation'])
