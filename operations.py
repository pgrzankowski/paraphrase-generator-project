import requests
from string import punctuation
from random import choice

urls = {
    'rhymes': 'https://api.datamuse.com/words?rel_rhy={word}',
    'synonyms': 'https://api.datamuse.com/words?ml={word}',
    'adjectives': 'https://api.datamuse.com/words?rel_jjb={word}'
}


def lines_to_text(lines: list):
    text = ''
    for line in lines:
        text += line
    return text


def text_to_lines(text: str):
    lines = text.split('\n')
    return [line + '\n' for line in lines][:-1]


def swap_words(line: str, param: str):
    new_line = ''
    for word in line.split():
        last_char = ''
        if word[-1] in punctuation:
            last_char = word[-1]
            word = word[:-1]
        all_words = requests.get(urls[param].format(word=word.lower())).json()
        if len(all_words) > 0:
            chosen_word = choice(all_words)['word']
        else:
            new_line += word
            continue
        if word[0].isupper():
            chosen_word = chosen_word.capitalize()
        chosen_word += last_char
        new_line += chosen_word + ' '
    return new_line.rstrip() + '\n'


def swap_text(text: list, param: str):
    result = []
    for line in text:
        new_line = swap_words(line, param)
        result.append(new_line)
    return result


def add_words(line: str, param: str):
    new_line = ''
    for word in line.split():
        all_words = requests.get(urls[param].format(word=word)).json()
        if len(all_words) > 0:
            chosen_word = choice(all_words)['word']
        else:
            new_line += word
            continue
        if word[0].isupper():
            chosen_word = chosen_word.capitalize()
            word = word.lower()
        new_line += chosen_word + ' ' + word
    return new_line.rstrip() + '\n'


def add_text(text: list, param: str):
    result = []
    for line in text:
        new_line = add_words(line, param)
        result.append(new_line)
    return result


def swap_rhymes(text):
    return swap_text(text, 'rhymes')


def swap_synonyms(text):
    return swap_text(text, 'synonyms')


def add_adjectives(text):
    return add_text(text, 'adjectives')
