import requests
# from random import choice

urls = {
    'rhymes': 'https://api.datamuse.com/words?rel_rhy={word}',
    'synonyms': 'https://api.datamuse.com/words?ml={word}',
    'adjectives': 'https://api.datamuse.com/words?rel_jjb={word}'
}


# TODO
"""
Pobieraj tekst z inputText w taki sposób:
- pobierz tekst do zmiennej (będzie typu: str)
- zastosuj na nim funkcję .split(\n), żeby mieć listę osobnych lini
- stosuj wybraną operację na całej lini żeby przyśpieszyć działanie
"""


def swap_text(text, param: str):
    result = ''
    for word in text.split():
        all_words = requests.get(urls[param].format(word=word)).json()
        if len(all_words) > 0:
            chosen_word = all_words[0]['word']
            result += chosen_word
        else:
            result += word
        result += ' '
    return result.rstrip()


def add_text(text, param: str):
    result = ''
    for word in text.split():
        all_adjectives = requests.get(urls[param].format(word=word)).json()
        if len(all_adjectives) > 0:
            adjective = all_adjectives[0]['word']
            result += adjective + ' ' + word
        else:
            result += word
        result += ' '
    return result.rstrip()


def swap_rhymes(text):
    return swap_text(text, 'rhymes')


def swap_synonyms(text):
    return swap_text(text, 'synonyms')


def add_adjectives(text):
    return add_text(text, 'adjectives')
