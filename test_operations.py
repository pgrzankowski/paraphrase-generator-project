from operations import (
    swap_rhymes,
    swap_synonyms,
    add_adjectives
)


def test_swap_rhymes():
    assert swap_rhymes('forgetful') == 'fretful'


def test_swap_synonyms():
    assert swap_synonyms('ocean') == 'sea'


def test_add_adjectives():
    assert add_adjectives('ocean') == 'open ocean'
