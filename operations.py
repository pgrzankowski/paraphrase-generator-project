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


def get_paraphrase(word: str, param: str):
    all_paraphrases = requests.get(urls[param].format(word=word)).json()
    chosen_paraphrase = choice(all_paraphrases)['word']
    return chosen_paraphrase


def swap_word(sentance: str, keywords: dict):
    result = ''
    for word in sentance.split():
        first_char = word[0]
        last_char = word[-1]
        check_word = word.lower()
        if last_char in punctuation:
            check_word = check_word[:-1]
        if check_word in keywords.keys():
            replacement = keywords[check_word]
            if first_char.isupper():
                replacement = replacement.capitalize()
            if last_char in punctuation:
                replacement += last_char
            result += replacement
        else:
            result += word
        result += ' '
    return result.rstrip() + '\n'


def add_word(sentance: str, keywords: dict):
    result = ''
    for word in sentance.split():
        first_char = word[0]
        last_char = word[-1]
        check_word = word.lower()
        if last_char in punctuation:
            check_word = check_word[:-1]
        if check_word in keywords.keys():
            addition = keywords[check_word]
            if first_char.isupper():
                addition = addition.capitalize()
                word = word.lower()
            result += addition + ' ' + word
        else:
            result += word
        result += ' '
    return result.rstrip() + '\n'


def perform_operation(text_lines: list, keywords: list, param: str, operation):
    result = []
    assigned_keywords = {}
    for keyword in keywords:
        try:
            assigned_keywords[keyword] = get_paraphrase(keyword, param)
        except IndexError:
            continue
    for line in text_lines:
        result.append(operation(line, assigned_keywords))
    return lines_to_text(result)


def swap_rhymes(input_text: str, keywords: list):
    text_lines = text_to_lines(input_text)
    return perform_operation(text_lines, keywords, 'rhymes', swap_word)


def swap_synonyms(input_text: str, keywords: list):
    text_lines = text_to_lines(input_text)
    return perform_operation(text_lines, keywords, 'synonyms', swap_word)


def add_adjectives(input_text: str, keywords: list):
    text_lines = text_to_lines(input_text)
    return perform_operation(text_lines, keywords, 'adjectives', add_word)
