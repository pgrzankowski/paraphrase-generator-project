import requests
import json
from string import punctuation
from random import choice


def get_paraphrase_endpoints() -> dict:
    """
    Returns the dict with endpoints for each
    paraphrasing operation.

    Retruns:
        urls (dict): The dict with with endpoints.
    """
    with open('constants/paraphrase_endpoints.json', 'r') as file:
        urls = json.load(file)
    return urls


def lines_to_text(lines: list) -> str:
    """
    Takes list of strings as an argument.
    Transforms it into one string and returns it.

    Parameters:
        lines (list): List of sentances (str).

    Returns:
        text (str): The text made by connecting strings
                    in from the list.
    """
    text = ''
    for line in lines:
        text += line
    return text


def text_to_lines(text: str) -> list:
    """
    Takes string as an argument.
    Transforms it into a list of its substrings
    where '\n' is the separator and retruns that list.

    Parameters:
        text (str): Text with sentances separeted by '\\n'.

    Returns:
        lines (list): List of sentences (str).
    """
    lines = text.split('\n')
    return [line + '\n' for line in lines][:-1]


def get_paraphrase(word: str, param: str) -> str:
    """
    Takes word and paraphrasing option as arguments.
    Gets random paraphrase of the chosen option (rhyme, synonym, etc.)
    of the word and returns it.

    Parameters:
        word (str): Word for which paraphrased will be picked.
        param (str): Parameter which describes which endpoint
                     will be used.

    Returns:
        chosen_paraphrase (str): Paraphrase chosen for given word.
    """
    urls = get_paraphrase_endpoints()
    all_paraphrases = requests.get(urls[param].format(word=word)).json()
    chosen_paraphrase = choice(all_paraphrases)['word']
    return chosen_paraphrase


def swap_word(sentence: str, keywords: dict) -> str:
    """
    Takes a sentance and dictionary of keywords with their
    replacements which will be swaped.
    Replaces all keywords in the given sentance with their
    paraphrases and returns new sentance created that way.

    Parameters:
        sentence (str): Sentence with some words.
        keywords (str): Dictionary of from some words in the sentence
                        and words to replace them.

    Result:
        result (str): Sentence with replaced words.
    """
    result = ''
    for word in sentence.split():
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


def add_word(sentence: str, keywords: dict) -> str:
    """
    Takes a sentance and dictionary of keywords with words
    which will be added before them in text.
    Adds all mapped words before keywords in the given sentance
    with and returns new sentance created that way.

    Parameters:
        sentence (str): Sentence with some words.
        keywords (str): Dictionary of from some words in the sentence
                        and words to add before them.

    Result:
        result (str): Sentence with added words.
    """
    result = ''
    for word in sentence.split():
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


def perform_operation(text_lines: list, keywords: list, param: str,
                      operation) -> str:
    """
    Performs chosen operation on list of strings (text_lines)
    and returns it as one string.

    Parameters:
        text_lines (list): List of sentences (str) on which given
                           operation will be performed.
        keywords (list): List of keywords which will get paraphrase
                         word assigned to them.
        param (str): Parameter which describes which endpoint will
                     be used.
        operation (function): Operation which will be performed
                              on the text_lines.
    Result:
        result (str): Paraphrased text.
    """
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


def swap_rhymes(input_text: str, keywords: list) -> str:
    """
    Swaps keywords in given text to their rhymes
    and return result.

    Parameters:
        input_text (str): Text on which operation will be executed.
        keywords (list): List of words which will be replaced with
                         their random rhymes.

    Result:
        text (str): Text with its keywords replaced with rhymes.
    """
    text_lines = text_to_lines(input_text)
    return perform_operation(text_lines, keywords, 'rhymes', swap_word)


def swap_synonyms(input_text: str, keywords: list) -> str:
    """
    Swaps keywords in given text to their synonyms
    and return result.

    Parameters:
        input_text (str): Text on which operation will be executed.
        keywords (list): List of words which will be replaced with
                         their random synonyms.

    Result:
        text (str): Text with its keywords replaced with synonyms.
    """
    text_lines = text_to_lines(input_text)
    return perform_operation(text_lines, keywords, 'synonyms', swap_word)


def swap_homophones(input_text: str, keywords: list) -> str:
    """
    Swap keywords in given text to their homophones
    and return result.

    Parameters:
        input_text (str): Text on which operation will be executed.
        keywords (list): List of words which will be replaced with
                         their random homophones.

    Result:
        text (str): Text with its keywords replaced with homophones.
    """
    text_lines = text_to_lines(input_text)
    return perform_operation(text_lines, keywords, 'homophones', swap_word)


def swap_homonyms(input_text: str, keywords: list) -> str:
    """
    Swap keywords in given text to their homonyms
    and return result.

    Parameters:
        input_text (str): Text on which operation will be executed.
        keywords (list): List of words which will be replaced with
                         their random homonyms.

    Result:
        text (str): Text with its keywords replaced with homonyms.
    """
    text_lines = text_to_lines(input_text)
    return perform_operation(text_lines, keywords, 'homonyms', swap_word)


def add_adjectives(input_text: str, keywords: list) -> str:
    """
    Adds adjectives before keywords in given text
    and return result.

    Parameters:
        input_text (str): Text on which operation will be executed.
        keywords (list): List of words to which random adjectives
                         will be added.

    Result:
        text (str): Text with adjectives added before its keywords.
    """
    text_lines = text_to_lines(input_text)
    return perform_operation(text_lines, keywords, 'adjectives', add_word)
