import requests
# from random import choice

urls = {
    'rhymes': 'https://api.datamuse.com/words?rel_rhy={word}',
    'synonyms': 'https://api.datamuse.com/words?ml={word}',
    'adjectives': 'https://api.datamuse.com/words?rel_jjb={word}'
}


def swap_rhymes(text):
    pass


def swap_synonyms(text):
    pass


def add_adjectives(text):
    result = ''
    for word in text.split():
        all_adjectives = requests.get(urls['adjectives'].format(word=word))
        if len(all_adjectives) > 0:
            adjective = all_adjectives.json()[0]['word']
            result += adjective + ' ' + word
        else:
            result += word
        result += ' '
    return result.rstrip()
